
# Importing classes to main app file.
from Car_Class import Car

# A function that writes car's information to the file.
def file_write(added_car):

    write_to_file = open("Files/CarsData.txt", "a")

    #write_to_file.write(str(added_car) + "\n")
    write_to_file.write("Car Name:" + str(added_car.get_name()) + "\n")
    write_to_file.write("Available Quantity:" + str(added_car.get_quantity_available()) + "\n")
    write_to_file.write("Daily Rent Cost:" + str(added_car.get_daily_rent_cost()) + "\n")
    write_to_file.write("Liability Insurance Cost:" + str(added_car.get_liability_insurance_cost()) + "\n")
    write_to_file.write("Comprehensive Insurance Cost:" + str(added_car.get_comprehensive_insurance_cost()) + "\n")

    write_to_file.close()


# A function that reads car's information from the file.
def file_read():

    cars_list = []

    read_from_file = open("Files/CarsData.txt", "r")

    car_name = read_from_file.readline()

    while car_name != "":

        car_name = car_name.rstrip("\n").split(":")
        car_name = car_name[1]

        car_quantity = read_from_file.readline().rstrip("\n").split(":")
        car_quantity = car_quantity[1]

        car_daily_cost = read_from_file.readline().rstrip("\n").split(":")
        car_daily_cost = car_daily_cost[1]

        car_liability_insurance_cost = read_from_file.readline().rstrip("\n").split(":")
        car_liability_insurance_cost = car_liability_insurance_cost[1]

        car_comprehensive_insurance_cost = read_from_file.readline().rstrip("\n").split(":")
        car_comprehensive_insurance_cost = car_comprehensive_insurance_cost[1]

        car_object = Car(car_name, int(car_quantity), float(car_daily_cost), float(car_liability_insurance_cost), 
                         float(car_comprehensive_insurance_cost))
        
        cars_list.append(car_object)

        car_name = read_from_file.readline()

    read_from_file.close()

    return cars_list


# A function that displays the menu.
def menu_display():

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

        return -1


# A function that adds a car
def add_car():

    try:

        car_name = input("Enter Car's Name: ")
        available_quantity = int(input("Enter Available Car Quantity: "))
        daily_rent_cost = float(input("Enter Daily Rent Cost: "))
        liability_cost = float(input("Enter Liability Insurance Cost: "))
        comprehensive_cost = float(input("Enter Comprehensive Insurance Cost: "))

        car_object = Car(car_name, available_quantity, daily_rent_cost, liability_cost, comprehensive_cost)

        return car_object
    
    except ValueError:

        print("Wrong Input!\nCar Was Not Added.")


# A function that deals with car renting processes.
def car_rent(cars_list):

    print("Select One of The Available Cars:")
    print("-------------------------------------------------------------------------------------------------------")
    print("Model", "\t\tAvailable", "\tPrice/Day", "\tLiability Insurance/Day", "\tComprehensive Insurance/Day")
    print("-------------------------------------------------------------------------------------------------------")

    #print(f"1. Camry\t----3\t\t--$120\t\t\t$90\t\t\t\t$60")

    car_number = 1

    for car in cars_list:

        print(f"{car_number}. {car.get_name()}\t    {car.get_quantity_available()}\t\t  ${car.get_daily_rent_cost()}" + 
              f"\t\t${car.get_liability_insurance_cost()}\t\t\t${car.get_comprehensive_insurance_cost()}")
        
        car_number += 1

    car_selection = int(input("Enter Car Number Selection: "))

    if car_selection > 0 and car_selection <= len(cars_list):

        rented_days = int(input("Enter How Many Days to Be Rented: "))
        insurance_type = input("Enter (L) For Liability Insurance, (C) For Comprehensive Insurance: ")

        renting_cost = cars_list[car_selection - 1].get_daily_rent_cost() * rented_days
        tax_cost = renting_cost * 0.05
        total_cost = renting_cost + tax_cost

        print(f"Renting Cost: ${format(renting_cost, "0.2f")}")
        print(f"Tax (5%): ${format(tax_cost, "0.2f")}")

        if insurance_type.upper() == "L":

            print(f"Insurance Type: Liability.\tCost: ${format(cars_list[car_selection - 1].get_liability_insurance_cost(), "0.2f")}")

            insurance_cost = cars_list[car_selection - 1].get_liability_insurance_cost()

        elif insurance_type.upper() == "C":

            print(f"Insurance Type: Comprehensive.\tCost: ${format(cars_list[car_selection - 1].get_comprehensive_insurance_cost(), "0.2f")}")

            insurance_cost = cars_list[car_selection - 1].get_comprehensive_insurance_cost()

        total_cost += insurance_cost

        print(f"Total: ${format(total_cost, "0.2f")}")

        renting_confirmation = input("Confirm Renting (Y) or (N): ")

        if renting_confirmation.upper() == "Y":

            cars_list[car_selection - 1].decrease_available_quantity()

            print("Car Was Added To The Total Menu Option.")

            return total_cost, insurance_cost, tax_cost 
        
        else:

            print("Car Was Not Rented.")


# A function that deals with car returing processes.
def car_return(cars_list):

    car_number = 1

    for car in cars_list:

        print(f"{car_number}. {car.get_name()}")
        
        car_number += 1

    car_selection = int(input("Select Car Number to Be Returned: "))

    if car_selection > 0 and car_selection <= len(cars_list):

        print(f"You Selected {cars_list[car_selection - 1].get_name()}.")

        returning_confirmation = input("Confirm Returning (Y) or (N): ")

        if returning_confirmation.upper() == "Y":

            cars_list[car_selection - 1].increase_available_quantity()

            print("Car Returned.")

        else:

            print("Car Was Not Returned.")


# A function that deals with printing renting total.
def display_total(total_cost, insurance_cost, tax_cost):

    print(f"Total Cost: ${format(total_cost, "0.2f")}")
    print(f"Total Insurance: ${format(insurance_cost, "0.2f")}")
    print(f"Total Tax: ${format(tax_cost, "0.2f")}")


# A function that deals with deleting a car.
def car_delete(cars_list):

    print("Select One of The Available Cars:")

    car_number = 1

    for car in cars_list:

        print(f"{car_number}. {car.get_name()}")
        
        car_number += 1

    car_selection = int(input("Select Car Number to Be Returned: "))

    if car_selection > 0 and car_selection <= len(cars_list):

        deleting_confirmation = input("Confirm Deleting (Y) or (N): ")

        if deleting_confirmation.upper() == "Y":

            del cars_list[car_selection - 1]

            print("Car Was Deleted.")

        else:

            print("Car Was Not Deleted.")


# Main Function
def main():

    cars_list = file_read()

    user_input = menu_display()

    total_cost = 0
    insurance_cost = 0
    tax_cost = 0

    while user_input != 0:

        if user_input < 0 or user_input > 5:

            print("Invalid Option!")
            user_input = menu_display()

        if user_input == 1:

            new_car = add_car()

            if new_car != None:

                cars_list.append(new_car)

                file_write(new_car)

        elif user_input == 2:

            car_total_cost, car_insurance_cost, car_tax_cost = car_rent(cars_list)
            total_cost += car_total_cost
            insurance_cost += car_insurance_cost
            tax_cost += car_tax_cost

        elif user_input == 3:

            car_return(cars_list)

        elif user_input == 4:

            display_total(total_cost, insurance_cost, tax_cost)

        elif user_input == 5:

            car_delete(cars_list)

        user_input = menu_display()


# Calling Main Function
main()