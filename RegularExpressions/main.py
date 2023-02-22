import re

with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()

print("Number of Chapters")

pattern = re.compile("Chapter [0-9]+")

print(re.findall(pattern, book))
print(len(re.findall(pattern, book)))