"""
Author:         Griffin Warrington
Date:           2/09/26
Assignment:     Lab 04 si-calculator
Course:         CPSC1051
Lab Section:    CRN 002

"""


def get_property(prop=""):
    """ 
    Prompts user for property, validates, and returns prop
    
    Returns:
    mass/speed/distance/temperature if property is supported, False otherwise
    """


    #notes valid properties for conversion
    valid = ["distance", "mass", "speed", "temperature"]
    
    #accepts property number input under prop and stores the value through "" to strip and change value to a string
    if prop == "":
        prop = input().strip()
    else:
        prop = str(prop).strip()

    #examines and returns prop as valid if prop is in valid and Invalid unit type if false/not in
    if prop in valid:
        return prop
    else:
        print("Invalid unit type")
        return False


def get_unit(property, unit=""):
    """ 
    Prompts user for unit, validates, and returns unit
    
    Args: 
        property (str): Property to convert
            E.g. mass, speed
            
    Returns:
        String of the specific unit to convert, False if unit is unsupported
        
    """
    #locates which property is being used and prints the correct units and lists those units under valid
    if property == "distance":
        print("Please select one of the following to convert to meters: cm m km in ft: ")
        valid = ["cm", "m", "km", "in", "ft"] 
    elif property == "mass":
        print("Please select one of the following to convert to grams: mg g kg lbs: ")
        valid = ["mg", "g", "kg", "lbs"]
    elif property == "speed":
        print("Please select one of the following to convert to meters per second: m/s km/h ft/s mph: ")
        valid = ["km/h", "ft/s", "m/s", "mph"]
    elif property == "temperature":
        print("Please select one of the following to convert to Celsius: C F K: ")
        valid = ["C", "F", "K"]
    else:
        print("Invalid unit type")
        return False

    #accepts unit number input under unit and stores the value through "" to strip and change value to a string
    if unit == "":
        unit = input().strip()
    else:
        unit = str(unit).strip()

    if unit in valid:
        return unit
    else:
        print("Unsupported unit")
        return False
    
#accepts the unit and value for mass
def convert_mass(unit, value):
    #ensures mass is positive
    if value < 0:
        print("You can't have a negative mass!")
        return False
    #converts the following units
    elif unit == "mg":
        return value / 1000.00
    elif unit =="g":
        return value
    elif unit == "kg":
        return value * 1000.00
    elif unit == "lbs":
        return value * 453.592
    #if none of the previous units are detected return False
    else:
        return False
                
#accepts the unit and value for speed
def convert_speed(unit, value):
    #converts the following units
    if unit == "km/h":
        return value * 0.277778
    elif unit == "ft/s":
        return value * 0.3048
    elif unit == "m/s":
        return value
    elif unit =="mph":
        return value * 0.44704
    #if none of the previous units are detected return False
    else:
        return False   
 
#accepts the unit and value for distance
def convert_distance(unit, value):
    #converts the following units
    if unit == "cm":
        return value / 100.00
    elif unit == "km":
        return value * 1000.00
    elif unit == "in":
        return value * 0.0254
    elif unit == "ft":
        return value * 0.3048
    elif unit == "m":
        return value
    #if none of the previous units are detected return False
    else:
        return False

#accepts the unit and value for temperature
def convert_temperature(unit, value):
    #converts the following units
    if unit == "F":
        return (value - 32.00) * (5.00 / 9.00)
    elif unit == "K":
        return value - 273.15
    elif unit == "C":
        return value
    #if none of the previous units are detected return False
    else:
        return False




if __name__ == "__main__":
    #greets user, lists options and asks user for unit input
    print("Welcome to the SI units calculator!")
    print("Please input a type of unit that you would like to convert. Here are your options: \ndistance \nmass \nspeed \ntemperature\n")
   
   #accepts the unit needing converted and activates def get_property and returns prop if valid
    
    
    prop_val = get_property() #Implements get_property() to take in user input and validate it
    if prop_val is False:
        exit()

    unit = get_unit(prop_val) #Implements get_unit() to take in user input and validate it with get_property
    if unit is False:
        exit()


    print("Please input a value:") #ask user for digit/number of units wanting to be calculated
    value = float(input()) #accepts input as float

    #locates the property, tells program to return to the def function that equals that property and returns adjusted by sending the unit and value
    if prop_val == "mass":
        result = convert_mass(unit, value)
        final_unit = "grams"
    elif prop_val == "speed":
        result = convert_speed(unit, value)
        final_unit = "meters per second"
    elif prop_val == "distance":
        result = convert_distance(unit, value)
        final_unit = "meters"
    elif prop_val == "temperature":
        result = convert_temperature(unit, value)
        final_unit = "Celsius"
    #ensures value is correct
    else:
        result = False
        
    if result is not False: #displays final result using previous
        print(f"{value:.2f} {unit} in {final_unit}: {result:.2f}")