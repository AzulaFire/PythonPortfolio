from functions import *

#CLI TO-DO List

while True:
  user_action = input("\nType add, edit, complete, show or exit: ").lower().strip()

  try:

    if user_action == 'add':
      add()
    elif user_action == 'show':
      show()
    elif user_action == 'edit':
      todos = show()

      number = getNumber('edit')
      new_value = input("\nEnter the new value: ")
      todos[int(number) - 1] = new_value.title() + "\n"

      with open(TODOS_PATH, 'w') as file:
        file.writelines(todos)

      print("\nThe to-do has been updated.\n")
    elif user_action == 'complete':
      todos = show()

      number = getNumber('complete')
      todo_to_remove = todos[int(number) -1].strip('\n')
      with open(TODOS_PATH, 'w') as file:
        todos.pop(int(number) - 1)
        file.writelines(todos)

      print(f"\nTodo '{todo_to_remove}' was completed and removed from the list.\n")
    elif user_action == 'exit':
      print("\nBye")
      break
    else:
      print("Incorrect response provided.")

  except ValueError:
    pass
