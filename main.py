#main.py
from mySignals import myHandler
from myTransform import myTransform
from myUDPClient import myUDPClient
import socket
import time
import threading
import signal  
import time

# UDP Client
ip = "127.0.0.1"
port = 10000
myClient = myUDPClient(ip, port)
refresh_time = 30

f = open('config.txt')
lines = f.readline().split()
input_stream = lines[0]#'csv_test.csv'



class myJob (threading.Thread):
    
    threadLock = threading.Lock()

    def __init__(self, name, timer):
        super().__init__()  #myThread.__init__(self)
        self.name = name
        self.timer = timer
        self.shutdown_flag = threading.Event()

    def run(self):
        print ("Comienza thread:"+self.name)
        try:
            while not self.shutdown_flag.is_set():
                myJob.threadLock.acquire()
                # csv to json
                ETL = myTransform (input_stream)
                output_stream = ETL.csv2json()
                # send message
                myClient.sendto(output_stream)
                myJob.threadLock.release()
                # status
                print ("%s: running every %d seconds: %s" % (self.name, self.timer,time.ctime(time.time())))
                self.shutdown_flag.wait(self.timer)

        except Exception:
            self.shutdown_flag.set()
        

        print ("Exit:"+self.name)



def main():

    print("Starting main program")

    signal.signal(signal.SIGINT, myHandler)
    
    try:
        j1 = myJob("Thread", refresh_time)
        j1.start()

        while True:
            time.sleep(0.5)

    except Exception:
        print('Exit: Main')
        myClient.close()
        j1.shutdown_flag.set()
        j1.join()

 
if __name__ == '__main__':
    main()

