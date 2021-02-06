class Location:
    def __init__(self, country, city, terminal):
        self.country = country
        self.city = city
        self.terminal = terminal
    
    def setCountry(self, country):
        self.country = country
    def getCountry(self):
        return self.country

    def setCity(self, city):
        self.city = city
    def getCity(self):
        return self.city
    
    def setTerminal(self, terminal):
        self.terminal = terminal
    def getTerminal(self):
        return self.terminal