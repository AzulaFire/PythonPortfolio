import string

lower_letter_list = []
alpha_numbers = []

for letter in string.ascii_lowercase:
    lower_letter_list.append(letter)

for num in range(1, 27):
    alpha_numbers.append(num)

message = input("\nEnter a message to encode: ").lower()
encoded_message = ""

for letter in message:
    if letter != " ":
        encoded_message += str(alpha_numbers[lower_letter_list.index(letter)])
    else:
        encoded_message += letter

print(f"\n{encoded_message}\n")

