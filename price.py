import sys
# 시스템 불러오기
from PyQt5 import uic
# 디자인 만든거 불러와야됨
from PyQt5.QtWidgets import *
#큐티위젯 불러오고
from PyQt5.QtGui import *
#gui 불러오기

form_class = uic.loadUiType('ui/coinui.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
    # q메인윈도우 상속받기 그 후 폼클래스를 상속받아야 쓸 수 있는 것임
        super().__init__()  # 부모 초기화자 호출 안하면 에러
        self.setUpUi(self)
        self.price_button.clicked.connect(self.requestPrice)


    def requestPrice(self):





    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyWindow()
        ex.show()
        sys.exit(app.exec_())
