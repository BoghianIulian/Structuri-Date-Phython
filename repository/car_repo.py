class CarRepository:
    def __init__(self):
        self._cars = {}

    def get_all(self):
        return list(self._cars.values())

    def get_by_id(self, id_car):
        if id_car in self._cars:
            return self._cars[id_car]
        return None

    def add(self, car):
        if self.get_by_id(car.get_token()) is not None:
            raise KeyError("The token is already used")
        self._cars[car.get_token()] = car

    def get_marca(self, car):
        return car.get_marca()

    def get_model(self, car):
        return car.get_model()

    def get_pretAchizitie(self, car):
        return car.get_pretAchizitie()

    def get_token(self, car):
        return car.get_token()

    def get_pretVanzare(self,car):
        return car.get_pretVanzare()
