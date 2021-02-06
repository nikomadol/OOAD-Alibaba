from .seat import Seat
class TrainSeat(Seat):
    def __init__(self,
        seatNumber,
        properties,
        status,
        wagonNumber,
        coupeNumber
    ):
        super().__init__(seatNumber, properties, status)
        self.wagon_number = wagonNumber
        self.coupe_number = coupeNumber
    
    def setWagonNumber(self, wagonNumber):
        self.wagon_number = wagonNumber
    def getWagonNumber(self):
        return self.wagon_number

    def setCoupeNumber(self, coupeNumber):
        self.coupe_number = coupeNumber
    def getCoupeNumber(self):
        return self.coupe_number