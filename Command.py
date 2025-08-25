from abc import ABC, abstractmethod

# Abstract command class
class Command(ABC):
    def __init__(self, dbInstance) -> None:
        self.dbInstance = dbInstance
    @abstractmethod
    def execute(self):
        pass
    
# Command class to log food into database    
class logFoodCommand(Command):
    def __init__(self, dbInstance, food, calories) -> None:
        super().__init__(dbInstance)
        self.food = food
        self.calories = calories
        
    def execute(self):
        self.dbInstance.logFood(self.food,self.calories)
        print(f"{self.food} logged for today. Calories: {self.calories}")
        
# Command class to get total calories        
class getTotalCaloriesCommand(Command):
    def __init__(self, dbInstance) -> None:
        super().__init__(dbInstance)
        
    def execute(self):
        total = self.dbInstance.getTotalCalories()
        print(f"You have consumed {total} calories for today.")
        
# Command class to get the consumption history for a particular date and print it        
class getConsumptionHistoryCommand(Command):
    def __init__(self, dbInstance, date) -> None:
        super().__init__(dbInstance)   
        self.date = date
    
    def execute(self):
        total = 0
        Data = self.dbInstance.getConsumptionHistory(self.date)  
        print(f"Printing consumption history for {self.date}: ")
        for row in Data:
            foodName = row[1]
            calories = row[2]
            total = total + calories
            print(f"You ate {foodName} which was {calories} calories")                 
        print(f"Total calories consumed on {self.date} are {total}")    
        
        