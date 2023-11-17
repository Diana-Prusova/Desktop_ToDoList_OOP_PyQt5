from PyQt5 import QtWidgets, QtCore, QtGui

class OknoUpozorneni(QtWidgets.QMainWindow):
    """
    Jedná se o vyskakovací okno, se zprávou pro 
    uživatele. Objekt přijíma jeden agrument a to string
    se zprávou, která se má uživateli zobrazit.
    """
    def __init__(self, text, **kwargs):
        super(OknoUpozorneni, self).__init__(**kwargs)

        self.text_upozorneni = text
        self.init_gui()
        self.show()
        

    def init_gui(self):
        """
        Funkce vytvoří GUI a nastaví základní funkce
        a vzhled.
        """
        #vytvoření GUI
        okno = QtWidgets.QWidget()
        okno_layout = QtWidgets.QVBoxLayout()
        box_text_layout = QtWidgets.QHBoxLayout()
        box_info_layout = QtWidgets.QHBoxLayout()

        self.setCentralWidget(okno)
        okno.setLayout(okno_layout)
        okno_layout.addLayout(box_text_layout)
        okno_layout.addLayout(box_info_layout)

        self.text_upozorneni_label = QtWidgets.QLabel(self.text_upozorneni, self)
        self.info_label = QtWidgets.QLabel("Okno lze zavřít křížkem <br>nebo klávesou ENTER.")

        box_text_layout.addWidget(self.text_upozorneni_label)
        box_info_layout.addWidget(self.info_label)

        # vzhled

        self.text_upozorneni_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("font-family: Arial, sans-serif;")
        self.text_upozorneni_label.setStyleSheet("font-size: 17px;")
        self.info_label.setStyleSheet(
                                    "font-size: 11px;"
                                    "color: grey;"
        )
        
    
    def keyPressEvent(self, event):
        """
        Funkce umožňuje zavřít okno kliknutím na 
        klávesu enter.
        """
        if (event.key() == QtCore.Qt.Key_Enter 
            or 
            event.key() == QtCore.Qt.Key_Return):
            self.close()
        else:
            super().keyPressEvent(event)


        