http://stackoverflow.com/questions/10156795/microsoft-outlook-create-rule-run-application-script-python/10539111#10539111

import win32com.client
import pythoncom
import re

class Handler_Class(object):
    def OnNewMailEx(self, receivedItemsIDs):
        # RecrivedItemIDs is a collection of mail IDs separated by a ",".
        # You know, sometimes more than 1 mail is received at the same moment.
        for ID in receivedItemsIDs.split(","):
            mail = outlook.Session.GetItemFromID(ID)
            subject = mail.Subject
            try:
                # Taking all the "BLAHBLAH" which is enclosed by two "%".
                command = re.search(r"%(.*?)%", subject).group(1)

                print command # Or whatever code you wish to execute.
            except:
                pass


outlook = win32com.client.DispatchWithEvents("Outlook.Application",
Handler_Class)

# new comment
#and then an infinite loop that waits from events.
pythoncom.PumpMessages()