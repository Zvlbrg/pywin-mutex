import win32event
import win32security
import time

import pywintypes
acl = pywintypes.ACL()
ace = acl.GetAce(0)
sec_attrs = pywintypes.SECURITY_ATTRIBUTES()
sec_attrs.SECURITY_DESCRIPTOR.Initialize()
sec_attrs.SECURITY_DESCRIPTOR.SetSecurityDescriptorDacl(False, None, False)
mutex = win32event.CreateMutex(sec_attrs, False, "Mutex1234")

def test():
    mut1 = win32event.OpenMutex(-1, False, "Mutex1234")
    win32event.WaitForSingleObject(mut1.handle, 20)
    with open(r"C:\Users\Marius\Desktop\Neues Textdokument.txt", "w") as f:
        f.write("Prozess1")
    time.sleep(30)
    win32event.ReleaseMutex(mutex)
    
test()
