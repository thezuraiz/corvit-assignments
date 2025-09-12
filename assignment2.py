# Q1
print("Welcome to Python Programming!")

# Q2
x= input("Enter first number: ");
y= input("Enter second number: ");

print('After swapping: ');
x, y = y, x
print("First number: ", x);
print("Second number: ", y);

# Q3
temp = input("Enter temperature in Celsius: ")
temp = float(temp)
far = (temp * 9/5) + 32  
print("Temperature in Fahrenheit: ", far)

# Q4
digits =input("Enter a three-digit number: ")
total = 0
for digit in digits:
    total += int(digit)
print("Sum of digits:", total)

# Q5
num = int(input("Enter a number: "));
isEven = num%2==0;
print("Is Even: ",isEven);

# Q6
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
print("Largest number is:", max(first, second, third))
