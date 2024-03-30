class Entity:
    def __init__(self, entityId):
        self.__entityId = entityId

    def get_token(self):
        return self.__entityId

    def set_token(self, entityId):
        self.__entityId = entityId