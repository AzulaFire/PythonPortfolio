import random

numbers = []

for x in range(11):
    num = random.randint(1, 10)
    if num not in numbers:
        numbers.append(num)

def get_square(num):
    return num * num

for num in numbers:
    result = get_square(num)
    print(f"Square of {num} = {result}")

