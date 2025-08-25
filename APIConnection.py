from py_edamam import Edamam
class APIConnection:
    __instance = None
    # Implement as Singleton
    def __new__(cls):

        if (cls.__instance is None):
            cls.__instance = super(APIConnection, cls).__new__(cls)

        return cls.__instance
    # create connection to Edamam API and assign to instance variable
    def __init__(self):
        self.__instance = Edamam(nutrition_appid='c12f232b',
           nutrition_appkey='539d8e19c8ac429b01c1ec653ffe830a',
           )
    # This function gets calories from the API based on the passed String    
    def getCalories(self,foodData):
        return self.__instance.search_nutrient(foodData)["calories"]