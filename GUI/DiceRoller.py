from tkinter import *
from tkinter import ttk



class DiceRoller():
    
    def __init__(self):


        self.dicedice = Tk()     
        self.dicedice.title("DiceRoller")     
        self.dicedice.geometry("350x420")     
        
        
        for c in range(3): self.dicedice.columnconfigure(index=c, weight=1)
        for r in range(3): self.dicedice.rowconfigure(index=r, weight=1)

        title = Label(self.dicedice,text="Roll the dice!")
        title.grid(row=0, column=0,columnspan=3, ipadx=10, ipady=5, padx=0, pady=0)

        example = Label(self.dicedice,text="Example: 6d6 + 5")
        example.grid(row=1, column=0,columnspan=3, ipadx=10, ipady=5, padx=0, pady=0)

        self.task = Text(self.dicedice)
        self.task.grid(row=2, column=0, height=2, width=30)

        start = ttk.Button(self.dicedice,text="Кинуть")
        start.grid(row=2, column=1, ipadx=10, ipady=5,padx=0, pady=0)
        start.bind("<Button-1>", self.dice)

        self.dicedice.mainloop() 

    def dice(*args):
        roll = self.task.get("1.0","end-1c")
        rd = []
        roll = roll.split('d')
        if '+' in roll[1]:
            temp = roll[1].split('+')
            del roll[1]
            for i in temp:
                roll.append(i)
            roll = list(map(int, roll))
            for i in range(roll[0]):
                rd.append(random.randint(1, roll[1]))
            return sum(rd) + roll[2]
        roll = list(map(int, roll))
        for i in range(roll[0]):
            rd.append(random.randint(1, roll[1]))
        return sum(rd)

    


