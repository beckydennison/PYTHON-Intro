'''3. (The Time class) Design a class named Time. The class contains: 
■ The private data fields hour, minute, and second that represent a time. 
■ A constructor that constructs a Time object that initializes hour, minute, and second using the current time. 
■ The get methods for the data fields hour, minute, and second, respectively. 
■ A method named setTime(elapseTime) that sets a new time for the object using the elapsed time in seconds. For example, if the elapsed time is 555550 seconds, the hour is 10, the minute is 19, and the second is 12. 
'''
import datetime

class Time(object):

    def __init__ (self):
        now = datetime.datetime.now()
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second
        self.day = now.day
        self.year = now.year

    def gethour(self):
        return self.hour

    def getminute(self):
        return self.minute

    def getsecond(self):
        return self.second

    def setTime(self, elapseTime):
        self.second = int(elapseTime)
        self.minute, self.second = divmod(self.second, 60)
        self.hour, self.minute = divmod(self.minute, 60)
        self.day, self.hour =divmod(self.hour, 24)
        self.year, self.day =divmod(self.day, 365)

MyTime = Time()
print(MyTime.gethour(),":", MyTime.getminute(),":", MyTime.getsecond())
elapseTime = int(input("Please enter elapsed Time in Seconds:"))
MyTime.setTime(elapseTime)
print(MyTime.gethour(),":", MyTime.getminute(), ":", MyTime.getsecond())

    
