from PyQt5.QtWidgets import QMainWindow, QPushButton

class SubWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("První Podokno")
        self.setGeometry(300, 300, 200, 100)
        self.main_window = main_window

        self.button_close_main_window = QPushButton("Zavři hlavní okno", self)
        self.button_close_main_window.clicked.connect(self.closeMainWindow)

    def closeMainWindow(self):
        self.main_window.close()
