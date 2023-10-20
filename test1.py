import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from test2 import SubWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hlavní Okno")
        self.setGeometry(100, 100, 400, 200)

        self.button_open_subwindow = QPushButton("Otevři podokno", self)
        self.button_open_subwindow.clicked.connect(self.openSubWindow)

    def openSubWindow(self):
        self.sub_window = SubWindow(self)
        self.sub_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
