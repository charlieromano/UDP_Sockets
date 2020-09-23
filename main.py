#main.py
from mySignals import myHandler
from threading import Thread
from myTransform import myTransform
from myUDPClient import myUDPClient
import signal
import socket
import time

# UDP Client
ip = "127.0.0.1"
port = 10000
myClient = myUDPClient(ip, port)	

class myJob (Thread):

    def __init__(self, name, timer):
        super().__init__()  #myThread.__init__(self)
        self.name = name
        self.timer = timer

    def start(self):
        print ("Comienza thread:"+self.name)
        while self.timer:
            time.sleep(self.timer)
            # csv to json
            input_stream = 'csv_test.csv'
            ETL = myTransform (input_stream)
            myJob.threadLock.acquire()
            output_stream = ETL.csv2json()
            myJob.threadLock.release()
            # status
            print ("%s: %s, se ejecuta cada %d segundos;" % (self.name, time.ctime(time.time()), self.timer))
            

        print ("Exit:"+self.name)



def main():
    signal.signal(signal.SIGINT, myHandler)
    input_stream = 'csv_test.csv'
    print("Starting main program")
    
    try:

        while True:
            ETL = myTransform (input_stream)
            output_stream = ETL.csv2json()
            print ("Main:")
            myClient.sendto(output_stream)
            time.sleep(10)

    except:
    	pass

    print('Exiting main program')
 
 
if __name__ == '__main__':
    main()

  