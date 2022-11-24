#make a Aircraft
class Aircraft:
    def __init__(self, make, code, type, flight_range) -> None:
        self.make = make
        self.code = code
        self.type = type
        self.flight_range = float (flight_range)
    #now make this 
    def get_make(self):
        return self.make
    def get_flight_range(self):
        return self.flight_range
    #show the data 
    def __repr__(self) -> str:
        return f"Aircraft make: {self.make}, code:{self.code}, type: {self.type}, flight_range: {self.flight_range}"
    