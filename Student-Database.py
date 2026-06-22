#Initial Dictionary
students = {
    "001": {"name": "Alice", "math": 85, "science": 90, "english": 88},
    "002": {"name": "Bob", "math": 72, "science": 78, "english": 75},
}

#Main Menu
while True:
    print("\n--- Student Database Menu ---")
    print("1. Add a new student")
    print("2. Search by ID")
    print("3. Find students above average threshold")
    print("4. List all students with averages")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    # Next, we build the structure to handle the choice
    if choice == "1":
        # Logic for adding a student goes here
        new_id = input("Enter new student ID: ")
        name = input("Enter student name: ")
        math_score = int(input("Enter math score: "))
        english_score = int(input("Enter english score: "))
        science_score = int(input("Enter science score: "))

        students[new_id] = { #insert new student info to the dictionary
            "name": name,
            "math": math_score,
            "science": science_score,
            "english": english_score
        }
       
        print("\nStudent added successfully!")
        pass
    elif choice == "2":
        # Logic for searching goes here
        print("\nSearch by ID:")
        student_id = input("Enter student ID: ")
        if student_id in students:
            info = students[student_id]
            print (f"Student found: ID: {student_id}, Name: {info['name']}, Math: {info['math']}, Science: {info['science']}, English: {info['english']}")
        else:
            print("Student not found.")
        pass
    elif choice == "3":
        # Logic for filtering by average goes here
        threshold = float(input("Enter average score threshold: "))
        results = []

        for student_id , info in students.items():
            total = info["english"] + info["math"] + info["science"]
            average = total / 3
            if average > threshold:
                results.append(f"Name: {info["name"]} (Avg: {average:.1f})")

        print(f"\nStudents with an average above {threshold}:")

        if results:
            for match in results:
                print(f"- {match}")
        else:
            print("No students found above this threshold.")
        pass
    elif choice == "4":
        # Logic for listing all goes here
        for student_id , info in students.items():
            total = info["english"] + info["math"] + info["science"]
            average = total / 3
            print(f"student ID: {student_id}, Name: {info['name']}, Average Score: {average:.1f}")
        
        pass
    elif choice == "5":
        print("Goodbye!")
        break # This breaks the loop and ends the program
    else:
        print("Invalid choice, please try again.")
