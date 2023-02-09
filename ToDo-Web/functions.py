
TODOS_PATH = "files/todos.txt"

# GUI Version - FUNCTIONS

def gui_write_todos(todo):
    with open(TODOS_PATH, 'w') as file:
      file.writelines(todo)

def gui_get_todos():
  with open(TODOS_PATH) as file:  
    todos_local = file.readlines()
  return todos_local