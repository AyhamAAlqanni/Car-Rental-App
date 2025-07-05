
class Car:

    def __init__(self, name, quantity_available, daily_rent_cost, liability_insurance_cost, comprehensive_insurance_cost):

        self.__name = name
        self.__quantity_available = quantity_available
        self.__daily_rent_cost = daily_rent_cost
        self.__liability_insurance_cost = liability_insurance_cost
        self.__comprehensive_insurance_cost = comprehensive_insurance_cost

    def set_name(self, name):

        self.__name = name

    def get_name(self):

        return self.__name
    
    def set_quantity_available(self, quantity_available):

        self.__quantity_available = quantity_available

    def get_quantity_available(self):

        return self.__quantity_available
    
    def set_daily_rent_cost(self, daily_rent_cost):

        self.__daily_rent_cost = daily_rent_cost

    def get_daily_rent_cost(self):

        return self.__daily_rent_cost
    
    def set_liability_insurance_cost(self, liability_insurance_cost):

        self.__liability_insurance_cost = liability_insurance_cost

    def get_liability_insurance_cost(self):

        return self.__liability_insurance_cost
    
    def set_comprehensive_insurance_cost(self, comprehensive_insurance_cost):

        self.__comprehensive_insurance_cost = comprehensive_insurance_cost

    def get_comprehensive_insurance_cost(self):

        return self.__comprehensive_insurance_cost
    
    def __str__(self):

        return (f"Car Name: {self.__name}\nAvailable Quantity: {self.__quantity_available}\n"
                f"Daily Rent Cost: ${format(self.__daily_rent_cost, "0.2f")}\n"
                f"Liability Insurance Cost: ${format(self.__liability_insurance_cost, "0.2f")}\n"
                f"Comprehensive Insurance Cost: ${format(self.__comprehensive_insurance_cost, "0.2f")}")