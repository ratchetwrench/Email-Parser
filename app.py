#!/usr/bin/python
"""Email Parser
__author__ = 'David Wrench'
__version__ = '0.1.0'
"""
import re
from datetime import datetime
import datetime
import email_1.header
import getpass
import imaplib
import sys
import email_1


EMAIL_ACCOUNT = "example@outlook.com"
EMAIL_FOLDER = "Inbox/Vendors/SMS/Notifications"
DEBUG = True

with open('/Users/david/dev/email-parser/notification.txt', 'r') as f:
    email_notification = f.read()


def parse_email(notification):
    """Given an email return the desired contents.
    :return: result
    """
    # TODO: Do something with the email

    category = r'Category: (?P<category>[\w].*)'
    # print(category.group(1))

    incident_number = r': (?P<incident_number>INC[\d]{12})'
    # print(incident_number.group(1))

    content = re.compile('INC[\d]*\n\n(?P<content>.*)Customer Impact:',
              re.DOTALL)\
        .search(notification)
    content = content.group(1).strip()
    # print(re.sub(r'Super Secret Provider', r'Our SMS Provider',

    customer_impact = r'Customer Impact: (?P<customer_impact>[\w].*)'
    # print(customer_impact.group(1))

    # TODO: get affected carriers
    carriers_affected = r'Carriers Affected: (?P<carriers_affected>[\w].*)'
    if carriers_affected:
        pass
        print(carriers_affected.group(1))
    else:
        carriers_affected = parse_attachment(email_attachment)

    # Tuesday, January 31, 2017 3:42:34 PM
    rfc_1123 = "%A, %B %d, %Y %H:%M:%S %p"
    iso_8601 = "%Y-%m-%dT%H:%M:%S"
    # TODO: fix notification date and string date parsing
    sent_date = re.compile(r'Sent: (?P<sent_date>[\w]+\,'  # %A,
                           r'\s[\w]+'  # %B
                           r'\s[\d]{1,2}\,'  # %d,
                           r'\s[\d]{4}\s'  # %Y
                           r'[\d]{1,2}\:[\d]{1,2}\:[\d]{1,2}'  # HH:MM:SS
                           r'\s[\w]{2})').search(notification)  # AM/PM

    # print(type(sent_date))
    # sent_date_obj = datetime.strptime(sent_date, rfc_1123).tzinfo('CST')
    # notification_date = sent_date_obj.strftime(iso_8601).tzinfo('UTC')

    if sent_date:
        print(sent_date.group(1))
    else:
        print("TBD")

    start_date = re.compile(r'Start Date[\/]Time: (?P<start_date>[\w].*)')\
        .search(notification)
    if start_date:
        print(start_date.group(1))
    else:
        print("TBD")

    end_date = re.compile(r'Expected End Date[\/]Time: (?P<end_date>[\w].*)')\
        .search(notification)
    if end_date:
        print(end_date.group(1))
    else:
        print("TBD")

    expected_end_date = r'Expected End Date[\/]Time: (?P<expected_end_date>[\w].*)'
    if expected_end_date:
        print(expected_end_date.group(1))
    else:
        print("TBD")

    patterns = re.compile(category,
                          incident_number)

    result = patterns.search(notification)

    print(result)


def parse_attachment(email_attachment):
    """Retrieves a list of affected carriers from an attachment
If there is an attachment, the affected operators are stored in here line bu line.
If there is not attachment and the "Affected Operators:" regex is found it will either say
"See Attached List" OR Have them listed in the regex.
If neither is present they might be listed in the body. Should search the body against
a known list of operators.
    :return: affected_carriers[]
    """
    with open(email_attachment) as attachment:
        carriers = attachment.readlines()

    affected_carriers = [carrier.strip() for carrier in attachment]

    return affected_carriers
