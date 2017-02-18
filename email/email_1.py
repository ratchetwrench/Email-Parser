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
import datetime
import getpass
import imaplib
import sys

# TODO: create email reader
"""EmailReader
Takes unread Outlook emails from specified folder
Opens the email and reads into an object.
"""

EMAIL_ACCOUNT = "notatallawhistleblowerIswear@gmail.com"

# Use 'INBOX' to read inbox.  Note that whatever folder is specified,
# after successfully running this script all emails in that folder
# will be marked as read.
EMAIL_FOLDER = "Top Secret/PRISM Documents"


def process_mailbox(mail_box):
    """
    Do something with emails messages in the folder.
    For the sake of this example, print some headers.
    """

    rv, data = mail_box.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = mail_box.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = email_1.message_from_bytes(data[0][1])
        hdr = email_1.header.make_header(
            email_1.header.decode_header(msg['Subject']))
        subject = str(hdr)
        print('Message %s: %s' % (num, subject))
        print('Raw Date:', msg['Date'])
        # Now convert to local date-time
        date_tuple = email_1.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email_1.utils.mktime_tz(date_tuple))
            print("Local Date:", local_date.strftime("%a, %d %b %Y %H:%M:%S"))


mail_box = imaplib.IMAP4_SSL('imap.outlook.com')

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