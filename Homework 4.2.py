""". (Stopwatch) Design a class named StopWatch. The class contains: 
■ The private data fields startTime and endTime with get methods. 
■ A constructor that initializes startTime with the current time. 
■ A method named start() that resets the startTime to the current time. 
■ A method named stop() that sets the endTime to the current time.
 ■ A method named getElapsedTime() that returns the elapsed time for the stop watch in milliseconds.

 """

import datetime

class StopWatch(object):
    def __init__ (self):
        self.startTime = datetime.datetime.now()
        self.endTime = datetime.datetime.now()
        
    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def start(self):
        self.startTime = datetime.datetime.now()

    def stop(self):
        self.endTime = datetime.datetime.now()

    def getElapsedTime(self):
        return (self.endTime - self.startTime)

MyStopWatch = StopWatch()


MyStopWatch.start()
n=0
for i in range(1, 1000000):
    n = n + i
MyStopWatch.getStartTime()
MyStopWatch.stop()
MyStopWatch.getEndTime()
print (MyStopWatch.getElapsedTime())



    

    
