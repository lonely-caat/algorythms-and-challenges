from tkinter import *

window = Tk()
window.title("Widget positioning")
window.minsize(width=500, height=500)
window.config(padx=100,pady=100)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0, row=0)

#Buttons
def butt_1():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=butt_1)
button.grid(column=1, row=1)


#Buttons
def butt_2():
    print("Do something 2")

#calls action() when pressed
button = Button(text="Click Me", command=butt_2)
button.grid(column=0, row=2)


#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.grid(column=3, row=2)

window.mainloop()
