from tkinter import *
from tkinter import ttk



root = Tk()     
root.title("Приложение на Tkinter")     
root.geometry("350x420")

root.resizable(True, True)

label = Label(text="CyberPunk 2020 GM's toolkit v 0.1") 


for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(4): root.rowconfigure(index=r, weight=1)

title = Label(text="Welcome to CyberPunk 2020 GM's toolkit v 0.1")
title.grid(row=0, column=0,columnspan=3, ipadx=10, ipady=5, padx=0, pady=0)

InventoryManager = ttk.Button(text="Инвентарь")
InventoryManager.grid(row=1, column=0, ipadx=10, ipady=5, padx=0, pady=0)

DiceRoller = ttk.Button(text="Роллер")
DiceRoller.grid(row=1,column=1,ipadx=10, ipady=5, padx=0, pady=0)


root.mainloop()