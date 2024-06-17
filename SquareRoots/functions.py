

# def my_function():
#     print("My first function")

# def greeting(name):
#     print(f"Hello, {name}")

# def greeting2(name, food):
#     print(f"My name is {name}. I love {food}.")

# def welcome(country="Japan"):
#     print(f"I am from {country}")

def count(num):
    if num <= 0:
        print("stop")
    else:
        print(num)
        count(num - 1)


count(5)