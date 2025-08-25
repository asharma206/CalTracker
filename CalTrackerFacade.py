from APIConnection import APIConnection
from DatabaseConnection import DatabaseConnection
from Command import logFoodCommand,getTotalCaloriesCommand,getConsumptionHistoryCommand

# Facade class is used by the UI class to execute the related application functionality
# This facade class acts as an invoker for the Command pattern and calls the execute method
# for related Command class
class CalTrackerFacade:
    def __init__(self) -> None:
        self.dbInstance = DatabaseConnection()
        self.APIInstance = APIConnection()
        self.command = None
        
    def logFood(self, food):
        self.command = logFoodCommand(self.dbInstance,food, self.APIInstance.getCalories(food))
        self.command.execute()
        
    def getTotalCalories(self):
        self.command = getTotalCaloriesCommand(self.dbInstance)
        self.command.execute()
        
    def getConsumptionHistory(self,date):
        self.command = getConsumptionHistoryCommand(self.dbInstance,date)
        self.command.execute()        