
# Enter today's date:
# How do you rate your mood today from 1 to 10?
# Let your thoughts flow: 


date = input("\n\nEnter today's date [YYYY-MM-DD]: ")

date = date.replace('/', '-')
date = date.replace('[', '')
date = date.replace(']', '')

new_journal = f'./Journals/{date}.txt'

mood = input("How do you rate your mood today from 1 to 10? ")
entry = input("Let your thoughts flow:\n\n")

new_entry = f"Mood Rating: {mood}\n\n{entry}"

with open(new_journal, 'w') as file:
  file.writelines(new_entry)


print("\n\nToday's journal entry has been saved. Thank you.\n\n")