import sys
from PyQt5.QtGui import  QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit,  QComboBox

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)
from hw2_1_1 import hw2_1_1
from hw2_2_1 import hw2_2_1
from hw2_3_1 import hw2_3_1,hw2_3_2

class Cv2019_Hw2(QWidget):

    def __init__(self):
        super(Cv2019_Hw2,self).__init__()

        self.initUI()


    def initUI(self):
        self.createGridGroupBox()


        qbtn_ok = QPushButton("OK")
        qbtn_cancel = QPushButton("Cancel")

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.vGroupBox1,0,0,2,2)
        mainLayout.addWidget(self.vGroupBox3,0,2,3,2)
        mainLayout.addWidget(self.vGroupBox2,2,0,1,2)
        mainLayout.addWidget(qbtn_ok,3,2)
        mainLayout.addWidget(qbtn_cancel,3,3)
        self.setLayout(mainLayout)



    def createGridGroupBox(self):
        self.vGroupBox1 = QGroupBox("1. Stereo")
        self.vGroupBox2 = QGroupBox("2. Normalized Creoss Correlation")
        self.vGroupBox3 = QGroupBox("3. SIFT")

        qbtn1_1 = QPushButton('1.1 Disparity', self)
        qbtn1_1.clicked.connect(hw2_1_1)  
        qbtn2_1 = QPushButton('2.1 NCC', self)
        qbtn2_1.clicked.connect(hw2_2_1)  

        qbtn3_1 = QPushButton('3.1 Keypoints', self)
        qbtn3_1.clicked.connect(hw2_3_1)  

        qbtn3_2 = QPushButton('3.2 Matched keypoints', self)
        qbtn3_2.clicked.connect(hw2_3_2)  


        layout1 = QVBoxLayout() 
        layout2 = QVBoxLayout() 
        layout3 = QVBoxLayout() 

        layout2.addWidget(qbtn2_1)
        layout1.addWidget(qbtn1_1)
        layout3.addWidget(qbtn3_1)
        layout3.addWidget(qbtn3_2)

        self.vGroupBox2.setLayout(layout2)
        self.vGroupBox1.setLayout(layout1)
        self.vGroupBox3.setLayout(layout3)
        self.setWindowTitle('Cv2019_Hw2')




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Cv2019_Hw2()
    ex.show()
    sys.exit(app.exec_())