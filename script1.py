# Importing the required libraries
from tkinter import *

# Creating a window
window = Tk()

# Function to convert kg to gm, lb, ounce
def kg_conversion():
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.20462
    ounces = float(e1_value.get())*35.274
    t1.delete("1.0", END)
    t1.insert(END,grams)
    t2.delete("1.0", END)
    t2.insert(END,pounds)
    t3.delete("1.0", END)
    t3.insert(END,ounces)

# Button which will convert the input
b1 = Button(window, text='Convert',command=kg_conversion)
b1.grid(row=0,column=2)

# Entry where the user can input the value
e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

# labels to show the repsective weight measures
l1 = Label(window, text="kg")
l1.grid(row=0,column=0)

l2 = Label(window, text="grams")
l2.grid(row=1,column=0)

l3 = Label(window, text="pounds")
l3.grid(row=1,column=1)

l4 = Label(window, text="ounces")
l4.grid(row=1,column=2)

# Text boxes where converted values will be displayed
t1=Text(window,height=1,width=20)
t1.grid(row=2,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=2,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=2,column=2)

# Infinite loop to run the application
window.mainloop()