
import string

lower_letter = []
num_list = []

def encode(msg):
    new_message = ""

    for letter in string.ascii_lowercase:
        lower_letter.append(letter)

    for num in range(1,27):
        num_list.append(num)

    for letter in msg:
        if letter != " ":
            new_message = new_message + str(num_list[lower_letter.index(letter)])
        else:
            new_message = new_message + letter

    return new_message

message = input("Enter a message using any letter from a-z: ").lower()
print(encode(message))

encoded = encode(message)
print(encoded)


