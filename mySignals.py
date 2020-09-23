#!/usr/bin/python3
import signal  
import time
import traceback


def myHandler(sig, frame):  # define the handler  
    print("Signal Number:", sig, " Frame: ", frame)  
    traceback.print_stack(frame)
    raise Exception("Exit service")


  
#signal.signal(signal.SIGINT, handler)  # hacerlo en el thread ppal. El handler siempre se ejecuta en el thread ppal.
  

