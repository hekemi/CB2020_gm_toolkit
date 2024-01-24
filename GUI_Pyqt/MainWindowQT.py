import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from GUI_Pyqt import GUI_PY
from GUI_Pyqt import Roller
from GUI_Pyqt import inventoryManager

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from scripts import diceroller
from scripts import inventory_manager

global retured_name
retured_name = ""


# Чтобы конвертировать .ui в .py используй команду
# pyuic5 C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\GUI_UI.ui -o C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\GUI_PY.py

class RollerWindow(QtWidgets.QMainWindow, Roller.Ui_RollDice):
    def __init__(self):
        super(RollerWindow, self).__init__()
        self.setupUi(self)
        self.BtnRoll.clicked.connect(self.Roll)

    
    def Roll(self):
        text = self.Input.text()
        temp = str(diceroller.dice(text))
        self.Output.setText(temp)

class InventoryManagerWindow(QtWidgets.QMainWindow, inventoryManager.Ui_InventoryManager):
    def __init__(self):
        super(InventoryManagerWindow, self).__init__() 
        self.setupUi(self)
        self.CharacSel.addItems(inventory_manager.names())
        self.Load.clicked.connect(self.return_name)
    
    def return_name(self):
        retured_name = self.CharacSel.currentText()







class MainMenu(QtWidgets.QMainWindow, GUI_PY.Ui_MainWindow):
    def __init__(self):
        super(MainMenu,self).__init__()
        self.setupUi(self) 
        self.init_Roll()
        self.init_Inv()



    def init_Roll(self):
        self.Diceroller.clicked.connect(self.show_roll_window)
    
    def show_roll_window(self):
        self.r = RollerWindow()
        self.r.show()


    def init_Inv(self):
        # НЕ ЗАБЫТЬ ПЕРЕИМЕНОВАТЬ КНОПКУ В GUI_PY!!!!!
        self.InventoryMain.clicked.connect(self.show_inv_window)

    def show_inv_window(self):
        self.i = InventoryManagerWindow()
        self.i.show()





        






def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = MainMenu()  
    window.show()  
    sys.exit(app.exec_())