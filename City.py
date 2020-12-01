class City:
    def __init__(self,cityName,country,airport,IATAcode,latitude1,longitude):
        self.cityName = cityName
        self.country = country
        self.airport = airport
        self.IATAcode = IATAcode
        self.latitude = latitude1
        self.longitude = longitude

    def printCoordinate(self):
        print(self.cityName+" : " + "(" + str(self.latitude) + ", " + str(self.longitude) + ")")
