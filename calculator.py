print("5 - Add")
print("6 - Subtract")
print("7 - Multiply")
print("8 - Divide")
option = int(input("Choose an operaton: "))
result = 0

if (option in [5,6,7,8]):
     num1 = int(input("Enter first number:"))
     num2 = int(input("Enter Second number:"))

     if(option == 5):
          result = num1 + num2
     elif(option == 6):
          result = num1 - num2
     elif(option == 7):
          result = num1 * num2
     elif(option == 8):
          result = num1 // num2          
else:
    print("Invalid operation enetered")
          
print("The result of the operation is {}".format(result))         