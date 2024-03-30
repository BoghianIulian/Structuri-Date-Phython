from repository.car_repo import CarRepository
from domeniu.car import Car


class CarService:
    def __init__(self, carRepository: CarRepository):
        self.__carRepository = carRepository

    def addCar(self, marca, model, token, pretAchizitie, pretVanzare):
        car = Car(marca, model, token, pretAchizitie, pretVanzare)
        self.__carRepository.add(car)

    def get_all(self):
        lista = self.__carRepository.get_all()
        return lista

    def find_by_id(self, token):
        return self.__carRepository.get_by_id(token)

    def criteriu(self, elem, masina):
        if elem == "marca":
            return self.__carRepository.get_marca(masina)
        elif elem == "model":
            return self.__carRepository.get_model(masina)
        elif elem == "pret achizitie":
            return self.__carRepository.get_pretAchizitie(masina)
        elif elem == "pret vanzare":
            return self.__carRepository.get_pretVanzare(masina)
        elif elem == "token":
            return self.__carRepository.get_token(masina)
        elif elem == "profit":
            return int(self.__carRepository.get_pretVanzare(masina)) - int(
                self.__carRepository.get_pretAchizitie(masina))

    def sequential_search(self, list, criteriu_cautare, val_criteriu):
        for i in list:
            if self.criteriu(criteriu_cautare, i) == val_criteriu:
                return i

        return -1

    def comparator(self, a, b):
        if a > b:
            return True
        return False

    def binary_search(self, lst, criteriu_cautare, val_criteriu):
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.comparator(self.criteriu(criteriu_cautare, lst[mid]), val_criteriu):
                right = mid - 1
            elif self.comparator(val_criteriu, self.criteriu(criteriu_cautare, lst[mid])):
                left = mid + 1

            else:
                return mid
        return -1

    def selection_sort(self, lst, criteriu_sortare):
        n = len(lst)
        for i in range(n):
            # Găsește elementul minim în lista nesortată
            min_index = i
            for j in range(i, n):
                if self.criteriu(criteriu_sortare, lst[j]) < self.criteriu(criteriu_sortare, lst[min_index]):
                    min_index = j
            # Schimbă poziția elementului minim cu primul element din lista nesortată
            lst[i], lst[min_index] = lst[min_index], lst[i]

        return lst

    def selection_sort_new(self, lst, lista_criterii):
        n = len(lst)
        n2 = len(lista_criterii)
        k = 0
        for i in range(n):
            # Găsește elementul minim în lista nesortată
            min_index = i
            for j in range(i, n):
                while k < n2:
                    if self.criteriu(lista_criterii[k], lst[j]) < self.criteriu(lista_criterii[k], lst[min_index]):
                        min_index = j
                    elif self.criteriu(lista_criterii[k], lst[j]) < self.criteriu(lista_criterii[k], lst[min_index]):
                        k = k + 1

                # Schimbă poziția elementului minim cu primul element din lista nesortată
                lst[i], lst[min_index] = lst[min_index], lst[i]

        return lst

    def selection_sort3(self, lst, criteriu_sortare1, criteriu_sortare2, criteriu_sortare3):
        n = len(lst)
        for i in range(n):
            min_index = i
            for j in range(i, n):
                if self.criteriu(criteriu_sortare1, lst[j]) < self.criteriu(criteriu_sortare1, lst[min_index]):
                    min_index = j
                elif self.criteriu(criteriu_sortare1, lst[j]) == self.criteriu(criteriu_sortare1, lst[min_index]):
                    if self.criteriu(criteriu_sortare2, lst[j]) < self.criteriu(criteriu_sortare2, lst[min_index]):
                        min_index = j
                    elif self.criteriu(criteriu_sortare2, lst[j]) == self.criteriu(criteriu_sortare2, lst[min_index]):
                        if self.criteriu(criteriu_sortare3, lst[j]) < self.criteriu(criteriu_sortare3, lst[min_index]):
                            min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst

    def selection_sort2(self, lst, criteriu_sortare1, criteriu_sortare2):
        n = len(lst)
        for i in range(n):
            min_index = i
            for j in range(i, n):
                if self.criteriu(criteriu_sortare1, lst[j]) < self.criteriu(criteriu_sortare1, lst[min_index]):
                    min_index = j
                elif self.criteriu(criteriu_sortare1, lst[j]) == self.criteriu(criteriu_sortare1, lst[min_index]):
                    if self.criteriu(criteriu_sortare2, lst[j]) < self.criteriu(criteriu_sortare2, lst[min_index]):
                        min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst

    def partition1(self, array, low, high, criteriu_sortare):
        # choose the rightmost element as pivot
        pivot = array[high]
        # pointer for greater element
        i = low - 1
        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if self.criteriu(criteriu_sortare, array[j]) <= self.criteriu(criteriu_sortare, pivot):
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])
        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        # Return the position from where partition is done
        return i + 1

    # function to perform quicksort
    def quickSort(self, array, low, high, criteriu_sortare):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition1(array, low, high, criteriu_sortare)
            # Recursive call on the left of pivot
            self.quickSort(array, low, pi - 1, criteriu_sortare)
            # Recursive call on the right of pivot
            self.quickSort(array, pi + 1, high, criteriu_sortare)

    def partition3(self, array, low, high, criteriu_sortare1, criteriu_sortare2, criteriu_sortare3):
        # choose the rightmost element as pivot
        pivot = array[high]
        # pointer for greater element
        i = low - 1
        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if self.criteriu(criteriu_sortare1, array[j]) < self.criteriu(criteriu_sortare1, pivot):
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
            elif self.criteriu(criteriu_sortare1, array[j]) == self.criteriu(criteriu_sortare1, pivot):
                if self.criteriu(criteriu_sortare2, array[j]) < self.criteriu(criteriu_sortare2, pivot):
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
                elif self.criteriu(criteriu_sortare2, array[j]) == self.criteriu(criteriu_sortare2, pivot):
                    if self.criteriu(criteriu_sortare3, array[j]) < self.criteriu(criteriu_sortare3, pivot):
                        i = i + 1
                        (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        # Return the position from where partition is done
        return i + 1

    def partition2(self, array, low, high, criteriu_sortare1, criteriu_sortare2):
        # choose the rightmost element as pivot
        pivot = array[high]
        # pointer for greater element
        i = low - 1
        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if self.criteriu(criteriu_sortare1, array[j]) < self.criteriu(criteriu_sortare1, pivot):
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
            elif self.criteriu(criteriu_sortare1, array[j]) == self.criteriu(criteriu_sortare1, pivot):
                if self.criteriu(criteriu_sortare2, array[j]) < self.criteriu(criteriu_sortare2, pivot):
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        # Return the position from where partition is done
        return i + 1

    def quickSort3(self, array, low, high, criteriu_sortare1, criteriu_sortare2, criteriu_sortare3):
        if low < high:
            pi = self.partition3(array, low, high, criteriu_sortare1, criteriu_sortare2, criteriu_sortare3)
            self.quickSort3(array, low, pi - 1, criteriu_sortare1, criteriu_sortare2, criteriu_sortare3)
            self.quickSort3(array, pi + 1, high, criteriu_sortare1, criteriu_sortare2, criteriu_sortare3)

    def quickSort2(self, array, low, high, criteriu_sortare1, criteriu_sortare2):
        if low < high:
            pi = self.partition2(array, low, high, criteriu_sortare1, criteriu_sortare2)
            self.quickSort2(array, low, pi - 1, criteriu_sortare1, criteriu_sortare2)
            self.quickSort2(array, pi + 1, high, criteriu_sortare1, criteriu_sortare2)
