from tkinter import *

window = Tk()
window.title("Widget positioning")
window.minsize(width=500, height=500)
window.config(padx=100,pady=100)

#Entries


#Labels
label = Label(text="0")
label.grid(column=3, row=3)


entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Miles")
entry.grid(column=0, row=0)



#Buttons
def calculate_miles_to_km():

    # Gets text in entry
    miles = (entry.get())

    km = int(miles) * 1.6
    label.config(text=km)


#calls action() when pressed
button = Button(text="Calculate", command=calculate_miles_to_km)
button.grid(column=1, row=1)

window.mainloop()
