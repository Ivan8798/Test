from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Тест Руфье')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.text_name = QLabel(txt_name)
        self.text_hintname = QLineEdit(txt_hintname)
        self.text_age = QLabel(txt_age)
        self.text_hintage = QLineEdit(txt_hintage)
        self.text_test1 = QLabel(txt_test1)
        self.start_test1 = QPushButton(txt_starttest1)
        self.text_hinttest1 = QLineEdit(txt_hinttest1)
        self.text_test2 = QLabel(txt_test2)
        self.start_test2 = QPushButton(txt_starttest2)
        self.text_hinttest2 = QLineEdit(txt_hinttest2)
        self.text_test3 = QLabel(txt_test3)
        self.start_test3 = QPushButton(txt_starttest3)
        self.text_hinttest3 = QLineEdit(txt_hinttest3)
        self.text_hinttest3 = QLineEdit(txt_hinttest3)
        self.text_results = QPushButton(txt_sendresults)
        self.text_counter = QLabel('test')
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line.addWidget(self.text_counter, alignment=Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_hintname, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_hintage, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.start_test1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_hinttest1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.start_test2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_hinttest2, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.start_test3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_hinttest3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_hinttest3, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.text_results, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.text_results.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()

        












