from PyQt6.QtWidgets import *
from widgets.regwindow import RegWindow
import sys

if __name__ == '__main__':
  app = QApplication(sys.argv)
  wind = RegWindow()
  

  wind.show()
  app.exec()