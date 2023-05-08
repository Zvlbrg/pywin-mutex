import win32event
import win32con

class Mutex(object):

    def __init__(self, name: str, timeout: int=win32event.INFINITE):
        self._mutex = win32event.CreateMutex(None, False, name)
        self._name = name
        self._timeout = timeout
        self.is_aquired = False

    def acquire(self):
        if self.is_aquired:
            return
        win32event.WaitForSingleObject(self._mutex, self._timeout)
        win32event.OpenMutex(win32con.SYNCHRONIZE, False, self._name)
        self.is_aquired = True

    def release(self):
        if not self.is_aquired:
            return
        win32event.ReleaseMutex(self._mutex)
        self.is_aquired = False

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

if __name__ == "__main__":
    import time
    with Mutex("Mutex1234") as mutex:
        time.sleep(30)
