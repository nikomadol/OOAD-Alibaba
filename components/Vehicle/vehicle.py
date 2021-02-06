class Vehicle():
    def __init__(
        self,
        manufacturer,
        model,
        build_year,
        capacity,
    ):
        self.manufacturer = manufacturer
        self.model = model
        self.build_year = build_year
        self.capacity = capacity

    def setManufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    def getManufacturer(self):
        return self.manufacturer
    
    def setModel(self, model):
        self.model = model
    def getModel(self):
        return self.model

    def setBuildYear(self, year):
        self.build_year = year
    def getBuildYear(self):
        return self.build_year
    
    def setCapacity(self, capacity):
        self.capacity = capacity
    def getCapacity(self) -> int:
        return self.capacity
