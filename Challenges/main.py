
# ------------------------------------------------------------------------------

# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def capital_indexes(word):
    index_list = []
    for index, letter in enumerate(word):
        if letter.isupper():
            index_list.append(index)
    return index_list

result = capital_indexes("TEsT")
print(result)

# ------------------------------------------------------------------------------

# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".
import math

def mid(word):
    word_len = len(word)
    if word_len % 2 == 0:
        return ""
    else:
        num = math.ceil(word_len / 2) - 1
        print(num)
        return word[num]
    
print(mid("abcde"))    


# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def mid_short(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]

# ------------------------------------------------------------------------------


# Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# In this case, the number of people online is 2.

# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

# Your function should return the number of people who are online.

def online_count(dict):
    count = 0
    for key, value in dict.items():
        if value == "online":
            count += 1

    return count

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

online = online_count(statuses)

print(f"The number of people online is: {online}")

# short version
def online_count_short(people):
    return len([p for p in people if people[p] == "online"])

# ------------------------------------------------------------------------------

# Randomness
# Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.

# Calling the function multiple times should (usually) return different numbers.

# For example, calling random_number() some times might first return 42, then 63, then 1.

import random

def random_number():
    num = random.randint(1,101)
    return num

random_number()

# ------------------------------------------------------------------------------

# Type check
# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

def only_ints(one, two):
    if type(one) == int and type(two) == int:
        return True
    else:
        return False

only_ints(2,24)

# ------------------------------------------------------------------------------

# Double letters
# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(word):
    num = len(word) - 1
    for c in range(0, num):
        if word[c] == word[c + 1]:
            return True
    return False
double_letters("hello")


# ------------------------------------------------------------------------------

# Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

# (You may assume that the input to add_dots does not itself contain any dots.)

def add_dots(word):
    char = list(word)
    new_word = ".".join(char)
    return new_word

def remove_dots(word):
    new_word = word.replace(".", "")
    return new_word

add_dots("test")
remove_dots("t.e.s.t")

# ------------------------------------------------------------------------------

# Thousands separator
# Write a function named format_number that takes a non-negative number as its only parameter.

# Your function should convert the number to a string and add commas as a thousands separator.

# For example, calling format_number(1000000) should return "1,000,000".


# (\d) one digit…
# (?= followed by…
#    (\d{3}) 3 digits
# )


# (\d) capture one digit…
# (?= which is followed by…
#    (\d{3})+ one or more groups of 3 digits…
#    (?!\d) which are not followed by any more digits
# )

import re

def format_number(num):
    pattern = "(\d)(?=(\d{3})+(?!\d))"
    str_num = str(num)
    new_num = re.sub(pattern, r"\1,", str_num)
    print(new_num)

format_number(900000078963547)

# built-in solution
def format_number_short(n):
    return "{:,}".format(n)