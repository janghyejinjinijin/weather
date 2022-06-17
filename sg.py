import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class SignalThread(QThread):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        self.signal1.emit() #방출하다
        self.signal2.emit(100,200) #인티저타입 인수 두개 필요




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() #초기화자


        signalThr = SignalThread() #시그널스레드생성 //객체에 연결

        signalThr.signal1.connect(self.signal1_print) #연결
        signalThr.signal2.connect(self.signal2_print) #연결
        signalThr.run()# 실행 호출 1

    @pyqtSlot()  # 데코레이터 어노테이션이랑 비슷한거임 빈슬롯이라는 뜻
    def signal1_print(self):
        print("signal1 emit!!")

    #시그널투는 인수가 두개필요함
    @pyqtSlot(int,int)  # 데코레이터 어노테이션이랑 비슷한거임 인수두개가 필요한 슬롯이라는 ㄷ뜻
    def signal2_print(self, arg1, arg2):
        print("signal2 emit!!", arg1, arg2)
#무한루프
app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
