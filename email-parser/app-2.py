import re

with open('/Users/david/dev/test/notification.txt', 'r') as f:
    notification = f.read()

category = r'Category: ([\w].*)'
notification_date = r'Sent: [\w][\s]([\w].*)'
start_date = r'Start Date[\/]Time: ([\w].*)'
end_date = r'Expected End Date[\/]Time: ([\w].*)'
expected_end_date = r'Expected End Date[\/]Time: ([\w].*)'
incident_number = r': (INC[\d]{12})'
content = "r'INC[\d]*\n\n(.*)Customer Impact:', re.DOTALL"
customer_impact = r'Customer Impact: ([\w].*)'

p = re.compile(category +
               notification_date +
               start_date +
               end_date +
               expected_end_date +
               incident_number +
               content +
               customer_impact)

r = p.search(notification)

if r:
    print("Category: {}".format(r.group(1)))
    print("Notification Date: {}".format(result.group(2)))
    print("Start Date: {}".format(result.group(3)))
    print("End Date: {}".format(result.group(4)))
    print("Expected End Date: {}".format(result.group(5)))
    print("Incident Number: {}".format(result.group(6)))
    print("Notification Date: {}".format(result.group(7)))
    print("Customer Impact: {}".format(result.group(8)))
