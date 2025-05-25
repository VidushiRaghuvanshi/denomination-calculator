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
   message= messagebox.showinfo("Alert","Do you want to proceed?")
   if message =="ok":
      topwin()





button = Button(window, text="Let's get started", command=msg)
button.pack()

def topwin():
   top=Toplevel()
   top.geometry("400x400")
   top.config(bg="skyblue")
   top.title("Denomination counter")
   lbl1 = Label(top,text= "Enter the amount", bg="skyblue")
   lbl1.place(x=150,y=50)
   entry1= Entry(top)
   entry1.place(x=140,y=70) 
   lbl2= Label(top,text="Here are the number of notes for each denomination", bg="skyblue")
   lbl2.place(x=70, y=150)
   
   lbl3=Label(top,text="500")
   lbl3.place(x=110,y=180)
   entry2=Entry(top)
   entry2.place(x=150,y=180)
   lbl4=Label(top,text="200")
   lbl4.place(x=110,y=210)
   entry3=Entry(top)
   entry3.place(x=150,y=210)
   lbl5=Label(top,text="100")
   lbl5.place(x=110,y=240)
   entry4=Entry(top)
   entry4.place(x=150,y=240)
   
   def calculate():
      global amount
      amount=int(entry1.get())
      note500=amount//500
      amount%=500
      note200=amount//200
      amount%=200
      note100=amount//100
      amount%=100
      entry2.delete(0,END)
      entry3.delete(0,END)
      entry4.delete(0,END)
      entry2.insert(END,str(note500))
      entry3.insert(END,str(note200))
      entry4.insert(END,str(note100))
      
   btn1= Button(top,text="calculate", bg="green", command=calculate )
   btn1.place(x=170,y=100)


window.mainloop()