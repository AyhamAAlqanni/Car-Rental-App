
# Importing classes to main app file.
from Car_Class import Car

# A function that writes car's information to the file.
def file_write(cars_list):

    write_to_file = open("Files/CarsData.txt", "w")

    for car_object in cars_list:

        # Writing car object information to the file.
        write_to_file.write("Car Name:" + str(car_object.get_name()) + "\n")
        write_to_file.write("Available Quantity:" + str(car_object.get_quantity_available()) + "\n")
        write_to_file.write("Daily Rent Cost:" + str(car_object.get_daily_rent_cost()) + "\n")
        write_to_file.write("Liability Insurance Cost:" + str(car_object.get_liability_insurance_cost()) + "\n")
        write_to_file.write("Comprehensive Insurance Cost:" + str(car_object.get_comprehensive_insurance_cost()) + "\n")

    write_to_file.close()


# A function that reads car's information from the file.
def file_read():

    cars_list = []

    read_from_file = open("Files/CarsData.txt", "r")

    # Reading first line (Car Name).
    car_name = read_from_file.readline()

    # Stop reading when the empty line is reached.
    while car_name != "":

        car_name = car_name.rstrip("\n").split(":")
        car_name = car_name[1]

        # Reading second line (Car Available Quantity).
        car_quantity = read_from_file.readline().rstrip("\n").split(":")
        car_quantity = car_quantity[1]

        # Reading third line (Car Daily Cost).
        car_daily_cost = read_from_file.readline().rstrip("\n").split(":")
        car_daily_cost = car_daily_cost[1]

        # Reading fourth line (Car Liability Insurance Cost).
        car_liability_insurance_cost = read_from_file.readline().rstrip("\n").split(":")
        car_liability_insurance_cost = car_liability_insurance_cost[1]

        # Reading fifth line (Car Comprehensive Insurance Cost).
        car_comprehensive_insurance_cost = read_from_file.readline().rstrip("\n").split(":")
        car_comprehensive_insurance_cost = car_comprehensive_insurance_cost[1]

        # Creating a car object from the information collected from the file.
        car_object = Car(car_name, int(car_quantity), float(car_daily_cost), float(car_liability_insurance_cost), 
                         float(car_comprehensive_insurance_cost))
        
        # Adding car object to the list.
        cars_list.append(car_object)

        car_name = read_from_file.readline()

    read_from_file.close()

    # Returning car list.
    return cars_list


# A function that displays the menu.
def menu_display():

    # only 1, 2, 3, 4, 5 and 0 are accepted. If the users enters anything else, 
    # the system keeps asking the user to enter a valid option
    try:

        print("Please Select One:")
        print("\t1- Add Car.")
        print("\t2- Car Rental.")
        print("\t3- Car Return.")
        print("\t4- Print The Total.")
        print("\t5- Delete Car.")
        print("\t0- Exit Program.")

        user_input = int(input("Option Number: "))

        return user_input
    
    except ValueError:

        print("Invalid Input!")
        print("***************************************************************")

        return -1


# A function that creates a car object and returns it.
def add_car():

    try:

        car_name = input("Enter Car's Name: ")
        available_quantity = int(input("Enter Available Car Quantity: "))
        daily_rent_cost = float(input("Enter Daily Rent Cost: "))
        liability_cost = float(input("Enter Liability Insurance Cost: "))
        comprehensive_cost = float(input("Enter Comprehensive Insurance Cost: "))

        # Creating a car object from the information collected from the user.
        car_object = Car(car_name.capitalize(), available_quantity, daily_rent_cost, liability_cost, comprehensive_cost)

        return car_object
    
    except ValueError:

        print("RESULT: Wrong Input!\nCar Has Not Been Added.")


# A function that deals with car renting process.
def car_rent(cars_list):

    print("Select One of The Available Cars:")
    print("-------------------------------------------------------------------------------------------------------")
    print("Model", "\t\tAvailable", "\tPrice/Day", "\tLiability Insurance/Day", "\tComprehensive Insurance/Day")
    print("-------------------------------------------------------------------------------------------------------")

    # A variable that holds car listing number for the car list menu.
    car_number = 1

    # Displaying cars information.
    for car in cars_list:

        print(f"{car_number}. {car.get_name()}\t    {car.get_quantity_available()}\t\t  ${car.get_daily_rent_cost()}" + 
              f"\t\t${car.get_liability_insurance_cost()}\t\t\t${car.get_comprehensive_insurance_cost()}")
        
        car_number += 1

    # Making Sure that the user selection is between 1 and cars list length plus it is an integer.
    try:

        car_selection = int(input("Enter Car Number Selection: "))

        if car_selection > 0 and car_selection <= len(cars_list):

            rented_days = int(input("Enter How Many Days to Be Rented: "))
            insurance_type = input("Enter (L) For Liability Insurance, (C) For Comprehensive Insurance: ")

            renting_cost = cars_list[car_selection - 1].get_daily_rent_cost() * rented_days
            tax_cost = renting_cost * 0.05
            total_cost = renting_cost + tax_cost

            if insurance_type.upper() == "L":

                print(f"Insurance Type: Liability.\tCost: ${format(cars_list[car_selection - 1].get_liability_insurance_cost(), "0.2f")}")

                insurance_cost = cars_list[car_selection - 1].get_liability_insurance_cost()

            elif insurance_type.upper() == "C":

                print(f"Insurance Type: Comprehensive.\tCost: ${format(cars_list[car_selection - 1].get_comprehensive_insurance_cost(), "0.2f")}")

                insurance_cost = cars_list[car_selection - 1].get_comprehensive_insurance_cost()

            else:

                print("RESULT: Invalid Input!\nOnly The Letters “L”, “l”, “F”, and “f” Are Accepted.")

                # Returning 0 for total_cost, insurance_cost, tax_cost as a invalid input.
                return 0, 0, 0
            
            print(f"Renting Cost: ${format(renting_cost, "0.2f")}")
            print(f"Tax (5%): ${format(tax_cost, "0.2f")}")

            total_cost += insurance_cost

            print(f"Total: ${format(total_cost, "0.2f")}")

            renting_confirmation = input("Confirm Renting (Y) or (N): ")

            if renting_confirmation.upper() == "Y":

                cars_list[car_selection - 1].decrease_available_quantity()

                print("RESULT: Car Was Added To The Total Menu Option.")

                return total_cost, insurance_cost, tax_cost 
            
            else:

                print("RESULT: Car Has Not Been Rented.")

                # Returning 0 for total_cost, insurance_cost, tax_cost as a invalid input.
                return 0, 0, 0

        else:
                print("RESULT: Invalid Selection!\nEntered a Value Not in The List.")

                # Returning 0 for total_cost, insurance_cost, tax_cost as a invalid input.
                return 0, 0, 0

    except ValueError:

        print("RESULT: Wrong Input!\nEntered a Non Integer Value.")

        # Returning 0 for total_cost, insurance_cost, tax_cost as a invalid input.
        return 0, 0, 0


# A function that deals with car returing process.
def car_return(cars_list):

    # A variable that holds car listing number for the car list menu.
    car_number = 1

    # Displaying cars in the list.
    for car in cars_list:

        print(f"{car_number}. {car.get_name()}")
        
        car_number += 1

    try:

        car_selection = int(input("Select Car Number to Be Returned: "))

        if car_selection > 0 and car_selection <= len(cars_list):

            print(f"You Selected {cars_list[car_selection - 1].get_name()}.")

            returning_confirmation = input("Confirm Returning (Y) or (N): ")

            if returning_confirmation.upper() == "Y":

                cars_list[car_selection - 1].increase_available_quantity()

                print("RESULT: Car Has Been Returned.")

            else:

                print("RESULT: Car Has Not Been Returned.")

        else:
                print("RESULT: Invalid Selection!\nEntered a Value Not in The List.")

    except ValueError:

        print("RESULT: Wrong Input!\nEntered a Non Integer Value.")


# A function that deals with printing renting total.
def display_total(total_cost, insurance_cost, tax_cost):

    print(f"Total Cost: ${format(total_cost, "0.2f")}")
    print(f"Total Insurance: ${format(insurance_cost, "0.2f")}")
    print(f"Total Tax: ${format(tax_cost, "0.2f")}")


# A function that deals with deleting a car.
def car_delete(cars_list):

    print("Select One of The Available Cars:")

    # A variable that holds car listing number for the car list menu.
    car_number = 1

    # Displaying cars in the list.
    for car in cars_list:

        print(f"{car_number}. {car.get_name()}")
        
        car_number += 1

    try:

        car_selection = int(input("Select Car Number to Be Returned: "))

        if car_selection > 0 and car_selection <= len(cars_list):

            deleting_confirmation = input("Confirm Deleting (Y) or (N): ")

            if deleting_confirmation.upper() == "Y":

                del cars_list[car_selection - 1]

                print("RESULT: Car Has Been Deleted.")

            else:

                print("RESULT: Car Has Not Been Deleted!")

        else:
                print("RESULT: Invalid Selection!\nEntered a Value Not in The List.")

    except ValueError:

        print("RESULT: Wrong Input!\nEntered a Non Integer Value.")


# Main Function
def main():

    # Reading file content to the list.
    cars_list = file_read()

    # Getting user option input.
    user_input = menu_display()

    # Variables to hold costs information for displaying.
    total_cost = 0
    insurance_cost = 0
    tax_cost = 0

    while user_input != 0:

        # only 1, 2, 3, 4, 5 and 0 are accepted. If the users enters anything else, 
        # the system keeps asking the user to enter a valid option.
        if user_input < 0 or user_input > 5:

            print("RESULT: Invalid Option!")
            print("***************************************************************")
            user_input = menu_display()

        if user_input == 1:

            print("***************************************************************")
            print("OPTION 1: Adding Car Information")
            new_car = add_car()

            if new_car != None:

                cars_list.append(new_car)
                print("RESULT: Car Has Been Added.")

        elif user_input == 2:

            print("***************************************************************")
            print("OPTION 2: Car Renting")

            car_total_cost, car_insurance_cost, car_tax_cost = car_rent(cars_list)
            # Updating costs information.
            total_cost += car_total_cost
            insurance_cost += car_insurance_cost
            tax_cost += car_tax_cost

        elif user_input == 3:

            print("***************************************************************")
            print("OPTION 3: Car Returning")

            car_return(cars_list)

        elif user_input == 4:

            print("***************************************************************")
            print("OPTION 4: Displaying Total")

            display_total(total_cost, insurance_cost, tax_cost)

        elif user_input == 5:

            print("***************************************************************")
            print("OPTION 5: Deleting Car")

            car_delete(cars_list)

        # Getting user option input.
        # Keep asking the user for input until user inputs 0 (to exit).
        print("***************************************************************")
        user_input = menu_display()

    # Exited the loop (the program).
    print("***************************************************************")
    print("OPTION 0: Exited Program.")

    print("Saving Changes To File......")

    # Writing list contents to the file.
    #for car in cars_list:

    file_write(cars_list)

    print("Done Writing to File.")


# Calling Main Function
main()