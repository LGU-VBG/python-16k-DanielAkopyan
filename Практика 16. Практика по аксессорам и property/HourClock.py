class HourClock:
    def __init__(self, hours):
        if  isinstance(hours, int) and 1 <= hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')
    
    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, value):
        if not isinstance(value, int) or not 1 <= value <= 12:
            raise ValueError('Некорректное время')
        self._hours = value

try: 
    HourClock('pizza time 🕷') 
except ValueError as e: 
    print(e) 