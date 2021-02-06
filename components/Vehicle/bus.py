from vehicle import Vehicle
class Bus(Vehicle):
    def __init__(
        self,
        manufacturer,
        model,
        build_year,
        capacity,
        bus_id,
        bus_type
    ):
        super().__init__(manufacturer, model, build_year, capacity)
        self.bus_id = bus_id
        self.type = bus_type

    def setBusID(self, bus_id):
        self.bus_id = bus_id
    def getBusID(self):
        return self.bus_id
    
    def setType(self, bus_type):
        self.type = bus_type
    def getType(self):
        return self.type