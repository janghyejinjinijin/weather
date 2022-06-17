from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from PyQt5.QtWidgets import *


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        threadStart = QPushButton("start")
        threadStart.clicked.connect(self.testFor)

        vbox = QVBoxLayout()
        vbox.addWidget(threadStart)

        self.resize(300,300)
        self.setLayout(vbox)

    def testFor(self):
        for i in range(20):
            print(i)
            time.sleep(1)

if __name__ == '__main__':
    app = QGuiApplication
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())