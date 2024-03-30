from domeniu.car import Car
from repository.car_repo import CarRepository


class FileCarRepository(CarRepository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def add(self, car):
        super().add(car)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                marca = line.split()[0]
                model = line.split()[1]
                token = line.split()[2]
                pretAchizitie = line.split()[3]
                pretVanzare = line.split()[4]
                car = Car(marca, model, token, pretAchizitie, pretVanzare)
                self._cars[token] = car

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for car in self.get_all():
                f.write(f'{car.get_marca()} {car.get_model()} {car.get_token()} {car.get_pretAchizitie()} {car.get_pretVanzare()}\n')
