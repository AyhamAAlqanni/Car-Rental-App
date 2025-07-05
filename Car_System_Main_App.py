
# Importing classes to main app file.
from Car_Class import Car


# A function that displays the menu.
def menu_display():

    try:

        print("Please Select One:")
        print("\t1- Add Car.")
        print("\t2- Car Rental.")
        print("\t3- Car Return.")
        print("\t4- Print The Total.")
        print("\t5- Delete Car.")

        user_input = int(input("Option Number: "))

        return user_input
    
    except ValueError:

        print("Invalid Input!")


# A function that adds a car
def add_car():

    car_name = input("Enter Car's Name: ")
    available_quantity = int(input("Enter Available Car Quantity: "))
    daily_rent_cost = float(input("Enter Daily Rent Cost: "))
    liability_cost = float(input("Enter Liability Insurance Cost: "))
    comprehensive_cost = float(input("Enter Comprehensive Insurance Cost: "))

    car_object = Car(car_name, available_quantity, daily_rent_cost, liability_cost, comprehensive_cost)

    return car_object


# Main Function
def main():

    cars_list = []

    user_input = menu_display()

    if user_input == 1:

        cars_list.append(add_car())

        print(cars_list[0])


# Calling Main Function
main()