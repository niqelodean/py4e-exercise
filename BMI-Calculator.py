def calculate_bmi(bmi):
    if bmi >= 30:
        return ("Obese")
    elif bmi >= 25:
        return ("Overweight")
    elif bmi >= 18.5:
        return ("Normal")
    else:
        return ("Underweight")
name = input("What is your name: ")
weight = int(input("how much do u weight: "))
height = float(input("How tall are you: "))

bmi_score = weight / (height*height)
bmi_category = calculate_bmi(bmi_score)

print ("---BMI Calculator---")
print ("Hi", name)
print ("Your weight is:" ,weight)
print ("Your Height is:",height)
print ("Your BMI Score is :", round(bmi_score, 2))
print ("You're ", bmi_category)