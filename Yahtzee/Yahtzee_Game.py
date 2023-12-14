import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox

#CONTSTANTS ---------------------------------------

one = r"./img/one.png"
two = r"./img/two.png"
three = r"./img/three.png"
four = r"./img/four.png"
five = r"./img/five.png"
six = r"./img/six.png"

bgColor = "seashell3"
btn_width = 15

window = tk.Tk()
window.title("YAHTZO!")
window.config(width=800, height=900, padx=40, pady=20, background=bgColor)
w = window.winfo_reqwidth()
h = window.winfo_reqheight()
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('+%d+%d' % (x, y)) ## this part allows you to only change the location


#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img_one = tk.PhotoImage(file=one)
img_two = tk.PhotoImage(file=two)
img_three = tk.PhotoImage(file=three)
img_four = tk.PhotoImage(file=four)
img_five = tk.PhotoImage(file=five)
img_six = tk.PhotoImage(file=six)



#The Button widget is a standard Tkinter widget used to display a text or image on the screen.

btn_one = tk.Button(image=img_one, height=130, width=130, command=lambda x=1:switch(x), background=bgColor)
btn_two = tk.Button(image=img_two, height=130, width=130, command=lambda x=2:switch(x), background=bgColor)
btn_three = tk.Button(image=img_three, height=130, width=130, command=lambda x=3:switch(x), background=bgColor)
btn_four = tk.Button(image=img_four, height=130, width=130, command=lambda x=4:switch(x), background=bgColor)
btn_five = tk.Button(image=img_five, height=130, width=130, command=lambda x=5:switch(x), background=bgColor)


game_board = '''

YAHTZEE - - - - - - Player's Name: {player_name}
SCORE CARD

UPPER SECTION ---------------------------

1. Aces:	   {yahtzee_dict["Aces"]}
2. Twos:	   {yahtzee_dict["Twos"]}
3. Threes: 	   {yahtzee_dict["Threes"]}
4. Fours:  	   {yahtzee_dict["Fours"]}
5. Fives:  	   {yahtzee_dict["Fives"]}
6. Sixes:  	   {yahtzee_dict["Sixes"]}
-----------------------------------------
Total Score:	   {yahtzee_dict["U_Total"]}
BONUS:		   {yahtzee_dict["Bonus"]}
UPPER TOTAL:       {Upper_Total}

LOWER SECTION ---------------------------

7. 3 of a kind:    {yahtzee_dict["T3ofKind"]}
8. 4 of a kind:	   {yahtzee_dict["F4ofKind"]}
9. Full House:	   {yahtzee_dict["FullHouse"]}
10. Sm. Straight:  {yahtzee_dict["smStraight"]}
11. Lg. Straight:  {yahtzee_dict["lgStraight"]}
12. YAHTZEE:	   {yahtzee_dict["Yahtzee"]}
13. Chance:	   {yahtzee_dict["Chance"]}
14. YAHTZEE BONUS: {yahtzee_bonus}
-----------------------------------------
LOWER TOTAL:	{yahtzee_dict["L_Total"]}
UPPER TOTAL:	{yahtzee_dict["U_Total"]}
-----------------------------------------
GRAND TOTAL:	{Grand_Total}

'''

roll_dic = {1:img_one,2:img_two,3:img_three,4:img_four,5:img_five,6:img_six}
count = 0

results = [0,0,0,0,0]
upper = []
lower = []


sm_1 = [1,2,3,4]
sm_2 = [2,3,4,5]
sm_3 = [3,4,5,6]
lrg_1 = [1,2,3,4,5]
lrg_2 = [2,3,4,5,6]

def YAHTZEE():	
	reset()
# be treated as a new window 
	newWindow = tk.Toplevel(window)
	w = window.winfo_reqwidth()
	h = window.winfo_reqheight()
	ws = window.winfo_screenwidth()
	hs = window.winfo_screenheight()
	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)
	newWindow.geometry('+%d+%d' % (x, y)) ## this part allows you to only change the location	
	my_canvas=tk.Canvas(newWindow, height=492, width=400)
	img_yahtzee = tk.PhotoImage(file="img/yahtzee.jpg")
	image=my_canvas.create_image(0,0, anchor='nw',image=img_yahtzee)
	my_canvas.pack(side='top')
	newWindow.mainloop()

def switch(var):
	if var == 1:
		if btn_one['text'] == "":
			btn_one.config(text="Keep", background="orange red")
		else:
			btn_one.config(text="", background=bgColor)
	elif var == 2:		
		if btn_two['text'] == "":
			btn_two.config(text="Keep", background="orange red")
		else:
			btn_two.config(text="", background=bgColor)
	elif var == 3:
		if btn_three['text'] == "":
			btn_three.config(text="Keep", background="orange red")
		else:
			btn_three.config(text="", background=bgColor)
	elif var == 4:
		if btn_four['text'] == "":
			btn_four.config(text="Keep", background="orange red")
		else:
			btn_four.config(text="", background=bgColor)
	elif var == 5:
		if btn_five['text'] == "":
			btn_five.config(text="Keep", background="orange red")
		else:
			btn_five.config(text="", background=bgColor)							

def roll():
	global count

	if count < 3:
		btn_roll.config(text=f"ROLL {count + 1}", background="orange red")
		roll = [random.randint(1,6) for num in range(1,6)]
		#roll = [3, 3, 3, 3, 3]
		print(roll)
		if btn_one['text'] != "Keep":
			btn_one.config(image=roll_dic[roll[0]])
			results[0] = roll[0]
		if btn_two['text'] != "Keep":	
			btn_two.config(image=roll_dic[roll[1]])
			results[1] = roll[1]
		if btn_three['text'] != "Keep":	
			btn_three.config(image=roll_dic[roll[2]])
			results[2] = roll[2]
		if btn_four['text'] != "Keep":	
			btn_four.config(image=roll_dic[roll[3]])
			results[3] = roll[3]
		if btn_five['text'] != "Keep":	
			btn_five.config(image=roll_dic[roll[4]])
			results[4] = roll[4]
	count += 1

def reset():
	global count
	count = 0
	btn_one.config(text="", background=bgColor)	
	btn_two.config(text="", background=bgColor)
	btn_three.config(text="", background=bgColor)
	btn_four.config(text="", background=bgColor)
	btn_five.config(text="", background=bgColor)
	btn_roll.config(text=f"ROLL {count + 1}", background="chartreuse2")

	c_1 = txt_aces.get()
	c_2 = txt_twos.get()
	c_3 = txt_threes.get()
	c_4 = txt_fours.get()
	c_5 = txt_fives.get()
	c_6 = txt_sixes.get()

	c_7 = txt_3ofkind.get()
	c_8 = txt_4ofkind.get()
	c_9 = txt_fullhouse.get()
	c_10 = txt_sm_straight.get()
	c_11 = txt_lg_straight.get()
	c_12 = txt_yahtzee.get()
	c_13 = txt_chance.get()

	if c_1 != "" and c_2 != "" and c_3 != "" and c_4 != "" and c_5 != "" and c_6 != "" and c_7 != "" and c_8 != "" and c_9 != "" and c_10 != "" and c_11 != "" and c_12 != "" and c_13 != "":
		total_val = txt_grand_total.get()
		tk.messagebox.showinfo(title="Game Over", message=f"Congratulations! Your total score was: {total_val}")

def calc(results, btnNum):
	print(results)
	t_one = results.count(1)
	t_two = results.count(2)
	t_three = results.count(3)
	t_four = results.count(4)
	t_five = results.count(5)
	t_six = results.count(6)

	if btnNum == 1:
		if txt_aces.get() == "":
			txt_aces.delete("0", tk.END)
			txt_aces.insert(tk.END, t_one * 1)
			upper.append(t_one * 1)
			reset()
	elif btnNum == 2:		
		if txt_twos.get() == "":
			txt_twos.delete("0", tk.END)
			txt_twos.insert(tk.END, t_two * 2)
			upper.append(t_two * 2)
			reset()
	elif btnNum == 3:
		if txt_threes.get() == "":
			txt_threes.delete("0", tk.END)
			txt_threes.insert(tk.END, t_three * 3)
			upper.append(t_three * 3)
			reset()
	elif btnNum == 4:
		if txt_fours.get() == "":
			txt_fours.delete("0", tk.END)
			txt_fours.insert(tk.END, t_four * 4)
			upper.append(t_four * 4)
			reset()
	elif btnNum == 5:
		if txt_fives.get() == "":
			txt_fives.delete("0", tk.END)
			txt_fives.insert(tk.END, t_five * 5)
			upper.append(t_five * 5)
			reset()
	elif btnNum == 6:
		if txt_sixes.get() == "":
			txt_sixes.delete("0", tk.END)
			txt_sixes.insert(tk.END, t_six * 6)
			upper.append(t_six * 6)
			reset()

	elif btnNum == 7:
		if txt_3ofkind.get() == "":
			txt_3ofkind.delete("0", tk.END)
			if t_one >= 3 or t_two >= 3 or t_three >= 3 or t_four >= 3 or t_five >= 3 or t_six >= 3:
				txt_3ofkind.insert(tk.END, sum(results))
				lower.append(sum(results))
			else:
				txt_3ofkind.insert(tk.END, 0)
				lower.append(0)
			reset()
	elif btnNum == 8:
		if txt_4ofkind.get() == "":
			txt_4ofkind.delete("0", tk.END)
			if t_one >= 4 or t_two >= 4 or t_three >= 4 or t_four >= 4 or t_five >= 4 or t_six >= 4:
				txt_4ofkind.insert(tk.END, sum(results))
				lower.append(sum(results))
			else:
				txt_4ofkind.insert(tk.END, 0)
				lower.append(0)
			reset()
	elif btnNum == 9:
		if txt_fullhouse.get() == "":
			txt_fullhouse.delete("0", tk.END)
			if t_one == 3 or t_two == 3 or t_three == 3 or t_four == 3 or t_five == 3 or t_six == 3:
				if t_one == 2 or t_two == 2 or t_three == 2 or t_four == 2 or t_five == 2 or t_six == 2:
					txt_fullhouse.insert(tk.END, 25)
					lower.append(25)
				else:
					txt_fullhouse.insert(tk.END, 0)
					lower.append(0)
			reset()
	elif btnNum == 10:
		if txt_sm_straight.get() == "":
			txt_sm_straight.delete("0", tk.END)
			if sorted(results[0:4]) == sm_1 or sorted(results[0:4]) == sm_2 or sorted(results[0:4]) == sm_3 or sorted(results[1:5]) == sm_1 or sorted(results[1:5]) == sm_2 or sorted(results[1:5]) == sm_3 or sorted(results[2:6]) == sm_1 or sorted(results[2:6]) == sm_2 or sorted(results[2:6]) == sm_3:
				txt_sm_straight.insert(tk.END, 30)
				lower.append(30)
			else:
				txt_sm_straight.insert(tk.END, 0)
				lower.append(0)
			reset()
	elif btnNum == 11:
		if txt_lg_straight.get() == "":
			txt_lg_straight.delete("0", tk.END)
			if sorted(results) == lrg_1 or sorted(results) == lrg_2:
				txt_lg_straight.insert(tk.END, 40)
				lower.append(40)
			else:
				txt_lg_straight.insert(tk.END, 0)
				lower.append(0)
			reset()
	elif btnNum == 12:
		if txt_yahtzee.get() == "":
			txt_yahtzee.delete("0", tk.END)
			if t_one == 5 or t_two == 5 or t_three == 5 or t_four == 5 or t_five == 5 or t_six == 5:
				txt_yahtzee.insert(tk.END, 50)
				lower.append(50)
				btn_yahtzee_bonus.grid(row=8, column=2)
				txt_yahtzee_bonus.grid(row=8, column=3)	
				YAHTZEE()
			else:
				txt_yahtzee.insert(tk.END, 0)
				lower.append(0)
				reset()
	elif btnNum == 13:
		if txt_chance.get() == "":
			txt_chance.delete("0", tk.END)
			txt_chance.insert(tk.END, sum(results))
			lower.append(sum(results))
			reset()
	elif btnNum == 14:
		if txt_yahtzee.get() == "50":
			if t_one == 5 or t_two == 5 or t_three == 5 or t_four == 5 or t_five == 5 or t_six == 5:
				if txt_yahtzee_bonus.get() == "":
					var = 0
				else:
					var = int(txt_yahtzee_bonus.get())
					txt_yahtzee_bonus.delete("0", tk.END)
				txt_yahtzee_bonus.insert(tk.END, var + 100)
				lower.append(100)
			else:
				txt_yahtzee_bonus.insert(tk.END, 0)
				lower.append(0)
			reset()
	
	print(upper)
	print(lower)

	txt_total.delete("0", tk.END)
	txt_bonus.delete("0", tk.END)
	txt_upper_total.delete("0", tk.END)
	txt_lower_total.delete("0", tk.END)
	txt_grand_total.delete("0", tk.END)

	txt_total.insert(tk.END, sum(upper))
	if sum(upper) >= 63:
		txt_bonus.insert(tk.END, 35)
	else:
		txt_bonus.insert(tk.END, 0)
	txt_upper_total.insert(tk.END, sum(upper) + int(txt_bonus.get()))
	txt_lower_total.insert(tk.END, sum(lower))
	txt_grand_total.insert(tk.END, sum(upper) + sum(lower) + int(txt_bonus.get()))		

btn_aces = tk.Button(text="Ones:", width=btn_width, pady=10, command=lambda:calc(results, 1), background=bgColor)
btn_twos = tk.Button(text="Twos:", width=btn_width, pady=10, command=lambda:calc(results, 2), background=bgColor)
btn_threes = tk.Button(text="Threes:", width=btn_width, pady=10, command=lambda:calc(results, 3), background=bgColor)
btn_fours = tk.Button(text="Fours:", width=btn_width, pady=10, command=lambda:calc(results, 4), background=bgColor)
btn_fives = tk.Button(text="Fives:", width=btn_width, pady=10, command=lambda:calc(results, 5), background=bgColor)
btn_sixes = tk.Button(text="Sixes:", width=btn_width, pady=10, command=lambda:calc(results, 6), background=bgColor)

lb_total = tk.Label(text="Total Score:", font="arial 10 bold", width=btn_width, pady=10, background=bgColor)
lb_bonus = tk.Label(text="Bonus:", width=btn_width, font="arial 10 bold", pady=10, background=bgColor)
lb_upper_total = tk.Label(text="UPPER TOTAL:", width=btn_width, font="arial 12 bold", pady=10, background=bgColor)

btn_3ofkind = tk.Button(text="3 of a Kind:", width=btn_width, pady=10, command=lambda:calc(results, 7), background=bgColor)
btn_4ofkind = tk.Button(text="4 of a Kind:", width=btn_width, pady=10, command=lambda:calc(results, 8), background=bgColor)
btn_fullhouse = tk.Button(text="Full House:", width=btn_width, pady=10, command=lambda:calc(results, 9), background=bgColor)
btn_sm_straight = tk.Button(text="Sm. Straight:", width=btn_width, pady=10, command=lambda:calc(results, 10), background=bgColor)
btn_lg_straight = tk.Button(text="Lg. Straight:", width=btn_width, pady=10, command=lambda:calc(results, 11), background=bgColor)
btn_yahtzee = tk.Button(text="YAHTZEE:", width=btn_width, pady=10, command=lambda:calc(results, 12), background=bgColor)
btn_chance = tk.Button(text="Chance:", width=btn_width, pady=10, command=lambda:calc(results, 13), background=bgColor)
btn_yahtzee_bonus = tk.Button(text="YAHTZEE Bonus:", width=btn_width, pady=10, command=lambda:calc(results, 14), background=bgColor)

lb_lower_total = tk.Label(text="LOWER TOTAL:", width=btn_width, font="arial 12 bold", pady=10, background=bgColor)
lb_grand_total = tk.Label(text="GRAND TOTAL:", width=btn_width, font="arial 14 bold", pady=10, background=bgColor)


txt_aces = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_twos = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_threes = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_fours = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_fives = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_sixes = tk.Entry(width=10, font="arial 10 bold", justify='center')

txt_total = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_bonus = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_u_total = tk.Entry(width=10, font="arial 10 bold", justify='center')

txt_3ofkind = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_4ofkind = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_fullhouse = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_sm_straight = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_lg_straight = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_yahtzee = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_chance = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_yahtzee_bonus = tk.Entry(width=10, font="arial 10 bold", justify='center')

txt_lower_total = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_upper_total = tk.Entry(width=10, font="arial 10 bold", justify='center')
txt_grand_total = tk.Entry(width=10, font="arial 16 bold", justify='center')


btn_one.grid(row=0, column=0, padx=20, pady=50)
btn_two.grid(row=0, column=1, padx=20)
btn_three.grid(row=0, column=2, padx=20)
btn_four.grid(row=0, column=3, padx=20)
btn_five.grid(row=0, column=4, padx=20)


btn_aces.grid(row=1, column=0, pady=5)
btn_twos.grid(row=2, column=0, pady=5)
btn_threes.grid(row=3, column=0, pady=5)
btn_fours.grid(row=4, column=0, pady=5)
btn_fives.grid(row=5, column=0, pady=5)
btn_sixes.grid(row=6, column=0, pady=5)
lb_total.grid(row=7, column=0, pady=5)
lb_bonus.grid(row=8, column=0, pady=5)

btn_3ofkind.grid(row=1, column=2)
btn_4ofkind.grid(row=2, column=2)
btn_fullhouse.grid(row=3, column=2)
btn_sm_straight.grid(row=4, column=2)
btn_lg_straight.grid(row=5, column=2)
btn_yahtzee.grid(row=6, column=2)
btn_chance.grid(row=7, column=2)

lb_lower_total.grid(row=10, column=2)
lb_upper_total.grid(row=10, column=0)
lb_grand_total.grid(row=20, column=0)

txt_aces.grid(row=1, column=1, padx=10)
txt_twos.grid(row=2, column=1)
txt_threes.grid(row=3, column=1)
txt_fours.grid(row=4, column=1)
txt_fives.grid(row=5, column=1)
txt_sixes.grid(row=6, column=1)
txt_total.grid(row=7, column=1)
txt_bonus.grid(row=8, column=1)

txt_3ofkind.grid(row=1, column=3, padx=10)
txt_4ofkind.grid(row=2, column=3)
txt_fullhouse.grid(row=3, column=3)
txt_sm_straight.grid(row=4, column=3)
txt_lg_straight.grid(row=5, column=3)
txt_yahtzee.grid(row=6, column=3)
txt_chance.grid(row=7, column=3)

txt_lower_total.grid(row=10, column=3)
txt_upper_total.grid(row=10, column=1)
txt_grand_total.grid(row=20, column=1, pady=50)


btn_roll = tk.Button(text="START", width=10, font="arial 16 bold", justify='center', command=roll, background="chartreuse2")
btn_roll.grid(row=20, column=3, columnspan=3)

window.mainloop()
