import tkinter as tk


# -------------------------- Calculator Functions --------------------

val = []

def button_click(button):
	print(button)
	txt_input.delete(0, tk.END)
	txt_input.insert(0, button)


	result = 0

	if txt_input.get().isnumeric():
		get_numbers(float(txt_input.get()))
	elif txt_input.get() == "+":
		result = add(val)
		txt_input.delete(0, tk.END)
		txt_input.insert(0, result)
	elif txt_input.get() == "-":
		result = subtract(val)
		txt_input.delete(0, tk.END)
		txt_input.insert(0, result)
	elif txt_input.get() == "*":
		result = multiply(val)
		txt_input.delete(0, tk.END)
		txt_input.insert(0, result)
	elif txt_input.get() == "/":
		result = divide(val)
		txt_input.delete(0, tk.END)
		txt_input.insert(0, result)
	elif txt_input.get() == "C":
		val.clear()
		txt_input.delete(0, tk.END)


def get_numbers(num):
	global val
	val.append(float(num))
	print(val)


def add(val):
    result = 0
    for x in val:
         result = (x + result)
    return int(result)	

def subtract(val):
    result = 0
    for x in val:
         result = (x - result)
    return int(result) * -1	

def multiply(val):
# Multiply elements one by one
    result = 1
    for x in val:
         result = result * x 
    return int(result)

def divide(val):
	result = val[0] / val[1]
	return result	

window = tk.Tk()
window.title("Python Playground")
window.configure(padx=20, pady=20)

large_font = ('Verdana', 16)

txt_input = tk.Entry(font=large_font)
txt_input.insert(0, 0)
lb_spacer_top = tk.Label()

buttons = [7, 4, 1, "/", 8, 5, 2, "*", 9, 6, 3, "-", "C", 0, ".", "+"]
btn_dict = {}

col = 0
row = 1
count = 0 	
for button in buttons:
	action = lambda x = button: button_click(x)
	btn_dict[button] = tk.Button(window, width=5, height=3, text=button, command=action)
	btn_dict[button].grid(row=row, column=col, padx=5, pady=5)
	col += 1
	count += 1
	if count == 4 or count == 8 or count == 12:
		row += 1
		col = 0
txt_input.grid(row=0, column=0, columnspan=4)
lb_spacer_top.grid(row=1, column=0, columnspan=4)

window.mainloop()