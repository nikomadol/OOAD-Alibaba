from .vehicle import Vehicle
class Plain(Vehicle):
    def __init__(
        self,
        plane_id,
        manufacturer,
        model,
        build_year,
        capacity
    ):
        super().__init__(
            manufacturer,
            model,
            build_year,
            capacity
        )
        self.plane_id = plane_id
    def getID(self):
        return self.plane_id
