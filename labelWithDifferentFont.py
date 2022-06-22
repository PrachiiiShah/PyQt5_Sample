# importing the required libraries  

from PyQt5.QtWidgets import *  

from PyQt5.QtGui import *  

import sys  

class Window(QMainWindow):  

    def __init__(self):  

        super().__init__()  

        # set the title  

        self.setWindowTitle("Label")  

        # setting  the geometry of window  

        self.setGeometry(300, 300, 600, 300)  

        # creating a label widget  

        # by default label will display at top left corner  

        self.label_1 = QLabel('Arial font', self)  

        # moving position  

        self.label_1.move(300, 200) 

        # setting font and size  

        self.label_1.setFont(QFont('Arial', 15))  

        # creating a label widget  

        # by default label will display at top left corner  

        self.label_2 = QLabel('Times font', self) 

        # moving position  

        self.label_2.move(100, 200)  

        # setting font and size  

        self.label_2.setFont(QFont('Times', 10)) 

        # show all the widgets  

        self.show()  

# create pyqt5 app  

App = QApplication(sys.argv)  

# create the instance of our Window  

window = Window()  

# start the app  

sys.exit(App.exec())