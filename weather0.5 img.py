import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/imageTest.ui")[0]

class TestWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.imageButton.clicked.connect(self.outputImage)


    def outputImage(self):
        pic1 = QPixmap("image/rain.png")
        self.image_label.setPixmap(QPixmap(pic1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TestWindow()
    ex.show()
    sys.exit(app.exec_())