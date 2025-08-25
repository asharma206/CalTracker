# CalTracker

CalTracker is a Python-based application that helps users track their **daily food intake** and monitor **calorie consumption**.  
By entering food items and portion sizes, the app retrieves calorie information using the **Edamam API** and stores data in a **SQLite Cloud database**.  

The project was developed as part of the **Software Architecture (SFWRTECH 4SA3)** course, following the **4+1 View Model** and applying key design patterns.

---

## Features
- Log daily food entries with portion size.  
- Retrieve calorie information for each food item (via Edamam API).  
- Automatically calculate total daily calorie intake.  
- Store entries in a SQLite Cloud database.  
- View consumption history by date.  
- Console-based menu system for interaction.  

---

## Tech Stack
- **Language:** Python  
- **Database:** SQLite Cloud  
- **API:** Edamam Nutrition API  
- **Architecture Patterns:**  
  - Singleton (Database + API connections)  
  - Command Pattern (Encapsulation of operations)  
  - Façade (Simplified interface for UI interactions)  

---

## Database Schema
**Food Entries Table**

| Column  | Type   | Purpose                          |
|---------|--------|----------------------------------|
| date    | TEXT   | Date the food was consumed       |
| name    | TEXT   | Name of the food                 |
| calories| REAL   | Calories for the food item       |

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/asharma206/CalTracker.git
   cd CalTracker
   ```
   
2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Replace Variables**

   Replace the YourAppId and YourAppKey variables in APIConnection file and SQLiteConnectionURL in DatabaseConnection file with your variables.

4. **Run the application**

   ```bash
   python CalTrackerUI.py
   ```
---

## Target Audience

- Health-conscious individuals

- Fitness enthusiasts

- Anyone interested in monitoring their nutrition and calorie intake
---

This project is for educational purposes.
You may modify and use it as needed.
