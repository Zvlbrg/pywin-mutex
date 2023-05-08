import mutex
import time
import os

with mutex.Mutex("Mutex1234"):
    print(f"{os.getpid()} Mutex acquired")
    time.sleep(30)
print(f"{os.getpid()} Mutex Released")
