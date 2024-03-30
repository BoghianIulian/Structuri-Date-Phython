from repository.file_repo import FileCarRepository
from service.car_serv import CarService
from ui.console import Console

def main():

    fileCarRepository = FileCarRepository("car.txt")

    carService = CarService(fileCarRepository)

    console = Console(carService)

    console.run_menu()


main()
