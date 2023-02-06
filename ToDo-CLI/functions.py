
TODOS_PATH = "./files/todos.txt"

def add():
  x = 0
  num_of_todos = input("\nHow many to-do tasks do you want to add. Enter a number: ")
  if num_of_todos.isnumeric() == False:
    print("Error: A number must be entered.")
    return
  with open(TODOS_PATH) as file:  
    todos = file.readlines()

  while(x < int(num_of_todos)):
    user_prompt = "Enter a to-do: "
    user_text = input(user_prompt)
    todo = user_text.title() + "\n"
    todos.append(todo)
    with open(TODOS_PATH, 'w') as file:
      file.writelines(todos)
    x += 1

def show():
  with open(TODOS_PATH) as file: 
    todos = file.readlines()

  # list comprehension example - new_todos = [todo.strip('\n) for todo in todos]

  print("\n")
  for index, todo in enumerate(todos):
    todo = todo.strip('\n')
    print(f"{index + 1}. {todo}")
  return todos

def getNumber(mode):
    with open(TODOS_PATH) as file:  
      todos = file.readlines()

    number_check = True  
    
    while number_check:
      todo_number = input("\nEnter the number for the task you would like to %s: " % (mode))
      if todo_number.isnumeric() == False:
        print("Error: Must be a number.")
      elif int(todo_number) > len(todos):
        print("Number not found.")
      else:
        number_check = False
        return int(todo_number)