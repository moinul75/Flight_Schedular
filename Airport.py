#make a airport 
class Airport:
    #name, latitude , logitute , country , rate
    def __init__(self,code,name,city, country, latitude , logitude,rate) -> None:
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.latitude = float(latitude)
        self.logitude = float(logitude)
        self.rate = float(rate)
    def __repr__(self) -> str:
        return f"Airport:{self.name}, in: {self.country}, Latitude:{self.latitude}, Longitude:{self.logitude}, Rate:{self.rate}"
    
        