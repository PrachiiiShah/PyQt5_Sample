import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   button1 = QPushButton(widget)
   button1.setText("Login")
   button1.move(64,32)
  

   button2 = QPushButton(widget)
   button2.setText("Sign up")
   button2.move(64,64)
  

   widget.setGeometry(100,100,420,200)
   widget.setWindowTitle("Simple Button Example")
   widget.show()
   sys.exit(app.exec_())


  
   
if __name__ == '__main__':
   window()