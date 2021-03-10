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
        self.exist = []

    def story(self, v):
        self.listWidget_2.addItem(v)

    def check(self, button):
        self.sign = button.text()
        self.lineEdit_4.setText(self.sign)

    def encode(self):
        a = self.lineEdit.text()
        x = int(self.spinBox.text())
        numbers = '1234567890ABCDEF'
        let_to_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        true_a = False
        n = 0
        m = 0
        for i in a:
            if i in numbers:
                n += 1
            if i not in numbers and i != '.':
                m += 1
        if len(a) == 0:
            self.lineEdit.setStyleSheet("background-color: red")
            self.label_4.setText('Ничего не введено')
        elif n == len(a):
            self.lineEdit.setStyleSheet("color: black")
            true_a = True
        elif a[0] == '-' and n == len(a) - 1:
            self.lineEdit.setStyleSheet("color: red")
            self.label_4.setText('Отрицательное число')

        elif n < len(a) and m > 0:
            self.lineEdit.setStyleSheet("color: red")
            self.label_4.setText('Не число')
        else:
            self.lineEdit.setStyleSheet("color: red")
            self.label_4.setText('Нецелое число')

        true_b = False
        n = 0
        if true_a:
            for i in a:
                if i in 'ABCDEF':
                    i = let_to_num[i]
                if int(i) < x:
                    n += 1
            if n == len(a):
                true_b = True
            else:
                num_to_sys = {2: 'двоичной', 3: 'троичной', 4: 'четвертичной', 5: 'пятеричной',
                              6: 'шестеричной', 7: 'семиричной', 8: 'восьмеричная', 9: 'девятеричной',
                              10: 'десятичной', 11: 'одиннадцатеричной', 12: 'двенадцатеричной',
                              13: 'тринадцатеричной', 14: 'четырнадцатеричной', 15: 'пятнадцатеричной',
                              16: 'шестнадцатеричной'}
                d = 'Число не принадлежит ' + '\n' + num_to_sys[x] + ' СС'
                self.label_4.setText(d)
                self.lineEdit.setStyleSheet("color: red")

        if true_b:
            a = list(a)
            a.reverse()
            amount = 0
            degree = 0
            for i in a:
                if i in 'ABCDEF':
                    i = let_to_num[i]
                summand = (int(i) * (x ** degree))
                degree += 1
                amount += summand
            y = int(self.spinBox_2.text())
            if y != 10:
                num_to_let = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
                res = []
                while amount >= y:
                    end = amount % y
                    if end >= 10:
                        end = num_to_let[end]
                    amount //= y
                    res.append(str(end))
                res.append(str(amount))
                res.reverse()
                res = ''.join(res)
                self.lineEdit_2.setText(res)
            else:
                self.lineEdit_2.setText(str(amount))

    def explain(self):
        let_to_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        num_to_let = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        k = []
        s = []
        ss = []
        a = self.lineEdit.text()
        x = int(self.spinBox.text())
        a = list(a)
        a.reverse()
        amount = 0
        degree = 0
        k.append('Переводим число в десятичную систему счисления:')
        for i in a:
            d = 'Возводим остнование системы счисления в степень ' + str(degree) + ' и умножаем на ' + str(i) + ':'
            e = str(x) + '^' + str(degree) + ' * ' + str(i) + ' = ' + str((int(i) * (x ** degree)))
            k.append(d)
            k.append(e)
            if i in 'ABCDEF':
                i = let_to_num[i]
            summand = (int(i) * (x ** degree))
            degree += 1
            amount += summand
            s.append(summand)
            ss.append(str(summand))
        k.append('Складываем полученные числа:')
        d = ' + '.join(ss)
        d += ' = '
        d += str(sum(s))
        k.append(d)
        for i in k:
            print(i)

        y = int(self.spinBox_2.text())
        if y != 10:
            num_to_let = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            res = []
            while amount >= y:
                end = amount % y
                if end >= 10:
                    end = num_to_let[end]
                amount //= y
                res.append(str(end))
            res.append(str(amount))
            res.reverse()
            res = ''.join(res)
            self.lineEdit_2.setText(res)

    def calculate(self):
        a = self.lineEdit_3.text()
        x = int(self.spinBox_3.text())
        numbers = '1234567890ABCDEF'
        let_to_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
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
            self.label_6.setText('Ничего не введено')
        elif n == len(a):
            self.lineEdit_3.setStyleSheet("color: black")
            true_a = True
        elif a[0] == '-' and n == len(a) - 1:
            self.lineEdit_3.setStyleSheet("color: red")
            self.label_6.setText('Отрицательное число')

        elif n < len(a) and m > 0:
            self.lineEdit_3.setStyleSheet("color: red")
            self.label_6.setText('Не число')
        else:
            self.lineEdit_3.setStyleSheet("color: red")
            self.label_6.setText('Нецелое число')

        b = self.lineEdit_5.text()
        y = int(self.spinBox_4.text())
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
            self.label_7.setText('Ничего не введено')
        elif n == len(b):
            self.lineEdit_5.setStyleSheet("color: black")
            true_b = True
        elif b[0] == '-' and n == len(b) - 1:
            self.lineEdit_5.setStyleSheet("color: red")
            self.label_7.setText('Отрицательное число')
        elif n < len(b) and m > 0:
            self.lineEdit_5.setStyleSheet("color: red")
            self.label_7.setText('Не число')
        else:
            self.lineEdit_5.setStyleSheet("color: red")
            self.label_7.setText('Нецелое число')

        true_c = False
        true_d = False

        num_to_sys = {2: 'двоичной', 3: 'троичной', 4: 'четвертичной', 5: 'пятеричной',
                      6: 'шестеричной', 7: 'семиричной', 8: 'восьмеричная', 9: 'девятеричной',
                      10: 'десятичной', 11: 'одиннадцатеричной', 12: 'двенадцатеричной',
                      13: 'тринадцатеричной', 14: 'четырнадцатеричной', 15: 'пятнадцатеричной',
                      16: 'шестнадцатеричной'}
        n = 0
        if true_a:
            for i in a:
                if i in 'ABCDEF':
                    i = let_to_num[i]
                if int(i) < x:
                    n += 1
            if n == len(a):
                true_c = True
            else:
                d = 'Число не принадлежит ' + '\n' + num_to_sys[x] + ' СС'
                print(d)
                self.lineEdit_3.setStyleSheet("color: red")
                self.label_6.setText(d)
        n = 0
        if true_b:
            for i in b:
                if i in 'ABCDEF':
                    i = let_to_num[i]
                if int(i) < x:
                    n += 1
            if n == len(b):
                true_d = True
            else:
                d = 'Число не принадлежит ' + '\n' + num_to_sys[x] + ' СС'
                print(d)
                self.lineEdit_5.setStyleSheet("color: red")
                self.label_7.setText(d)

        if true_c and true_d:
            a = list(a)
            a.reverse()
            degree = 0
            amount_a = 0
            for i in a:
                summand = int(i) * (x ** degree)
                amount_a += summand
                degree += 1
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
                    self.label_7.setText('Нельзя делить на 0')
                else:
                    self.lineEdit_5.setStyleSheet("color: red")
                    value = 'error'
            self.lineEdit_6.setText(str(value))
            v = ''.join(a) + '(' + str(x) + ') ' + self.sign + ' ' + ''.join(b) + '(' + str(y) + ') = ' + str(value)
            if v not in self.exist:
                self.story(v)
                self.exist.append(v)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
