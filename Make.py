# Solution: Class List Program

names = ["Name1", "Name2", "Name3", "Name4", "Name5", "Name6", "Name7", "Name8", "Name9", "Name10"]

while True:
    print("Choose an option: (1) Output range, (2) From point to end, (3) From beginning to point")
    try:
        option = int(input("Enter 1, 2, or 3: "))
        if option not in [1, 2, 3]:
            raise ValueError("Invalid option")
        break
    except ValueError:
        print("Please enter a valid option (1, 2, or 3):")

if option == 1:
    start = int(input("Enter the start index: "))
    end = int(input("Enter the end index: "))
    print(names[start:end])
elif option == 2:
    start = int(input("Enter the start index: "))
    print(names[start:])
elif option == 3:
    end = int(input("Enter the end index: "))
    print(names[:end])