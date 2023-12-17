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
        self.text_workheart = QLabel(txt_workheart + self.results())
        self.text_index = QLabel(txt_index + str(self.index))
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.text_index, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.text_workheart, alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)
        
    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index < 11 and self.index >= 6:
                return txt_res3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res4
            elif self.index <= 0.4:
                return txt_res5

        if int(self.exp.age) >= 13 and int(self.exp.age) <= 14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res2
            elif self.index < 12.4 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            elif self.index <= 1.9:
                return txt_res5

        if int(self.exp.age) >= 11 and int(self.exp.age) <= 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 14 and self.index >= 9:
                return txt_res3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res4
            elif self.index <= 3.4:
                return txt_res5

        if int(self.exp.age) >= 10 and int(self.exp.age) <= 9:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            elif self.index <= 4.9:
                return txt_res5

        if int(self.exp.age) >= 7 and int(self.exp.age) <= 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            elif self.index <= 6.4:
                return txt_res5

