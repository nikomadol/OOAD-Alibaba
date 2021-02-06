class Seat:
    def __init__(self, seatNumber, properties, status):
        self.seat_number = seatNumber
        self.properties = properties
        self.status = status
    
    def setSeatNumber(self, seatNumber):
        self.seat_number = seatNumber
    def getSeatNumber(self):
        return self.getSeatNumber
    
    def setProperties(self, properties):
        self.properties = properties
    def getProperties(self):
        return self.properties
    def addProperty(self, property, value):
        self.properties[property] = value
    def getProperty(self, key):
        return self.properties.get(key)

    def setStatus(self, status):
        self.status = status
    def getStatus(self):
        return self.status