from domeniu.entity import Entity

#DEFINIM CLASA MASINII
class Car(Entity):
    def __init__(self, marca, model, token, pretAchizitie, pretVanzare):
        super().__init__(token)
        self.__marca = marca
        self.__model = model
        self.__pretAchizitie = pretAchizitie
        self.__pretVanzare = pretVanzare

    #GETTER PENTRU MARCA
    def get_marca(self):
        return self.__marca

    #GETTER PENTRU MODEL
    def get_model(self):
        return self.__model

    #GETTER PENTRU PRETUL DE ACHIZITIE
    def get_pretAchizitie(self):
        return self.__pretAchizitie

    #GETTER PENTRU PRETUL DE VANZARE
    def get_pretVanzare(self):
        return self.__pretVanzare

    def __str__(self):
        return f"Marca:{self.__marca}, model:{self.__model}, token:{self.get_token()}, pretAchizitie:{self.__pretAchizitie}, pretVanzare:{self.__pretVanzare}"


