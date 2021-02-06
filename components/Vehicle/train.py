from .vehicle import Vehicle
class Train(Vehicle):
    def __init__(
        self,
        manufacturer,
        model,
        build_year,
        capacity,
        train_id,
        train_type,
        wagons_count,
        wagon_coupes_count,
        coupe_seats_count
    ):
        super().__init__(manufacturer, model, build_year, capacity)
        self.train_id = train_id
        self.train_type = train_type
        self.wagons_count = wagons_count
        self.wagon_coupes_count = wagon_coupes_count
        self.coupe_seats_count = coupe_seats_count

    def setTrainID(self, train_id):
        self.train_id = train_id
    def getTrainID(self):
        return self.train_id
    
    def setType(self, train_type):
        self.type = train_type
    def getType(self):
        return self.type
    
    def setWagonsCount(self, wagons_count):
        self.wagons_count = wagons_count
    def getWagonsCount(self):
        return self.wagons_count
    
    def setWagonCoupesCount(self, wagon_coupes_count):
        self.wagon_coupes_count = wagon_coupes_count
    def getWagonCoupesCount(self):
        return self.wagon_coupes_count

    def setCoupeSeatsCount(self, coupe_seats_count):
        self.coupe_seats_count = coupe_seats_count
    def getCoupeSeatsCount(self):
        return self.coupe_seats_count