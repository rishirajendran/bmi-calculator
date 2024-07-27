def get_height():
    height = input("Enter your height: ")
    return height

def get_weight():
    weight = input("Enter your weight: ")
    return weight

def get_units():
    print("Enter 1 if you would like to use kilograms/meters. Enter 2 if you would like to use pounds/inches.")
    units_id = input("Enter your number: ")
    
    if(units_id == "1"):
        return "kg"
    elif(units_id == "2"):
        return "lb"
    else:
        print("Not a valid input. Restarting...")
        return get_units()

def calc_bmi(units, height, weight):
    if (units == "kg"):
        bmi = weight/(height**2)
    else:
        bmi = 703*weight/(height**2)
    return bmi

def eval_bmi(bmi):
    if(bmi < 18.5):
        return "underweight"
    elif(18.5 <= bmi < 25):
        return "normal weight"
    elif(25 <= bmi < 30):
        return "overweight"
    else:
        return "obese"

def main():
    print("Welcome to the BMI Calculator!")
    units = get_units()
    height = float(get_height())
    weight = float(get_weight())
    bmi = calc_bmi(units, height, weight)
    category = eval_bmi(bmi)
    print("Your BMI is {}.".format(bmi))
    print("That BMI is categorized as {}.".format(category))
    
if __name__ == "__main__":
    main()