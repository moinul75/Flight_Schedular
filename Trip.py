#make a trip 
class Trip:
    def __init__(self, trip_cities,aircraft, cost, start_date, route):
        self.trip_cities = trip_cities
        self.start_date = start_date
        self.aircraft = aircraft
        self.trip_route = route
        self.cost = cost
    def __repr__(self) -> str:
        return f"Trip: {self.trip_cities},  Cost: {self.cost}"
    
        
        