#!/usr/bin/python
"""Email Parser
__author__ = 'David Wrench'
__version__ = '0.1.0'
"""
import re

with open('/Users/david/dev/email-parser/notification.txt', 'r') as f:
    email_notification = f.read()


def parse_email(notification, email_attachment=None):
    """Given an email return the desired contents.
    :return: result
    """
    # TODO: Do something with the email

    category = r'Category: (?P<category>[\w].*)'
    incident_number = r': (?P<incident_number>INC[\d]{12})'
    content = re.compile('INC[\d]*\n\n(?P<content>.*)Customer Impact:',
                         re.DOTALL) \
        .search(notification)
    content = content.group(1).strip()
    customer_impact = r'Customer Impact: (?P<customer_impact>[\w].*)'
    # TODO: get affected carriers
    carriers_affected = r'Carriers Affected: (?P<carriers_affected>[\w].*)'
    if carriers_affected:
        carriers_affected = carriers_affected.group(1)
    else:
        carriers_affected = parse_attachment(email_attachment)

    # Tuesday, January 31, 2017 3:42:34 PM to YYYY-MM-DDTHH:MM:SS
    rfc_1123 = "%A, %B %d, %Y %H:%M:%S %p"
    iso_8601 = "%Y-%m-%dT%H:%M:%S"
    sent_date = re.compile(r'Sent: (?P<sent_date>[\w]+\,'  # %A,
                           r'\s[\w]+'  # %B
                           r'\s[\d]{1,2}\,'  # %d,
                           r'\s[\d]{4}\s'  # %Y
                           r'[\d]{1,2}\:[\d]{1,2}\:[\d]{1,2}'  # HH:MM:SS
                           r'\s[\w]{2})').search(notification)  # AM/PM

    start_date = r'Start Date[\/]Time: (?P<start_date>[\w].*)'
    end_date = r'Expected End Date[\/]Time: (?P<end_date>[\w].*)'
    expected_end_date = r'Expected End Date[\/]Time: (?P<expected_end_date>[\w].*)'

    pattern = str([category, incident_number, start_date, end_date,
                   expected_end_date, sent_date, carriers_affected,
                   customer_impact, content])

    result = re.compile(pattern, flags=0)
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
        try:
            attachment = attachment.readlines()
            carriers_affected = [carrier.strip() for carrier in attachment]
        except ValueError as e:
            print(e.message)
