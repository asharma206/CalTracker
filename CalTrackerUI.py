from CalTrackerFacade import CalTrackerFacade

# UI class the user interacts with through the facade object
class CalTrackerUI:
    def __init__(self) -> None:
        self.facade = CalTrackerFacade()
        
# This method is called to start the application and displays the menu options to the user
# Related facade method is called based on the user entered option      
    def run(self):
        print("Welcome to CalTracker Application!")
        flag = True
        while(flag):
            userInput = input("""Please choose one of the options below:
1. Log a food entry
2. Get total calories for today
3. Get consumption history for a previous day
4. Exit the application
Option: """)   
            if(userInput=='1'):
                foodInput = input("Please enter food name along with portion size(ex: 1 bowl rice): ")
                self.facade.logFood(foodInput)
            elif(userInput=='2'):
                self.facade.getTotalCalories()
            elif(userInput=='3'):
                date = input("Enter the date you would like the consumption history for in format YYYY-MM-DD: ")
                self.facade.getConsumptionHistory(date)
            elif(userInput=='4'):
                print("Exiting application")
                flag = False
            else:
                print("Please enter a valid input")
        
# Call the run method for the UI        
CalTrackerUI().run()        