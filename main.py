import tkinter as tk
from GUI.MainWindow import MainWindow

 

def main():
    '''Входная точка приложения.'''
    root = tk.Tk()
    
    top1 = root

    MainWindow(top1)

    root.mainloop()


if __name__ == "__main__":
    main()
