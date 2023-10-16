from PyQt5 import QtWidgets, QtCore


class OknoNeniUlozeno(QtWidgets.QMainWindow):
    """
    Jedná se o vyskakovací okno, které přijíma jeden 
    argument v podobě stringu, který zobrazuje 
    uživateli jako zprávu.
    """
    def __init__(self, **kwargs):
        super(OknoNeniUlozeno, self).__init__(**kwargs)
        
        self.init_gui()
        self.show()


    def init_gui(self):
        #vytvoření GUI
        okno = QtWidgets.QWidget()
        okno_layout = QtWidgets.QVBoxLayout()
        box_text_layout = QtWidgets.QHBoxLayout()
        box_tlacitka_layout = QtWidgets.QHBoxLayout()

        self.setCentralWidget(okno)
        okno.setLayout(okno_layout)
        okno_layout.addLayout(box_text_layout)
        okno_layout.addLayout(box_tlacitka_layout)

        self.text_upozorneni_label = QtWidgets.QLabel(
                            "SEZNAM ÚKOLŮ NEBYL ULOŽEN."
                            "<br>Chcete seznam uložit?", 
                            self
                            )
        self.ano_button = QtWidgets.QPushButton("ANO", self)
        self.ne_button = QtWidgets.QPushButton("NE", self)

        box_text_layout.addWidget(self.text_upozorneni_label)
        box_tlacitka_layout.addStretch()
        box_tlacitka_layout.addWidget(self.ano_button)
        box_tlacitka_layout.addWidget(self.ne_button)
        box_tlacitka_layout.addStretch()

        # vzhled
        self.text_upozorneni_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("font-family: Arial, sans-serif;")
        self.text_upozorneni_label.setStyleSheet("font-size: 15px;"
                                                 "margin: 15px;")

        # funkcionalita
        self.ne_button.clicked.connect(self.neulozit)
        self.ano_button.clicked.connect(self.ulozit)

    def keyPressEvent(self, event):
        """
        Funkce umožňuje zavřít okno klávesovou zkratkou CTRL+W.
        """
        if event.modifiers() & QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_W:
                self.close()
        else:
            super().keyPressEvent(event)

    def ulozit(self):
        ...


    def neulozit(self):
        ...