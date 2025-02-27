# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, value):
        if isinstance(value, int) and 0 <= value <= 23:
            self.__hours = value
        else:
            raise ValueError("Hours must be from an 24-hour-clock integer")


    @property
    def minutes(self):
        return self.__minutes
        
    @minutes.setter
    def minutes(self, value):
        if isinstance(value, int) and 0 <= value <= 59:
            self.__minutes = value
        else:
            raise ValueError("Minutes must be from an 24-hour-clock integer")
    
    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, value):
        if isinstance(value, int) and 0 <= value <= 59:
            self.__seconds = value
        else:
            raise ValueError("Seconds must be from an 24-hour-clock integer")