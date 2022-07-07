from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi('tictactoe.ui', self)

        # Turn variable. True - X, False - O
        self.turn = True

        # Widgets definition
        self.button1 = self.findChild(QPushButton, 'pushButton_1')
        self.button2 = self.findChild(QPushButton, 'pushButton_2')
        self.button3 = self.findChild(QPushButton, 'pushButton_3')
        self.button4 = self.findChild(QPushButton, 'pushButton_4')
        self.button5 = self.findChild(QPushButton, 'pushButton_5')
        self.button6 = self.findChild(QPushButton, 'pushButton_6')
        self.button7 = self.findChild(QPushButton, 'pushButton_7')
        self.button8 = self.findChild(QPushButton, 'pushButton_8')
        self.button9 = self.findChild(QPushButton, 'pushButton_9')
        self.button10 = self.findChild(QPushButton, 'pushButton_10')
        self.label = self.findChild(QLabel, 'label')

        # Button clicked
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)

        # Show the app
        self.show()

    # Click handler
    def clicker(self, button):
        if self.turn:
            mark = 'X'
            self.label.setText('O')
        else:
            mark = 'O'
            self.label.setText('X')

        button.setText(mark)
        button.setEnabled(False)
        self.turn = not self.turn

    # Game reset
    def reset(self):
        # Reset the turn variable
        self.turn = True

        # Create a list of all grid buttons
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]

        # Reset the grid buttons
        for b in button_list:
            b.setText('')
            b.setEnabled(True)

        # Reset the labels
        self.label.setText('X')


app = QApplication(sys.argv)
game = UI()
app.exec_()
