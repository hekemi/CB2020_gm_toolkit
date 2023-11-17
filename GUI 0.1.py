from tkinter import *
from tkinter import ttk



root = Tk()     
root.title("CyberPunk 2020 GM's toolkit v 0.1")     
root.geometry("350x420")

root.resizable(True, True)

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(4): root.rowconfigure(index=r, weight=1)

title = Label(text="Welcome to CyberPunk 2020 GM's toolkit v 0.1")
title.grid(row=0, column=0,columnspan=3, ipadx=10, ipady=5, padx=0, pady=0)

InventoryManager = ttk.Button(text="Инвентарь")
InventoryManager.grid(row=1, column=0, ipadx=10, ipady=5, padx=0, pady=0)

DiceRoller = ttk.Button(text="Роллер")
DiceRoller.grid(row=1,column=1,ipadx=10, ipady=5, padx=0, pady=0)

FastCharSystem = ttk.Button(text="Генератор NPC")
FastCharSystem.grid(row=1,column=2,ipadx=10, ipady=5, padx=0, pady=0)

FightClub = ttk.Button(text="Бой")
FightClub.grid(row=2,column=0,ipadx=10, ipady=5, padx=0, pady=0)

Shop = ttk.Button(text="Магазин")
Shop.grid(row=2,column=1,ipadx=10, ipady=5, padx=0, pady=0)

DataForts = ttk.Button(text="ДатаФорт")
DataForts.grid(row=2,column=2,ipadx=10, ipady=5, padx=0, pady=0)

DrugLab = ttk.Button(text="Лаборатория")
DrugLab.grid(row=3,column=0,ipadx=10, ipady=5, padx=0, pady=0)

Cyber = ttk.Button(text="Кибернетика")
Cyber.grid(row=3,column=1,ipadx=10, ipady=5, padx=0, pady=0)

root.mainloop()