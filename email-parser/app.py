#!/usr/bin/python
import re
from datetime import datetime

# TODO: create email reader
"""EmailReader
Takes unread Outlook emails from specified folder
Opens the email and reads into an object.
"""
with open('/Users/david/dev/test/notification.txt', 'r') as f:
    notification = f.read()

"""Retrieving affected operators
If there is an attachment, the affected operators are stored in here line bu line.
If there is not attachment and the "Affected Operators:" regex is found it will either say
"See Attached List"
or
Have them listed in the regex
If neither is present they might be listed in the body. Should search the body against
a known list of operators.
"""
# TODO: refactoring 'DRY' calling compile and search each time, could use named groups
# TODO: properties feels like a getter/setter pattern and might need to use properties in a notification class
# patterns = re.findall(r'(?P<category>Category: ([\w].*))') #
# patterns = {"category" = "...", "named"}
# patterns.search(notification)

category = re.compile(r'Category: ([\w].*)').search(notification)
print(category.group(1))

incident_number = re.compile(r': (INC[\d]{12})').search(notification)
print(incident_number.group(1))

"""Get the content of the body between the new lines of incident number and customer impact
"""
content = re.compile(r'INC[\d]*\n\n(.*)Customer Impact:', re.DOTALL).search(notification)
print(re.sub(r'Super Secret Provider', r'Our SMS Provider', content.group(1).strip()))

customer_impact = re.compile(r'Customer Impact: ([\w].*)').search(notification)
print(customer_impact.group(1))

# TODO: get carriers affected
carriers_affected = re.compile(r'Carriers Affected: ([\w].*)').search(notification)
print(carriers_affected.group(1))

"""
Takes the the email header sent date.
'Sent: Tuesday, January 31, 2017 3:42:34 PM (UTC-06:00) Central Time (US & Canada)'
Strips the string and formats it (%b %d %Y %I:%M%p).
The database will convert to UTC upon INSERT.

First, parse the string into a naive datetime object.
This is an instance of datetime.datetime with no attached timezone information.
See documentation for datetime.strptime for information on parsing the date string.

Use the pytz module, which comes with a full list of time zones + UTC.
Figure out what the local timezone is, construct a timezone object from it,
and manipulate and attach it to the naive datetime.

Finally, use datetime.astimezone() method to convert the datetime to UTC.

Source code, using local timezone "America/Los_Angeles", for the string "2001-2-3 10:11:12":

# import pytz, datetime
# local = pytz.timezone ("America/Los_Angeles")
# naive = datetime.datetime.strptime ("2001-2-3 10:11:12", "%Y-%m-%d %H:%M:%S")
# local_dt = local.localize(naive, is_dst=None)
# utc_dt = local_dt.astimezone (pytz.utc)

From there, you can use the strftime() method to format the UTC datetime as needed:
utc_dt.strftime ("%Y-%m-%d %H:%M:%S")
"""
# Sent: 'Sent: Tuesday, January 31, 2017 3:42:34 PM (UTC-06:00) Central Time (US & Canada)'
rfc_1123 = "%A, %B %d, %Y %H:%M:%S %p"
iso_8601 = "%Y-%m-%dT%H:%M:%S"
# TODO: fix notification date and string date parsing
sent_date = re.compile(r'Sent: ([\w]+\,'                    # %A,
                       r'\s[\w]+'                           # %B
                       r'\s[\d]{1,2}\,'                     # %d,
                       r'\s[\d]{4}\s'                       # %Y
                       r'[\d]{1,2}\:[\d]{1,2}\:[\d]{1,2}'   # HH:MM:SS
                       r'\s[\w]{2})').search(notification)  # AM/PM

# print(type(sent_date))
# sent_date_obj = datetime.strptime(sent_date, rfc_1123).tzinfo('CST')
# notification_date = sent_date_obj.strftime(iso_8601).tzinfo('UTC')

if sent_date:
    print(sent_date.group(1))
else:
    print("TBD")

start_date = re.compile(r'Start Date[\/]Time: ([\w].*)').search(notification)
if start_date:
    print(start_date.group(1))
else:
    print("TBD")

end_date = re.compile(r'Expected End Date[\/]Time: ([\w].*)').search(notification)
if end_date:
    print(end_date.group(1))
else:
    print("TBD")

expected_end_date = re.compile(r'Expected End Date[\/]Time: ([\w].*)').search(notification)
if expected_end_date:
    print(expected_end_date.group(1))
else:
    print("TBD")
