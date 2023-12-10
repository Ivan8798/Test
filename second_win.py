from instr import *
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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
        self.text_results = QPushButton(txt_sendresults)
        self.text_timer = QLabel('')
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment=Qt.AlignCenter)
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
        self.l_line.addWidget(self.text_results, alignment=Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.text_results.clicked.connect(self.next_click)
        self.start_test1.clicked.connect(self.timer_test)
        self.start_test2.clicked.connect(self.timer_sits)
        self.start_test3.clicked.connect(self.final_timer)

    def next_click(self):
        self.hide()
        self.exp = Experiment(self.text_hintage.text(), self.text_hinttest1.text(),
                            self.text_hinttest2.text(), self.text_hinttest3.text())
        self.fw = FinalWin(self.exp)

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def final_timer(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")       
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def results(self):
        self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
        if self.exp.age >= 15:
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

        if self.exp.age >= 13 and self.exp.age <= 14:
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

        if self.exp.age >= 11 and self.exp.age <= 12:
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

        if self.exp.age >= 10 and self.exp.age <= 9:
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

        if self.exp.age >= 7 and self.exp.age <= 8:
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

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3






