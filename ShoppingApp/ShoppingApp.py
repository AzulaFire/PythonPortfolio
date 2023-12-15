
# BEGINNER

# total = 0

# item_cost = float(input("\nEnter the price of the 1st item: $"))
# total += item_cost
# print(f"\nThe running total is: ${total}")

# item_cost = float(input("\nEnter the price of the 2nd item: $"))
# total += item_cost
# print(f"\nThe running total is: ${total}")

# item_cost = float(input("\nEnter the price of the 3rd item: $"))
# total += item_cost
# print(f"\nThe running total is: ${total}")

# item_cost = float(input("\nEnter the price of the 4th item: $"))
# total += item_cost
# print(f"\nThe running total is: ${total}")

# if total >= 150:
#     total = total / 2
# elif total >= 100:
#     total = total - (total * .25)
# elif total > 75:
#     total = total - (total * .15)

# print(f"\nThe total is: ${total}")

# INTERMEDIATE 

num_prefix = ['st', 'nd', 'rd', 'th']
total = 0

for index, num in enumerate(num_prefix):
    item_cost = float(input(f"\nEnter the price of the {index + 1}{num_prefix[index]} item: $"))
    total += item_cost
    print(f"\nThe running total is: ${total:.2f}")  

discount = 0.5 if total >= 150 else (0.75 if total >= 100 else (0.85 if total > 75 else 1))
total *= discount

print(f"\nTotal: ${total:.2f}\n")


# ADVANCED

# total = sum(float(input(f"\nEnter the price of the {i}{'th' if i > 3 else ['st', 'nd', 'rd'][i - 1]} item: $")) for i in range(1, 5))
# print(f"\nThe running total is: ${total:.2f}")

# discount = 0.5 if total >= 150 else (0.75 if total >= 100 else (0.85 if total > 75 else 1))
# total *= discount

# print(f"\nTotal: ${total:.2f}\n")
