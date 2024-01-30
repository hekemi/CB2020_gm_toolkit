import os
import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from GUI_Pyqt import GUI_PY
from GUI_Pyqt import Roller
from GUI_Pyqt import inventoryManager

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from scripts import diceroller
from scripts import inventory_manager
from data.database_metods import * 

global returned_name
returned_name = "start"
sel_char = None

# Чтобы конвертировать .ui в .py используй команду
# pyuic5 C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\GUI_UI.ui -o C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\GUI_PY.py
# pyuic5 C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\inventoryManager.ui -o C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\inventoryManager.py


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
        self.Load.clicked.connect(self.get_character)
       
    def get_character(self):
        returned_name = self.CharacSel.currentText()
        sel_char = extract_stats(returned_name)
        
        # Вывод роли
        char_info = sel_char["Info"]
        self.Role.setText(str(show_info(char_info,"Role")))

        # Отрисовка СТАТов персонажа и присваивание им переменных для дальнейшей работы с ними
        all_stats = sel_char["Stats"]
        int_STAT = int(show_stat(all_stats, "INT"))
        self.INT.setText(str(show_stat(all_stats, "INT")))

        ref_STAT = int(show_stat(all_stats,"REF"))
        self.REF.setText(str(show_stat(all_stats,"REF")))

        tech_STAT = int(show_stat(all_stats,"TECH"))
        self.TECH.setText(str(show_stat(all_stats,"TECH")))

        cool_STAT = int(show_stat(all_stats,"COOL"))
        self.COOL.setText(str(show_stat(all_stats,"COOL")))

        char_STAT = int(show_stat(all_stats,"CHAR"))
        self.CHAR.setText(str(show_stat(all_stats,"CHAR")))

        luck_STAT = int(show_stat(all_stats,"LUCK"))
        self.LUCK.setText(str(show_stat(all_stats,"LUCK")))

        move_STAT = int(show_stat(all_stats,"MOVE"))
        self.MOV.setText(str(show_stat(all_stats,"MOVE")))

        body_STAT = int(show_stat(all_stats,"BODY"))
        self.BODY.setText(str(show_stat(all_stats,"BODY")))

        emp_STAT = int(show_stat(all_stats,"EMP"))
        self.EMP.setText(str(show_stat(all_stats,"EMP")))

        run_STAT = move_STAT
        self.RUN.setText(str(run_STAT))

        jump_STAT = move_STAT + body_STAT
        self.JUMP.setText(str(jump_STAT))

        pick_STAT = move_STAT + body_STAT
        self.PICK.setText(str(pick_STAT))

        carry_STAT = body_STAT // 2
        self.CARRY.setText(str(carry_STAT))

        save_STAT = int(body_STAT)
        self.SAVE.setText(str(save_STAT))


        if body_STAT <= 2:
            mbod_STAT = 0
        elif body_STAT > 2 and body_STAT <= 4:
            mbod_STAT = 1
        elif body_STAT > 4 and body_STAT <= 7:
            mbod_STAT = 2
        elif body_STAT > 7 and body_STAT <= 9:
            mbod_STAT = 3
        elif body_STAT == 10:
            mbod_STAT = 4
        elif body_STAT > 10:
            mbod_STAT = 5
        self.MBOD.setText(str(mbod_STAT))



        
    
    





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

    