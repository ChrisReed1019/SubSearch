from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

app = QApplication([])
layout = QVBoxLayout()
textbox = QLineEdit()
button = QPushButton('Click')
layout.addWidget(textbox)
layout.addWidget(button)
window = QWidget()
window.setLayout(layout)
window.show()

def on_button_clicked():
    label = QLabel()
    label.setText(textbox.text())
    layout.addWidget(label)
button.clicked.connect(on_button_clicked)

app.exec()