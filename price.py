import sys
# 시스템 불러오기
from PyQt5 import uic
# 디자인 만든거 불러와야됨
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
#큐티위젯 불러오고
from PyQt5.QtGui import *
#gui 불러오기

import pyupbit
# 업비트 파이썬 일

form_class = uic.loadUiType('ui/coin.ui')[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.requestPrice)

        #self.price_button.clicked.connect(self.requestPrice)


    def requestPrice(self):
        coinPrice = pyupbit.get_current_price(["KRW-BTC","KRW-XRP"])
        print(coinPrice["KRW-XRP"])
        self.price_label.setText(f"{coinPrice['KRW-BTC']:,.0f}원")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())