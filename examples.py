# Python Examples

# Python is a high-level programming language.

"""
Python (1 line) is an interpreted, dynamically typed languge. It is primarily used for Data Science, AI, Automation and Websites/Web Applications. Can also make desktop applications.

print("Hello, World")

--------------------------

Java (5 lines) is a compiled, statically typed language (variable types are set and cannot be changed). It is primarily used for desktop and mobile applications. Because it is a compiled language, applications tend to run a little faster than Python applications.

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World");
    }
}

--------------------------

c# - 13 lines

using System;
using System.Collections.Generic;
using System.Text;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, world!");
        }
    }
}


"""

# List

example_list = [1, 2, 3, 4, 5]
print(example_list)

example_list.append(6)
print(example_list)

example_list.pop(2)
print(example_list)

# Tuple - Cannot be changed

example_tuple = ("A", "B", "C", "D")

# Dictionary

example_dictionary = {"height":188, "weight":120, "age":44, "gender":"male"}
print(example_dictionary)

print(example_dictionary.keys())
print(example_dictionary.values())
print(example_dictionary["gender"])

# Using keyword --> in

password = "x7tyGhvAb$"
print(password)
print("x" in password)

for i in password:
  print(i + " is alphanumeric: ", i.isalnum())
  print(i + " is a alpha: ", i.isalpha())
  print(i + " is a digit: ", i.isdigit())
  print(i + " is numeric: ", i.isnumeric())
  print(i + " is uppercase: ", i.isupper())
  print(i + " is lowercase: ", i.islower())
  print(i + " is ascii: ", i.isascii())

print("password is greater than 8 characters: ", len(password) > 8)

special_characters = "!@#$%^&*()-+?_=,<>/"

if any(character in special_characters for character in password):
    print("yes")
else:
    print("no")

# while loop

x = 0

while x <= 5:
  print(x)
  x += 1

# for loop

for item in example_list:
  print(item)

# strings

name = "john"
feet_inches = "5_11"

print(name.startswith('jo'))
print(name.capitalize())
print(name.title())
print(name.endswith('h'))
print(feet_inches.split('_'))


