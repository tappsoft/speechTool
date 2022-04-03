from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ui,sys,os,sr
from pynput.keyboard import Key, Controller
import qtawesome as qta
keyboard = Controller()
class spthread(QThread):
    text=pyqtSignal(dict)
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def run(self):
        text = sr.rec()
        if(not text):
            self.text.emit({"text":"","success":False})
        else:
            self.text.emit({"text":text,"success":True})
        

class SpeechWindow(QMainWindow,ui.Ui_MainWindow):
    def __init__(self,parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.exitbtn.setText("")
        self.exitbtn.setIcon(qta.icon("mdi.close-circle",color="black"))
        self.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        point=QApplication.desktop().screen().rect().center()-self.rect().center()
        point=QPoint(point.x(),point.y()+point.y()/10*8)
        self.move(point)
        self.btn.clicked.connect(self.record)
        self.sp=spthread()
        self.sp.text.connect(self.showtext)

    def record(self):
        self.btn.setDisabled(True)
        self.sp.start()
        self.label.setText("正在录音...")
        
    def showtext(self,text):
        if(text["success"]):
            self.label.setText(f"结果：{text['text']}")
            keyboard.type(text['text'])
        else:
            self.label.setText(f"[识别失败]")
        self.btn.setDisabled(False)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=SpeechWindow()
    win.show()
    sys.exit(app.exec_())