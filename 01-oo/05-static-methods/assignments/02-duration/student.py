class Duration:
    def __init__(self, *, seconds):
        self.__seconds = seconds
        self.__minutes = seconds / 60
        self.__hours = seconds / 3600

    @property
    def seconds(self):
        return self.__seconds
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def hours(self):
        return self.__hours
    
    @staticmethod
    def from_seconds(amount):
        return Duration(seconds=amount)
    
    @staticmethod
    def from_minutes(amount):
        return Duration(seconds=amount*60)
    
    @staticmethod
    def from_hours(amount):
        return Duration(seconds=amount*3600)
    
duration = Duration.from_hours(1)
print(duration.seconds)