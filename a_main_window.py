import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class a_window_main():
 def __init__(self):

   self.window = QWidget()
   self.window.setWindowTitle("PythonPHPJS")
   self.layout = QVBoxLayout()
   self.horizontal = QHBoxLayout()

   self.browser = QWebEngineView()
   self.layout.addLayout(self.horizontal)
   self.layout.addWidget(self.browser)
   self.browser.setUrl(QUrl(os.getcwd().replace("\\", "/") +"/Templates/application/main.htm"))

   self.window.setLayout(self.layout)
   self.window.setFixedSize(1024, 768)
   self.window.show()

app = QApplication([])
window = a_window_main()
app.exec_()
