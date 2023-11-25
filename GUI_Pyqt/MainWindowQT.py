import os
import sys
from PyQt5 import QtWidgets
import GUI_PY
import Roller

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from scripts import diceroller


# Чтобы конвертировать .ui в .py используй команду
# pyuic5 C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\GUI_UI.ui -o C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\GUI_PY.py

class RollerWindow(QtWidgets.QMainWindow, Roller.Ui_RollDice):
    def __init__(self):
        super(RollerWindow, self).__init__()
        self.setupUi(self)


class MainMenu(QtWidgets.QMainWindow, GUI_PY.Ui_MainWindow):
    def __init__(self):
        super(MainMenu,self).__init__()
        self.setupUi(self) 
        self.Diceroller.clicked.connect(self.Roll)
        self.dialog = RollerWindow()
    
    def Roll(self):
        self.dialog.show()


def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = MainMenu()  
    window.show()  
    app.exec_()  
main()


