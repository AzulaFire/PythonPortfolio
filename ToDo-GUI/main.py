import functions
import time
import PySimpleGUI as sg
import os

# Check if file exists

if not os.path.exists("./files/todos.txt"):
  with open("./files/todos.txt", "w") as file:
    pass

# Functions

def get_count():
  count = len(functions.gui_get_todos())
  return f"Current To-Do Count: {count}"

def get_date():
  now = time.strftime("%b %d, %Y %H:%M:%S")
  return now 

# ---------------------------------------------------------

# Add your new theme colors and settings

custom_theme = {'BACKGROUND': '#191A19',
                'TEXT': '#D8E9A8',
                'INPUT': '#1E5128',
                'TEXT_INPUT': '#D8E9A8',
                'SCROLL': '#c7e78b',
                'BUTTON': ('#D8E9A8', '#1E5128'),
                'PROGRESS': ('#D8E9A8', '#4E9F3D'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('Custom', custom_theme)

# GUI Settings - Theme, Font
sg.theme('Custom')
sg.set_options(font='Arial 18')

# UI Elements
# [name('Frame'), sg.Frame('Frame', [[sg.T(s=15)]])]

title_label = sg.Text("Type in a To-Do:", font='Arial 22') # Label
time_label = sg.Text(get_date(), key='-TIME-', font='Arial 12') # Label
count_label = sg.Text(get_count(), key='-COUNT-', font='Arial 15') # Label
input_box = sg.InputText(tooltip="Enter To-Do", key='-IN-', do_not_clear=False) # Textbox
todo_list = sg.Listbox(values=functions.gui_get_todos(), key='-LIST-', enable_events=True, size=(45, 10), text_color="#D8E9A8")
add_button = sg.Button(key='-ADD-', size=2, image_source="./assets/add.png", tooltip="Add", mouseover_colors="#4E9F3D") # Button
edit_button = sg.Button(key='-EDIT-', size=2, image_source="./assets/edit.png", tooltip="Edit", mouseover_colors="#4E9F3D")
complete_button = sg.Button(key='-COMPLETE-', size=2, image_source="./assets/done.png", tooltip="Complete", mouseover_colors="#4E9F3D")
exit_button = sg.Button(key='-EXIT-', size=2, image_source="./assets/exit.png", tooltip="Exit", mouseover_colors="#4E9F3D")

# Prepare the widgets for the left column
left_column_content = [[input_box],
                       [todo_list]]
 
# Prepare the widgets for the right column
right_column_content = [[add_button], 
                        [edit_button],
                        [complete_button]]
 

# Construct the Column widgets
left_column = sg.Frame('', [[sg.Column(left_column_content)]])
right_column = sg.Column(right_column_content)
  

# Construct the layout
layout = [
  [time_label], 
  [title_label], 
  [left_column, right_column], 
  [count_label], 
  [exit_button]
  ]

# Create the window
window = sg.Window("TO-DO Task Manager", layout, finalize=True)
# window.Maximize()
window.bind("<Escape>", "-ESCAPE-")

# --------------------- RENDER APP --------------------  


# Create an event loop
while True:
  event, values = window.read()
  
  # OnClick - Add button to Add ToDo
  if event == '-ADD-':
    todos = functions.gui_get_todos()
    new_todo = values['-IN-'].title() + "\n"

    if len(new_todo) > 0:
      todos.append(new_todo)
      functions.gui_write_todos(todos)
      window['-LIST-'].update(values=todos)
      window['-COUNT-'].update(value=get_count())
      window['-TIME-'].update(value=get_date())
    else:
      print("Value was Zero")

  # OnClick - Edit button to Edit ToDo
  elif event == '-EDIT-':
    try:
      selected_todo = values['-LIST-'][0]
      updated_todo = values['-IN-'].replace("\n", "")
      updated_todo = updated_todo.title() + "\n"

      if updated_todo == selected_todo + "\n":
        sg.popup("Error: Please enter a value.")
      else:
        if updated_todo != "\n":
          todos = functions.gui_get_todos()
          index = todos.index(selected_todo)
          todos[index] = updated_todo
          functions.gui_write_todos(todos)
          todos = functions.gui_get_todos()
          window['-LIST-'].update(values=todos)
          window['-TIME-'].update(value=get_date())
    except IndexError:
      sg.popup("Error: Please select an item first.")

  # Update Listbox on User Select
  elif event == '-LIST-':
    window['-IN-'].update(value=values['-LIST-'][0])

  # OnClick - Complete button to Remove ToDo
  elif event == '-COMPLETE-':
    try:
      selected_todo = values['-LIST-'][0]

      todos = functions.gui_get_todos()
      index = todos.index(selected_todo)
      todos.pop(index)

      functions.gui_write_todos(todos)
      window['-LIST-'].update(values=todos)
      window['-COUNT-'].update(value=get_count())
      window['-TIME-'].update(value=get_date())
    except IndexError:
      sg.popup("Error: Please select an item first.")

  elif event == '-ESCAPE-':
    window.Minimize()

  # End program if user closes window
  elif event in (sg.WINDOW_CLOSED, "-EXIT-"):
    break

window.close()
