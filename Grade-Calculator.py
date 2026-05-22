def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
math = int(input("Enter the math score: "))
science = int(input("Enter the science score: "))
history = int(input("Enter the history score: "))
compsci = int(input("Enter the computer science score: "))
english = int(input("Enter the english score: "))
average = (math + science + history + compsci + english) / 5

grade = calculate_grade(average)
print ("---Results---")
print("Your average score is:", average)
print("Your grade is:", grade)
