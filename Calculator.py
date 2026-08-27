def calculator(num1, num2, choice):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! 0 cannot be divided"
    else:
        return "Wrong choice"
while True:
    start = input("Are you want to use calculator? Yes or No: ").lower()
    if start == "no":
        print("Program katam. Allah Hafiz")
        break
    elif start == "yes":
        print("---Simple Calculator---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = int(input("Enter your choice 1-4: "))
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = calculator(num1, num2, choice)
        print("Result:", result)
    else:
        print("Only 'yes' or 'no' write")