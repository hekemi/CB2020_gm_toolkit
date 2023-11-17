from tkinter import *
from tkinter import ttk



root = Tk()     
root.title("Приложение на Tkinter")     
root.geometry("300x250")

root.resizable(True, True)
 
label = Label(text="Hello World") 
label.pack()    
 
root.mainloop()