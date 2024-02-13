def factorial(number):
    sum = 1
    for i in range(1, number + 1):
        sum *= i
    return sum

numbers = []
for i in range(11):
    numbers.append(str(factorial(i))[-1])

print(numbers)