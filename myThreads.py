#!/usr/bin/python3

from threading import Thread
import time

class myThread (Thread):

    def __init__(self, name, timer):
        super().__init__()  #Thread.__init__(self)
        self.name = name
        self.timer = timer

    def run(self):
        print ("Comienza thread:"+self.name)
        while self.timer:
            time.sleep(self.timer)
            print ("%s: %s, se ejecuta cada %d segundos;" % (self.name, time.ctime(time.time()), self.timer))

        print ("Saliendo de:"+self.name)


    
# Creamos nuevos threads
#thread1 = MyThread("Thread-1", 10)

# Iniciamos threads y esperamos que terminen
#thread1.start()

#thread1.join()

