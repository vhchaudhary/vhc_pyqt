from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *

from calc import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    expr = ''
    number_display = '0'

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.btn_one.pressed.connect(lambda : self.input_number(1))
        self.btn_two.pressed.connect(lambda: self.input_number(2))
        self.btn_three.pressed.connect(lambda: self.input_number(3))
        self.btn_four.pressed.connect(lambda: self.input_number(4))
        self.btn_five.pressed.connect(lambda: self.input_number(5))
        self.btn_six.pressed.connect(lambda: self.input_number(6))
        self.btn_seven.pressed.connect(lambda: self.input_number(7))
        self.btn_eight.pressed.connect(lambda: self.input_number(8))
        self.btn_nine.pressed.connect(lambda: self.input_number(9))
        self.btn_zero.pressed.connect(lambda: self.input_number(0))
        self.btn_point.pressed.connect(lambda: self.input_number('.'))
        self.btn_clear.pressed.connect(lambda: self.clear())

        self.btn_add.pressed.connect(lambda: self.operation('+'))
        self.btn_sub.pressed.connect(lambda: self.operation('-'))
        self.btn_multi.pressed.connect(lambda: self.operation('*'))
        self.btn_div.pressed.connect(lambda: self.operation('/'))
        self.btn_eq.pressed.connect(lambda: self.operation('='))

        self.display()

        self.show()

    def operation(self, operator):

        if operator == '+':
            if self.number_display[-1] != '+':
                self.number_display += '+'
        elif operator == '-':
            if self.number_display[-1] != '-':
                self.number_display += '-'
        elif operator == '*':
            if self.number_display[-1] != '*':
                self.number_display += '*'
        elif operator == '/':
            if self.number_display[-1] != '/':
                self.number_display += '/'

        elif operator == '=':
            try:
                self.number_display = str(eval(self.txt_result.text()))
            except:
                self.lbl_info.setText("Invalid Expression")

        self.display()


    def input_number(self, number):
        if self.number_display != '0':
            self.number_display += str(number)
        else:
            self.number_display = str(number)
        self.display()

    def display(self):
        self.txt_result.setText(self.number_display)

    def clear(self):
        self.number_display = '0'
        self.lbl_info.setText("")
        self.display()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName('vhc_calc')

    window = MainWindow()
    app.exec()
