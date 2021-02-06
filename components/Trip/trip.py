class Trip:
    def __init__(self,
        tripType,
        vehicle,
        src, 
        dst,
        depTime,
        arrTime,
        seats,
        basePrice,
        seatExtraCharge,
        agency
    ):
        self.type = tripType
        self.vehicle = vehicle
        self.source = src
        self.destination = dst
        self.departure_time = depTime
        self.arrival_time = arrTime
        self.seats = seats
        self.base_price = basePrice
        self.seat_extra_charge = seatExtraCharge
        self.agency = agency

    def setTripType(self, tripType):
        self.type = tripType
    def getTripType(self):
        return self.type
    
    def setVehicle(self, vehicle):
        self.vehicle = vehicle
    def getVehicle(self):
        return self.vehicle
    
    def setSource(self, src):
        self.source = src
    def getSource(self):
        return self.source

    def setDestination(self, dst):
        self.destination = dst
    def getDestination(self):
        return self.destination

    def setDepartureTime(self, depTime):
        self.departure_time = depTime
    def getDepartureTime(self):
        return self.departure_time
    
    def setArrivalTime(self, arrTime):
        self.arrival_time = arrTime
    def getArrivalTime(self):
        return self.arrival_time

    def setSeats(self, seats):
        self.seats = seats
    def getSeats(self):
        return self.seats

    def setBasePrice(self, basePrice):
        self.base_price = basePrice
    def getBasePrice(self):
        return self.base_price
    
    def setSeatsExtraCharges(self, mapSeatPrice):
        self.seat_extra_charge = mapSeatPrice
    def getSeatsExtraCharges(self):
        return self.seat_extra_charge
    def setSeatExtraCharge(self, seat, extraPrice):
        self.seat_extra_charge[seat] = extraPrice
    def getSeatExtraCharge(self, seat):
        return self.seat_extra_charge[seat]

    def setAgency(self, agency):
        self.agency = agency
    def getAgency(self):
        return self.agency