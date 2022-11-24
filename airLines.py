#make a airlines 
import csv
from AirCraft import Aircraft
class AirLines:
    def __init__(self):
        self.air_crafts = None
        self.load_air_crafts_data('./data/aircraft.csv')
    
    #now load data 
    def load_air_crafts_data(self, csv_file):
        #open the csv file and load the data 
        air_crafts = {}
        with open(csv_file, 'r') as file:
            lines = csv.reader(file)
            next(lines)
            for line in lines:
                air_crafts[line[0]] = Aircraft(line[3], line[0], line[1], line[4])
        file.close()
        self.air_crafts = air_crafts
        
        
    def get_aircraft(self, code):
        return self.air_crafts[code]
    def get_aircraft_by_distance(self, distance):
        for aircraft in self.air_crafts.values():
            if aircraft.flight_range < distance:
                return aircraft


sh = AirLines()
c = sh.get_aircraft('DC8')
# print(c)
    