import calendar as c
import tkinter as tk
import tkinter.messagebox
import turtle


root = tk.Tk()
usr_turtle = turtle.Turtle()


#fucntion for button command
def btn_click(usr_choice):

	if usr_choice == "jan":
		tk.messagebox.showinfo("January", c.month(2020, 1))
		for x in range(4):
			usr_turtle.forward(100)
			usr_turtle.right(90)
	elif usr_choice == "feb":
		tk.messagebox.showinfo("Febuary", c.month(2020, 2))
		usr_turtle.forward(100)
		for x in range(4):
			usr_turtle.forward(100)
			usr_turtle.right(90)
	elif usr_choice == "mar":
		tk.messagebox.showinfo("March", c.month(2020, 3))
		usr_turtle.forward(100)
		for x in range(4):
			usr_turtle.forward(100)
			usr_turtle.right(90)
	elif usr_choice == "apr":
		tk.messagebox.showinfo("April", c.month(2020, 4))
		usr_turtle.forward(100)
		for x in range(4):
			usr_turtle.forward(100)
			usr_turtle.right(90)
		usr_turtle.forward(100)
		usr_turtle.right(90)
		usr_turtle.forward(100)
		usr_turtle.right(90)
		usr_turtle.forward(400)
		usr_turtle.left(90)
	elif usr_choice == "may":
		tk.messagebox.showinfo("May", c.month(2020, 5))
		usr_turtle.forward(100)
		for x in range(5):
			usr_turtle.left(90)
			usr_turtle.forward(100)
	elif usr_choice == "jun":
		tk.messagebox.showinfo("June", c.month(2020, 6))
		usr_turtle.forward(100)
		for x in range(4):
			usr_turtle.left(90)
			usr_turtle.forward(100)
	elif usr_choice == "jul":
		tk.messagebox.showinfo("July", c.month(2020, 7))
		usr_turtle.forward(100)
		for x in range(4):
			usr_turtle.left(90)
			usr_turtle.forward(100)
	elif usr_choice == "aug":
		tk.messagebox.showinfo("August", c.month(2020, 8))
		usr_turtle.forward(100)
		for x in range(3):
			usr_turtle.left(90)
			usr_turtle.forward(100)
		usr_turtle.right(90)
		usr_turtle.forward(300)
		usr_turtle.left(90)

	elif usr_choice == "sep":
		tk.messagebox.showinfo("September", c.month(2020, 9))
		usr_turtle.forward(100)
		for x in range(5):
			usr_turtle.left(90)
			usr_turtle.forward(100)

	elif usr_choice == "oct":
		tk.messagebox.showinfo("October", c.month(2020, 10))
		usr_turtle.forward(100)
		for x in range(4):
			usr_turtle.left(90)
			usr_turtle.forward(100)
	elif usr_choice == "nov":
		tk.messagebox.showinfo("November", c.month(2020, 11))
		usr_turtle.forward(100)
		for x in range(4):
			usr_turtle.left(90)
			usr_turtle.forward(100)
	elif usr_choice == "dec":
		tk.messagebox.showinfo("December", c.month(2020, 12))
		usr_turtle.forward(100)
		for x in range(3):
			usr_turtle.left(90)
			usr_turtle.forward(100)


#Creating a buttons
btn_jan = tk.Button(root, width=20, height=10, text=c.month(2020, 1), command= lambda: btn_click("jan"))
btn_feb = tk.Button(root, width=20, height=10, text=c.month(2020, 2), command= lambda: btn_click("feb"))
btn_mar = tk.Button(root, width=20, height=10, text=c.month(2020, 3), command= lambda: btn_click("mar"))
btn_apr = tk.Button(root, width=20, height=10, text=c.month(2020, 4), command= lambda: btn_click("apr"))
btn_may = tk.Button(root, width=20, height=10, text=c.month(2020, 5), command= lambda: btn_click("may"))
btn_jun = tk.Button(root, width=20, height=10, text=c.month(2020, 6), command= lambda: btn_click("jun"))
btn_jul = tk.Button(root, width=20, height=10, text=c.month(2020, 7), command= lambda: btn_click("jul"))
btn_aug = tk.Button(root, width=20, height=10, text=c.month(2020, 8), command= lambda: btn_click("aug"))
btn_sep = tk.Button(root, width=20, height=10, text=c.month(2020, 9), command= lambda: btn_click("sep"))
btn_oct = tk.Button(root, width=20, height=10, text=c.month(2020, 10), command= lambda: btn_click("oct"))
btn_nov = tk.Button(root, width=20, height=10, text=c.month(2020, 11), command= lambda: btn_click("nov"))
btn_dec = tk.Button(root, width=20, height=10, text=c.month(2020, 12), command= lambda: btn_click("dec"))



#Packing(Griding) a button!
btn_jan.grid(row=0, column=0, padx=5, pady=5)
btn_feb.grid(row=0, column=1, padx=5, pady=5)
btn_mar.grid(row=0, column=2, padx=5, pady=5)
btn_apr.grid(row=0, column=3, padx=5, pady=5)

btn_may.grid(row=1, column=0, padx=5, pady=5)
btn_jun.grid(row=1, column=1, padx=5, pady=5)
btn_jul.grid(row=1, column=2, padx=5, pady=5)
btn_aug.grid(row=1, column=3, padx=5, pady=5)

btn_sep.grid(row=2, column=0, padx=5, pady=5)
btn_oct.grid(row=2, column=1, padx=5, pady=5)
btn_nov.grid(row=2, column=2, padx=5, pady=5)
btn_dec.grid(row=2, column=3, padx=5, pady=5)

turtle.done()
root.mainloop()
