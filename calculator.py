print("Hey! Welcome to bboaslah's calculator.")
num1 = int(input("Please enter the first number: "));
operator = input("Please enter the operator: ");
num2 = int(input("Please enter the second number: "));

if(operator == "*"):
    result = num1 * num2;
elif(operator == "+"):
    result = num1 + num2;
elif(operator == "-"):
    result = num1 - num2;
elif(operator == "/"):
    result = num1 / num2;

print(num1, operator, num2, "=", result);