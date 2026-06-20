students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll No: ")
        name = input("Name: ")
        students[roll] = name
        print("Student Added")

    elif choice == "2":
        for roll, name in students.items():
            print(roll, "-", name)

    elif choice == "3":
        break
