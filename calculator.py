print("Select an operation to perform: ")

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    #code for ADD

    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Result is: " + str(int(num1) + int(num2)))
elif operation == "2":
    #code for SUBTRACT

    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Result is: " + str(int(num1) - int(num2)))
elif operation == "3":
    #code for MULTIPLY

    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Result is: " + str(int(num1) * int(num2)))
elif operation == "4":
    #code for DIVIDE

    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Result is: " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry!")
