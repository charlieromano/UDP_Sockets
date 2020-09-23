#main.py
from mySignals import handler
from myThreads import MyThread
import signal


signal.signal(signal.SIGINT, myHandler)


thread1 = myThread("Thread-1", 10)
thread1.start()
thread1.join()
