class PassengersSeat:
    def __init__(self, trip, passengersSeat):
        self.trip = trip
        self.passengers_seat = passengersSeat

    def setTrip(self, trip):
        self.trip = trip
    def getTrip(self, trip):
        return self.trip

    def setPassengersSeat(self, passengersSeat):
        self.passengers_seat = passengersSeat
    def getPassengersSeat(self):
        return self.passengers_seat

    def setPassengerSeat(self, passenger, seat):
        self.passengers_seat[passenger] = seat
    def getPassengerSeat(self, passenger):
        return self.passengers_seat.get(passenger)
    def removePassenger(self, passenger):
        self.passengers_seat.pop(passenger, None)