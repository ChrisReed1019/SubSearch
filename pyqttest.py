from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

app = QApplication([])
textbox = QLineEdit()
textbox.show()
button = QPushButton('Click')
def on_button_clicked():
    label = QLabel()
    label.text = textbox.text
    label.show()
button.clicked.connect(on_button_clicked)

app.exec()