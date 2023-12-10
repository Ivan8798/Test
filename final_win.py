from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle('Тест Руфье')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.text_index = QLabel(txt_index)
        self.text_workheart = QLabel(txt_workheart)
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.text_index, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.text_workheart, alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)

