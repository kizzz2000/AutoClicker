import sys
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from action_sets import action_set_1, action_set_2, action_set_3, action_set_4
import pyautogui

ui_file_name = "clicker.ui"
ui_file = QFile(ui_file_name)
if not ui_file.open(QIODevice.ReadOnly):
    print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
    sys.exit(-1)
loader = QUiLoader()
ui_file.close()


class App(QApplication):
    def __init__(self):
        super().__init__()
        self.ui = loader.load(ui_file)
        self.ui.autoclicker.clicked.connect(self.action_set_01)
        # self.ui.action_set_2.clicked.connect(self.action_set_02)
        # self.ui.action_set_3.clicked.connect(self.action_set_03)
        # self.ui.action_set_4.clicked.connect(self.action_set_04)
        self.ui.show()

    def action_set_01(self):
        text = self.ui.lineEdit.text()
        interval=float(text)
        action_set_1(interval)

    # def action_set_02(self):
    #     action_set_2()
    #
    # def action_set_03(self):
    #     action_set_3()
    #
    # def action_set_04(self):
    #     action_set_4()


if __name__ == "__main__":
    app = App()
    sys.exit(app.exec())