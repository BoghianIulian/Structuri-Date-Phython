import timeit


class Console:
    def __init__(self, car_service):
        self.__car_service = car_service

    def add_car(self):
        try:
            marca = input("Marca:")
            model = input("Model:")
            token = input("Token:")
            pretAchizitie = int(input("Pret Achizitie:"))
            pretVanzare = int(input("Pret vanzare:"))
            self.__car_service.addCar(marca, model, token, pretAchizitie, pretVanzare)
        except KeyError as ke:
            print(ke)

    def print_cars(self, cars):
        for car in cars:
            print(car)

    def numar_criterii(self, nr_criterii,lista):
        i = 0
        while i < nr_criterii:
            criteriu = input("Alegeti criteriu")
            lista[i] = criteriu
            i = i + 1
        return lista

    def sequential_search(self):
        cars = self.__car_service.get_all()
        token = input("Choose argument: ")
        val_token = input("Choose argument value: ")
        starttime = timeit.default_timer()
        rezultat = self.__car_service.sequential_search(cars, token, val_token)
        print("Time for this function is: ", timeit.default_timer() - starttime)
        return rezultat

    def selection_sort(self, cars, token):
        rezultat = self.__car_service.selection_sort(cars, token)
        return rezultat

    def selection_sort_new(self, cars, lista_criterii):
        rezultat = self.__car_service.selection_sort_new(cars, lista_criterii)
        return rezultat

    def selection_sort2(self, cars, token1, token2):
        rezultat = self.__car_service.selection_sort2(cars, token1, token2)
        return rezultat

    def selection_sort3(self, cars, token1, token2, token3):
        rezultat = self.__car_service.selection_sort3(cars, token1, token2, token3)
        return rezultat

    def binary_search(self, cars, token, val_token):
        lista = self.selection_sort(cars, token)
        rezultat = self.__car_service.binary_search(lista, token, val_token)
        return cars[rezultat]

    def quickSort(self, cars, token):
        low = 0
        high = len(cars) - 1
        self.__car_service.quickSort(cars, low, high, token)
        return cars

    def quickSort2(self, cars, token1, token2):
        low = 0
        high = len(cars) - 1
        self.__car_service.quickSort2(cars, low, high, token1, token2)
        return cars

    def quickSort3(self, cars, token1, token2, token3):
        low = 0
        high = len(cars) - 1
        self.__car_service.quickSort3(cars, low, high, token1, token2, token3)
        return cars

    def menu(self):
        print("1. Add car")
        print("2. Print cars")
        print("3. Find car by argument")
        print("4. Find car by argument-binary")
        print("5. Sort cars using selection-sort")
        print("6. Sort cars using quick-sort")
        print("7. Sort cars by profit")
        print("8.Sort cars selection sort-one function")
        print("x. Close program")

    def printcar(self):
        self.print_cars(self.__car_service.get_all())

    def run_menu(self):
        while True:
            self.menu()
            cmd = input("Choose: ")
            if cmd == "1":
                self.add_car()
            elif cmd == "2":
                execution_time = timeit.timeit(self.printcar, number=1)
                print(f"Durata de executie {execution_time / 1} secunde")
                # self.print_cars(self.__car_service.get_all())
            elif cmd == "3":
                pass
                # execution_time = timeit.timeit(self.sequential_search, number=1)
                # print(f"Durata de executie {execution_time / 1} secunde")
                print(self.sequential_search())
            elif cmd == "5":
                nr_crt = input("Number of sorting criterias: ")
                if nr_crt == "1":
                    token = input("Choose argument: ")
                    starttime = timeit.default_timer()
                    rezultat = self.selection_sort(self.__car_service.get_all(), token)
                    print("Time for this function is:", timeit.default_timer() - starttime)
                    for i in rezultat:
                        print(i)
                if nr_crt == "2":
                    token1 = input("Choose first argument:")
                    token2 = input("Choose second argument:")
                    starttime = timeit.default_timer()
                    rezultat = self.selection_sort2(self.__car_service.get_all(), token1, token2)
                    print("Time for this function is:", timeit.default_timer() - starttime)
                    for i in rezultat:
                        print(i)
                if nr_crt == "3":
                    token1 = input("Choose first argument: ")
                    token2 = input("Choose second argument: ")
                    token3 = input("Choose third argument: ")
                    starttime = timeit.default_timer()
                    rezultat = self.selection_sort3(self.__car_service.get_all(), token1, token2, token3)
                    print("Time for this function is:", timeit.default_timer() - starttime)
                    for i in rezultat:
                        print(i)

            elif cmd == "4":
                token = input("Choose argument: ")
                val_token = input("Choose argument value: ")
                starttime = timeit.default_timer()
                print(self.binary_search(self.__car_service.get_all(), token, val_token))
                print("Time for this function is:", timeit.default_timer() - starttime)
            elif cmd == "6":
                nr_crt = input("Number of sorting criterias: ")
                if nr_crt == "1":
                    token = input("Choose argument: ")
                    starttime = timeit.default_timer()
                    rezultat = self.quickSort(self.__car_service.get_all(), token)
                    print("Time for this function is:", timeit.default_timer() - starttime)
                    for i in rezultat:
                        print(i)
                if nr_crt == "2":
                    token1 = input("Choose first argument: ")
                    token2 = input("Choose second argument: ")
                    starttime = timeit.default_timer()
                    rezultat = self.quickSort2(self.__car_service.get_all(), token1, token2)
                    print("Time for this function is:", timeit.default_timer() - starttime)
                    for i in rezultat:
                        print(i)
                if nr_crt == "3":
                    token1 = input("Choose first argument: ")
                    token2 = input("Choose second argument: ")
                    token3 = input("Choose third argument: ")
                    starttime = timeit.default_timer()
                    rezultat = self.quickSort3(self.__car_service.get_all(), token1, token2, token3)
                    print("Time for this function is:", timeit.default_timer() - starttime)
                    for i in rezultat:
                        print(i)
            elif cmd == "7":
                starttime = timeit.default_timer()
                rezultat = self.selection_sort(self.__car_service.get_all(), "profit")
                print("Time for this function is:", timeit.default_timer() - starttime)
                for i in rezultat:
                    print(i)
            elif cmd == "8":
                lista = []
                nr_criterii = int(input("Alegeti numar criterii:"))
                lista = self.numar_criterii(nr_criterii,lista)
                rezultat = self.selection_sort_new(self.__car_service.get_all(), lista)
                for i in rezultat:
                    print(i)


            elif cmd == "x":
                break
            else:
                print("Choose a valid command")
