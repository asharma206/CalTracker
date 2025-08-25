import sqlitecloud
from datetime import datetime

class DatabaseConnection:
    __instance = None
    
    # Implement as Singleton
    def __new__(cls):

        if (cls.__instance is None):
            cls.__instance = super(DatabaseConnection, cls).__new__(cls)

        return cls.__instance
    
    # Database connection
    def __init__(self):
        self.__instance = sqlitecloud.connect("SQLiteConnectionURL")
    
    # This function inserts data into the database(date, food name, calories)    
    def logFood(self,foodName, calories):
        c = self.__instance.cursor()
        date = datetime.today().strftime('%Y-%m-%d')
        c.execute("""INSERT INTO foodData(date, name, calories)
         VALUES(:date, :food, :calories)""",{'date': date,'food': foodName, 'calories': calories})
        
    # This function fetches all data in the database for the current date, totals the calorie field and returns it
    def getTotalCalories(self):
        c = self.__instance.cursor()
        total = 0
        dateToday = datetime.today().strftime('%Y-%m-%d')

        c.execute("SELECT * from foodData WHERE date=:todayDate",{'todayDate': dateToday})
        Data = c.fetchall()
        for row in Data:
            total = total + row[2]
        return total
    
    # This function fetches the entries in the database that match the passed date to the function and returns them        
    def getConsumptionHistory(self, date):
        c = self.__instance.cursor()
        c.execute("SELECT * from foodData WHERE date=:Date",{'Date': date})
        Data = c.fetchall()
        return Data
        
                     