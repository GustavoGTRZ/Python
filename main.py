from numpy import number


num1 = int(input("Type the first number: "))

num2 = int(input("Type the second number: "))

numbers = []

numbers.append(num1)
numbers.append(num2)

total = sum(numbers)

print("The sum of the numbers is: ", total)