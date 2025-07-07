# 🚗 CAR RENTAL APP
A Python-based car rental management system using object-oriented programming. This program is designed to manage car inventory, rental operations, and total cost tracking efficiently.

# WHAT THE PROGRAM DOES
This app provides a menu-driven interface to perform the following:

✅ 1. Add a Car:
        
        1. Prompts the user to input car details (name, available quantity, rent cost, insurance costs).

        2. Creates a new Car object and stores it in memory.

        3. The car will also be saved to a file when the program ends.

✅ 2. Rent a Car:

        1. Displays a list of available cars with their prices and insurance costs.

        2. Validates user input for car selection, rental days, and insurance type.

        3. Calculates:

            - Rent = daily cost × number of days

            - Tax = 5% of rent

            - Insurance (liability or comprehensive)

            - Total cost = Rent + Insurance + Tax

        4. Updates inventory by decreasing the quantity.

        5. Updates and tracks total rent, insurance, and tax collected.

✅ 3. Return a Car:

        1. Allows the user to return a rented car by selecting from the list.

        2. Increments the quantity of that car in inventory.

✅ 4. Print the Totals:

        1. Displays the total rental revenue, total insurance collected, and total tax collected from all rentals made so far.

✅ 5. Delete a Car:

        1. Lets the user remove a car from the inventory by selecting from the list.

        2. Useful if the car is no longer offered.

✅ 6. Modify a Car:

        1. Enables modification of:

            - Available quantity

            - Daily rent cost

            - Liability insurance cost

            - Comprehensive insurance cost

        2. Ensures all updates are saved to the file when exiting.

✅ 0. Exit Program:

        1. Saves all current car data to a file (CarsData.txt) so that next time the program starts, data is preserved.

# 🧾 Class Details

    Car Class (in Car_Class.py): Represents each car with private attributes and provides setter/getter methods.

    1. Attributes:

        - Name

        - Available quantity

        - Daily rent cost

        - Liability insurance cost

        - Comprehensive insurance cost

    2. Methods:

        - get_ and set_ methods for each attribute

        - decrease_available_quantity() and increase_available_quantity()

        - __str__() for displaying car information

# 🧾 File Handling
All car data is read from and written to Files/CarsData.txt.
This allows data persistence between program runs.

- Functions:

    1. file_read() → Reads car data and loads into the app.

    2. file_write() → Saves all current cars back to file on exit.

# 🛡️ Input Validations

- The system validates:

    1. Menu options (must be between 0–6)

    2. Car number selections

    3. Insurance type (L, l, C, c)

    4. Confirmation prompts (Y, N)

    5. Input types (must be correct type: int/float)

# 🛠 How to Use

    1. Run Car_System_Main_App.py

    2. Follow the on-screen menu instructions

    3. Exit with option 0 to save all changes

# 📌 Notes
All modifications, rentals, and deletions are temporary until saved at exit.