import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Системы счисления.ui', self)
        self.pushButton.clicked.connect(self.encode)
        self.pushButton_2.clicked.connect(self.explain)
        self.pushButton_3.clicked.connect(self.calculate)
        self.buttonGroup.buttonClicked.connect(self.check)
        self.sign = '+'

    def check(self, button):
        self.sign = button.text()
        print(self.sign)

    def encode(self):
        pass

    def explain(self):
        pass

    def calculate(self):
        numbers = '1234567890'
        a = self.lineEdit_3.text()
        true_a = False
        n = 0
        m = 0
        for i in a:
            if i in numbers:
                n += 1
            if i not in numbers and i != '.':
                m += 1
        if len(a) == 0:
            self.lineEdit_3.setStyleSheet("background-color: red")
            print('Вы ничего не ввели')
        elif n == len(a):
            if int(a) < 0:
                self.lineEdit_3.setStyleSheet("color: red")
                print('Вы ввели отриательное число')
            else:
                self.lineEdit_3.setStyleSheet("color: black")
                true_a = True
        elif n < len(a) and m > 0:
            self.lineEdit_3.setStyleSheet("color: red")
            print('Вы ввели не число')
        else:
            self.lineEdit_3.setStyleSheet("color: red")
            print('Вы ввели нецелое число')

        b = self.lineEdit_5.text()
        true_b = False
        n = 0
        m = 0
        for i in b:
            if i in numbers:
                n += 1
            if i not in numbers and i != '.':
                m += 1
        if len(b) == 0:
            self.lineEdit_5.setStyleSheet("background-color: red")
            print('Вы ничего не ввели')
        elif n == len(b):
            if int(b) < 0:
                self.lineEdit_5.setStyleSheet("color: red")
                print('Вы ввели отриательное число')
            else:
                self.lineEdit_5.setStyleSheet("color: black")
                true_b = True
        elif n < len(b) and m > 0:
            self.lineEdit_5.setStyleSheet("color: red")
            print('Вы ввели не число')
        else:
            self.lineEdit_5.setStyleSheet("color: red")
            print('Вы ввели нецелое число')

        if true_a and true_b:
            x = int(self.spinBox_3.text())
            a = list(a)
            a.reverse()
            degree = 0
            amount_a = 0
            for i in a:
                summand = int(i) * (x ** degree)
                amount_a += summand
                degree += 1
            y = int(self.spinBox_4.text())
            b = list(b)
            b.reverse()
            degree = 0
            amount_b = 0
            for i in b:
                summand = int(i) * (y ** degree)
                amount_b += summand
                degree += 1
            if self.sign == '+':
                value = amount_a + amount_b
            elif self.sign == '-':
                value = amount_a - amount_b
            elif self.sign == '*':
                value = amount_a * amount_b
            elif self.sign == '/':
                if amount_b != 0:
                    value = amount_a / amount_b
                    value = round(value)
                    print('Делитель не может быть равен 0')
                else:
                    self.lineEdit_5.setStyleSheet("color: red")
                    value = 'error'
            self.lineEdit_6.setText(str(value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
