class LengthConverter:
    def __init__(self, distance_in_m = 0):
        self.__distance_in_m = distance_in_m
        

    @property
    def distance_in_m(self):
        return self.__distance_in_m
    
    @property
    def meter(self):
        return self.__distance_in_m
    
    @meter.setter
    def meter(self, value):
        self.__distance_in_m = value

    @property
    def inch(self):
        return self.__distance_in_m / 0.0254
    
    @inch.setter
    def inch(self, value):
        self.__distance_in_m = value * 0.0254

    @property
    def feet(self):
        return self.__distance_in_m / 0.3048
    
    @feet.setter
    def feet(self, value):
        self.__distance_in_m = value * 0.3048