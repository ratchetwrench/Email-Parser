#!/usr/bin/env python
#
# Very basic example of using Python 3 and IMAP to iterate over emails in a
# gmail folder/label.  This code is released into the public domain.
#
# This script is example code from this blog post:
# http://www.voidynullness.net/blog/2013/07/25/gmail-email-with-python-via-imap/
#
# This is an updated version of the original -- modified to work with Python 3.4.
#
import sys
import imaplib
import getpass
import email
import datetime
import configparser
from logging import DEBUG


try:
    config = configparser.ConfigParser()
    config.read("config.ini")

    EMAIL_ACCOUNT = config['email']['email_account']
    CREDENTIALS = config['email']['credentials']
    EMAIL_FOLDER = config['email']['email_folder']
    IMAP4_SSL_PORT = config['email']['imap4_ssl_port']
    DOMAIN = config['email']['domain']

    MAILBOX = imaplib.IMAP4_SSL(DOMAIN, IMAP4_SSL_PORT)

    if DEBUG:
        print(config.read('config.ini'))

except configparser.Error as e:
    print(e)


def process_mailbox(mail_box):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """
    # Search mailbox for matching messages
    rv, data = mail_box.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = mail_box.fetch(num, '(RFC822)')
        """Fetch (parts of) messages.
        message_parts should be a string of message part names,
        enclosed within parentheses, eg: "(UID BODY[TEXT])".
        Returned data are tuples of message part envelope and data.
        """
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(
            email.header.decode_header(msg['Subject']))
        subject = str(hdr)
        print('Message %s: %s' % (num, subject))
        print('Raw Date:', msg['Date'])
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print("Local Date:", local_date.strftime("%a, %d %b %Y %H:%M:%S"))

try:
    rv, data = mail_box.login(EMAIL_ACCOUNT, getpass.getpass())
except imaplib.IMAP4.error:
    print("Login Failed")
    sys.exit(1)

print(rv, data)

rv, mailboxes = mail_box.list()
if rv == 'OK':
    print("Mailboxes:")
    print(mailboxes)

rv, data = mail_box.select(EMAIL_FOLDER)
if rv == 'OK':
    print("Processing mailbox...\n")
    process_mailbox(mail_box)
    mail_box.close()
else:
    print("ERROR: Unable to open mailbox ", rv)

mail_box.logout()

#---------------------------#
#                           #
# I added this stuff below  #
#                           #
#---------------------------#
with IMAP4(MAILBOX) as M:
# Do something...

if __name__ == '__main__':
    try:
        rv, data = MAILBOX.login(EMAIL_ACCOUNT, CREDENTIALS)
        while True:
            process_mailbox(MAILBOX)
    except ValueError as e:
        print(e)
    finally:
        print("Exiting...")
