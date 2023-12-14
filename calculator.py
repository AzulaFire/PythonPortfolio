import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title("Calculator")
window.config(padx=20, pady=5, background="thistle4")

BG = "cornflower blue"

numbers = []
operator = []
full_equation = []
reset = False

def enter(event=None):
	calc("=")

def keyPressEvent(event):
	key = event.char
	print(key)
	if event.char == "0":
		build(0)
	elif event.char == "1":
		build(1)
	elif event.char == "2":
		build(2)
	elif event.char == "3":
		build(3)
	elif event.char == "4":
		build(4)
	elif event.char == "5":
		build(5)
	elif event.char == "6":
		build(6)
	elif event.char == "7":
		build(7)
	elif event.char == "8":
		build(8)
	elif event.char == "9":								
		build(9)
	elif event.char == "+":							
		calc("+")
	elif event.char == "-":								
		calc("-")
	elif event.char == "*":								
		calc("*")
	elif event.char == "/":								
		calc("/")
	elif event.char == ".":								
		build(".")		

					
def clear():
	global reset
	txt_main.delete("0", tk.END)
	lb_equation.config(text="")		
	numbers.clear()
	operator.clear()
	full_equation.clear()			
	reset = False

def check(start_over):
	global reset
	if reset == True:
		#result = txt_main.get()
		#lb_equation.config(text=result)
		txt_main.delete("0", tk.END)
		reset = False

def build(val):
	check(reset)	
	txt_main.insert(tk.END, val)
	full_equation.append(val)

def calc(symbol):
	global reset
	if symbol == "=" and len(operator) > 0 and len(numbers) > 0:
		if operator[0] == "+":
			val = int(txt_main.get())
			txt_main.delete("0", tk.END)
			numbers.append(val)	
			result = sum(numbers)
			txt_main.insert(tk.END, result)
			lb_equation.config(text=full_equation)			
			numbers.clear()
			operator.clear()
			full_equation.clear()
			reset = True
		elif operator[0] == "-":
			val = int(txt_main.get())
			txt_main.delete("0", tk.END)
			numbers.append(val)			
			result = (numbers[0] - numbers[1])
			txt_main.insert(tk.END, result)
			lb_equation.config(text=full_equation)				
			numbers.clear()
			operator.clear()
			full_equation.clear()			
			reset = True
		elif operator[0] == "*":
			val = int(txt_main.get())
			txt_main.delete("0", tk.END)
			numbers.append(val)			
			result = (numbers[0] * numbers[1])
			txt_main.insert(tk.END, result)
			lb_equation.config(text=full_equation)				
			numbers.clear()
			operator.clear()
			full_equation.clear()			
			reset = True
		elif operator[0] == "/":
			val = int(txt_main.get())
			txt_main.delete("0", tk.END)
			numbers.append(val)			
			result = float(numbers[0] / numbers[1])
			txt_main.insert(tk.END, result)
			lb_equation.config(text=full_equation)				
			numbers.clear()
			operator.clear()
			full_equation.clear()			
			reset = True									
	else:
		full_equation.append(symbol)
		lb_equation.config(text=full_equation)			
		operator.append(symbol)
		val = float(txt_main.get())
		reset = True
		numbers.append(val)

# GUI

# Lazy Way! Update variables to Dictionary for cleaner code.

plus = "+"
minus = "-"
multiply = "*"
divide = "/"
equals = "="

nine = 9
eight = 8
seven = 7
six = 6
five = 5
four = 4
three = 3
two = 2
one = 1
zero = 0
dot = "."

btn_clear = tk.Button(text="C", width=10, background=BG, font="arial 9 bold", command=clear)
lb_equation = tk.Label(width=40, font="arial 12 bold", background="thistle4")
txt_main = tk.Entry(width=30, font="arial 12 bold")

#First Row of Buttons
btn_9 = tk.Button(text="9", width=10, background=BG, font="arial 9 bold", textvariable=nine, command=lambda:build(nine))
btn_8 = tk.Button(text="8", width=10, background=BG, font="arial 9 bold", textvariable=eight, command=lambda:build(eight))
btn_7 = tk.Button(text="7", width=10, background=BG, font="arial 9 bold", textvariable=seven, command=lambda:build(seven))
btn_plus = tk.Button(text="+", width=10, background="orange red", font="arial 9 bold", textvariable=plus, command=lambda:calc(plus))
#Second Row of Buttons
btn_6 = tk.Button(text="6", width=10, background=BG, font="arial 9 bold", textvariable=six, command=lambda:build(six))
btn_5 = tk.Button(text="5", width=10, background=BG, font="arial 9 bold", textvariable=five, command=lambda:build(five))
btn_4 = tk.Button(text="4", width=10, background=BG, font="arial 9 bold", textvariable=four, command=lambda:build(four))
btn_minus = tk.Button(text="-", width=10, background="DarkOrange1", font="arial 9 bold", textvariable=minus, command=lambda:calc(minus))
#Third Row of Buttons
btn_3 = tk.Button(text="3", width=10, background=BG, font="arial 9 bold", textvariable=three, command=lambda:build(three))
btn_2 = tk.Button(text="2", width=10, background=BG, font="arial 9 bold", textvariable=two, command=lambda:build(two))
btn_1 = tk.Button(text="1", width=10, background=BG, font="arial 9 bold", textvariable=one, command=lambda:build(one))
btn_multiply = tk.Button(text="*", width=10, background="chartreuse3", font="arial 9 bold", textvariable=multiply, command=lambda:calc(multiply))
#Fourth Row of Buttons
btn_0 = tk.Button(text="0", width=10, background=BG, font="arial 9 bold", textvariable=zero, command=lambda:build(zero))
btn_dot = tk.Button(text=".", width=10, background=BG, font="arial 9 bold", textvariable=dot, command=lambda:build(dot))
btn_equals = tk.Button(text="=", width=10, background=BG, font="arial 9 bold", command=lambda:calc(equals))
btn_divide = tk.Button(text="/", width=10, background="medium orchid", font="arial 9 bold", textvariable=divide, command=lambda:calc(divide))

lb_equation.grid(row=0, column=0, columnspan=4, pady=(15,0))
btn_clear.grid(row=1, column=3, padx=5, pady=(5,20))
txt_main.grid(row=1, column=0, columnspan=3, pady=(5,20))
btn_9.grid(row=2, column=2, padx=5, pady=5)
btn_8.grid(row=2, column=1, padx=5)
btn_7.grid(row=2, column=0, padx=5)
btn_plus.grid(row=2, column=3, padx=5)

btn_6.grid(row=3, column=2, padx=5, pady=5)
btn_5.grid(row=3, column=1, padx=5)
btn_4.grid(row=3, column=0, padx=5)
btn_minus.grid(row=3, column=3, padx=5)

btn_1.grid(row=4, column=0, padx=5, pady=5)
btn_2.grid(row=4, column=1, padx=5)
btn_3.grid(row=4, column=2, padx=5)
btn_multiply.grid(row=4, column=3, padx=5)

btn_0.grid(row=5, column=0, padx=5, pady=(5,20))
btn_dot.grid(row=5, column=1, padx=5, pady=(5,20))
btn_equals.grid(row=5, column=2, padx=5, pady=(5,20))
btn_divide.grid(row=5, column=3, padx=5, pady=(5,20))

window.bind("<Return>", enter)
window.bind_all('<Key>', keyPressEvent) 

window.mainloop()