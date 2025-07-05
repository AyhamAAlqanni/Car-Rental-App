
# Importing classes to main app file.
from Car_Class import Car

# A function that writes car's information to the file.
def file_write(added_car):

    write_to_file = open("Files/CarsData.txt", "a")

    write_to_file.write(str(added_car) + "\n")

    write_to_file.close()


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


# Main Function
def main():

    cars_list = []

    user_input = menu_display()

    while user_input != 0:

        if user_input < 0 or user_input > 5:

            print("Invalid Option!")
            user_input = menu_display()

        if user_input == 1:

            new_car = add_car()

            if new_car != None:

                cars_list.append(new_car)

                file_write(new_car)


# Calling Main Function
main()