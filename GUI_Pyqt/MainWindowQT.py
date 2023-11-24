import sys  
from PyQt5 import QtWidgets
import GUI_PY
import Roller
# from ..scripts import diceroller


# Чтобы конвертировать .ui в .py используй команду
# pyuic5 C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\GUI_UI.ui -o C:\CyberPunkProject\CB2020_gm_toolkit\GUI_Pyqt\GUI_PY.py

class MainMenu(QtWidgets.QMainWindow, GUI_PY.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super(MainMenu, self).__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        
    def Menu(self):
        self.menu = MainMenu()
        self.menu.clicked.connect(self.RollerWindow)

    def Roll(self):
        self.roll = RollerWindow()


class RollerWindow(QtWidgets.QMainWindow, Roller.Ui_RollDice):
    def __init__(self):
        super(RollerWindow, self).__init__()
        self.setupUi(self)




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainMenu()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложени
main()


