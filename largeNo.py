numbers = [10, 45, 23, 89, 12]
Largest = numbers[0]
for number in numbers:
    if number > Largest:
        Largest = number
print("The largest number is:", Largest)

smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("The smallest number is:", smallest)