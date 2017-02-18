https://blog.matthewurch.ca/?p=236

import win32com.client
import pythoncom

class Handler_Class(object):
    def OnNewMailEx(self, receivedItemsIDs):
        for ID in receivedItemsIDs.split(","):
            # Microsoft.Office.Interop.Outlook _MailItem properties:
            # https://msdn.microsoft.com/en-us/library/microsoft.office.interop.outlook._mailitem_properties.aspx
            mailItem = outlook.Session.GetItemFromID(ID)
            print "Subj: " + mailItem.Subject
            print "Body: " + mailItem.Body.encode( 'ascii', 'ignore' )
            print "========"

outlook = win32com.client.DispatchWithEvents("Outlook.Application", Handler_Class)
pythoncom.PumpMessages()