def student_grade (grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    
num_of_student = int(input("How many student they are: \n"))

print ("=== Student Report === ")

highest_avg = 0
highest_name = ""
lowest_avg = 100
lowest_name = ""

for i in range(num_of_student):
    name = input("Student Name: \n")
    math = int(input("Enter the math score: \n"))
    science = int(input("Enter the science score: \n" ))
    history = int(input("Enter the history score: \n"))

    average = (math + science + history) /3
    grade = student_grade(average)
    print (f"{name}    | Avg: {average:.2f}      |Grade: {grade}")
    
    if average > highest_avg:
        highest_avg = average
        highest_name = name
    if average < lowest_avg:
        lowest_avg = average
        lowest_name = name

print (f"Highest Average: {highest_name} with {highest_avg:.2f}")
print (f"Lowest Average: {lowest_name} with {lowest_avg:.2f}")
