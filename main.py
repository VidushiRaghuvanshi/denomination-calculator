from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
window=Tk()
window.geometry("500x500")
window.config(bg="green")
window.title("Denomination Calculator")

upload = Image.open("cash tally.jpeg")
image = ImageTk.PhotoImage(upload)
label = Label(window,image= image)
label.pack()

label2 = Label (window,text= "Welcome to Denomination counter application" , bg="green", fg="white", font=("helvetica", 15))
label2.pack()

def msg():
    messagebox.showinfo("Alert","Do you want to proceed?")


button = Button(window, text="Let's get started", command=msg)
button.pack()


window.mainloop()