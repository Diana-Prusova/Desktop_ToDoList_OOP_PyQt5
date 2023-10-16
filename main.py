from PyQt5 import QtWidgets, QtCore
from math import ceil
import sys
import json
import upozorneni
import neni_ulozeno



class ToDoList(QtWidgets.QMainWindow):
    """
    Aplikace To do list umožňuje uživateli zapisovat si
    a ukládat úkoly. Umožňnuje také označovat, které úkoly
    již splněné. 
    Podfunkce navíc: 
    1. Úkol je možné přidat také klávesou enter.
    2. Okno je možné zavřít kl. zkratkou CTRL+W
    3. Pokud seznam není uložen, aplikace na to uživatele
    před zavřením okna upozorní.
    """

    def __init__(self, **kwargs):
        super(ToDoList, self).__init__(**kwargs)

        self.setWindowTitle("MŮJ SEZNAM ÚKOLŮ")
        self.init_gui()
        self.show()
        self.vypsani_uloz_ukolu()

        self.sum_ukolu = 0
        self.sum_splnenych_ukolu = 0

    def init_gui(self):
        """
        Funkce vytvoří GUI a nastaví základní funkce
        a vzhled.
        """
        # vytvoření GUI
        okno = QtWidgets.QWidget()
        okno_layout = QtWidgets.QVBoxLayout()
        box_input_layout = QtWidgets.QHBoxLayout()
        box_ukoly_layout = QtWidgets.QHBoxLayout()
        box_pocty_ukolu_layout = QtWidgets.QHBoxLayout()
        box_tlacitka_layout = QtWidgets.QHBoxLayout()

        self.setCentralWidget(okno)
        okno.setLayout(okno_layout)
        okno_layout.addLayout(box_input_layout)
        okno_layout.addLayout(box_ukoly_layout)
        okno_layout.addLayout(box_pocty_ukolu_layout)
        okno_layout.addLayout(box_tlacitka_layout)

        self.zapis_ukol_edit = QtWidgets.QLineEdit(self)
        self.novy_ukol_button = QtWidgets.QPushButton("PŘIDAT", self)
        self.seznam_ukolu_widget = QtWidgets.QListWidget()
        self.pocty_ukol_label = QtWidgets.QLabel("počet úkolů: 0 (splněno: 0)", self)
        self.smaz_polozku_button = QtWidgets.QPushButton("SMAŽ POLOŽKU", self)
        self.smaz_list_button = QtWidgets.QPushButton("SMAŽ SEZNAM", self)
        self.uloz_list_button = QtWidgets.QPushButton("ULOŽIT", self)

        box_input_layout.addWidget(self.zapis_ukol_edit)
        box_input_layout.addWidget(self.novy_ukol_button)
        box_ukoly_layout.addWidget(self.seznam_ukolu_widget)
        box_pocty_ukolu_layout.addStretch()
        box_pocty_ukolu_layout.addWidget(self.pocty_ukol_label)
        box_pocty_ukolu_layout.addStretch()
        box_tlacitka_layout.addWidget(self.smaz_polozku_button)
        box_tlacitka_layout.addWidget(self.smaz_list_button)
        box_tlacitka_layout.addWidget(self.uloz_list_button)
    
        # vzhled
        self.zapis_ukol_edit.setPlaceholderText("Zadej úkol...")
        self.seznam_ukolu_widget.setStyleSheet(
                            "QListWidget {" # styl widgetu
                            "font-family: Arial, sans-serif;"
                            "font-size: 17px;"                            
                            "margin-top: 5px;"
                            "}"
                            "QListWidget::item:selected {" # vybraná položka
                            "background : lightgray;"
                            "color: black;"
                            "}"
                            "QListWidget QScrollBar:vertical {" # vertikální lišta pozadí
                            "background: white;"  
                            "width: 10px;" 
                            "border-radius: 5px;"
                            "}"
                            "QListWidget QScrollBar::handle:vertical {" # vertikální lišta posuvník
                            "background: darkgray;"
                            "border-radius: 5px;"
                            "}"
                            "QListWidget QScrollBar::add-line:vertical,"
                            "QListWidget QScrollBar::sub-line:vertical {"
                            "background: white;"  # odstranění horního a dolního tlačítka
                            "}"
                            # "QListWidget QScrollBar:horizontal {" # horizontální lišta pozadí
                            # "background: white;"  
                            # "height: 10px;" 
                            # "border-radius: 5px;"
                            # "}"
                            # "QListWidget QScrollBar::handle:horizontal {" # horizontální lišta posuvník
                            # "background: darkgray;"
                            # "border-radius: 5px;"
                            # "}"
                            # "QListWidget QScrollBar::add-line:horizontal, QListWidget QScrollBar::sub-line:horizontal {"
                            # "background: white;"  # odstraneni levého a pravého tlačítka
                            # "}"
        )
        self.setStyleSheet(
                            "font-family: Arial, sans-serif;"
                            "font-size: 14px;"
        )
        self.pocty_ukol_label.setStyleSheet(                      
                            "margin-top: 10px;"
                            "margin-bottom: 10px;"
        )
        self.seznam_ukolu_widget.setMinimumWidth(400)

        # funkcionalita
        self.novy_ukol_button.clicked.connect(self.novy_ukol)
        self.zapis_ukol_edit.returnPressed.connect(self.novy_ukol)
        self.novy_ukol_button.clicked.connect(self.zapis_ukol_edit.setFocus)
        self.smaz_polozku_button.clicked.connect(self.smazat_polozku)
        self.smaz_list_button.clicked.connect(self.smazat_seznam)
        self.uloz_list_button.clicked.connect(self.uloz_seznam)


    def pridani_ukolu(self, ukol, check=False):
        """
        Funkce přidá zapsaný úkol do widgetu zobrazující
        zapsané úkoly.
        """
        # vytvoření widgetu
        ukol_widget = QtWidgets.QListWidgetItem()
        self.checkbox = QtWidgets.QCheckBox(ukol)

        # přidání obsahu
        self.checkbox.setChecked(check)
        self.seznam_ukolu_widget.insertItem(0, ukol_widget)
        self.seznam_ukolu_widget.setItemWidget(ukol_widget, self.checkbox)
        self.checkbox.stateChanged.connect(self.pocet_ukolu)

        # aktualizace počtu úkolů
        self.pocet_ukolu()


    def novy_ukol(self):
        """
        Po kliknutí na tlačítko "PŘIDAT" fukce zkontroluje, 
        jestli není pole pro získání prázdné a pokud ne,
        pomocí funkce "pridani_ukolu" úkol zapíše a vyčistí
        zadávací pole.
        """
        # získání textu
        ukol = self.zapis_ukol_edit.text()

        #kontrola duplicity
        seznam_ukolu = []
        if ukol != "":
            for index in range(self.seznam_ukolu_widget.count()):
                radek_winget = self.seznam_ukolu_widget.itemWidget(
                                self.seznam_ukolu_widget.item(index)
                                )
                radek = radek_winget.text()
                seznam_ukolu.append(radek)

            # přidání úkolu
            if ukol not in (seznam_ukolu):
                self.pridani_ukolu(ukol)
            # upozornění na duplicitu
            else:
                text = "Tento úkol již máte zaznamenaný."
                self.upozorneni = upozorneni.OknoUpozorneni(text)
                self.upozorneni.show()
            
            self.zapis_ukol_edit.clear()


    def smazat_polozku(self):
        """
        Funkce smaže vybranou položku seznamu.
        """
        vybrany_ukol = self.seznam_ukolu_widget.currentRow()
        self.seznam_ukolu_widget.takeItem(vybrany_ukol)
        self.pocet_ukolu()
        

    def smazat_seznam(self):
        """
        Funkce zavře staré okno To do listu a vytvoří nové.
        """
        self.seznam_ukolu_widget.clear()
        self.pocty_ukol_label.setText("počet úkolů: 0 (splněno: 0)")


    def pocet_ukolu(self):
        """
        Funkce spočítá celkový počet zadaných úkolů
        a splněných úkolů. Výsledné hodnoty zobrazí
        v daném widgetu a případně zobrazí vyskakovací okna:

        GRATULACE: pokud jsou splněny všechny úkoly
        PŘEDPOSLENÍ: motivační okno, které se zobrazí, pokud
            uživateli zbývá splnit už jen jeden úkol.
        POLOVINA: motivační okno, které uživatele informuje
            že už je za polovinou seznamu.
        """
        # spočítání úkolů
        self.sum_ukolu = 0
        self.sum_splnenych_ukolu = 0
        for index in range(self.seznam_ukolu_widget.count()):
            ukol_widget = self.seznam_ukolu_widget.itemWidget(self.seznam_ukolu_widget.item(index))
            if ukol_widget.isChecked():
                self.sum_splnenych_ukolu += 1
            self.sum_ukolu += 1

        # zobrazení výsledku
        self.pocty_ukol_label.setText(f"počet úkolů: {self.sum_ukolu} "
                            f"(splněno: {self.sum_splnenych_ukolu})")

        # zobrazení vyskakovacích oken
        if self.sum_ukolu == self.sum_splnenych_ukolu:
            text = "Vše splněno, GRATULUJI!"
            self.gratulace = upozorneni.OknoUpozorneni(text)
            self.gratulace.show()
        else:
            if self.sum_ukolu > 3:
                if self.sum_splnenych_ukolu == (self.sum_ukolu - 1):
                    text = "Perfektní, zbývá už jen poslední úkol."
                    self.gratulace_posledi = upozorneni.OknoUpozorneni(text)
                    self.gratulace_posledi.show()
            if self.sum_ukolu > 7:
                if (self.sum_splnenych_ukolu > ceil(self.sum_ukolu / 2) and
                    self.sum_splnenych_ukolu < ceil(self.sum_ukolu / 2) + 2): 
                    text = "Už jste za půlkou, WOW!"
                    self.gratulace_pulka = upozorneni.OknoUpozorneni(text)
                    self.gratulace_pulka.show()


    def ukoly_na_dict(self) -> dict:
        """
        Funkce projde zapsané úkoly a vytvoří z nich
        dict, který obsahuje text úkolu jako klíč a jako
        hodnotu informaci o splněnosti úkolu (0 - nesplněno;
        2 - splněno).
        """
        ukoly_dict = dict()
        for index in range(self.seznam_ukolu_widget.count()):
            radek_winget = self.seznam_ukolu_widget.itemWidget(
                                self.seznam_ukolu_widget.item(index)
                                )
            ukol = radek_winget.text()
            check = radek_winget.checkState()
            ukoly_dict[ukol] = check

        return ukoly_dict
    
    
    def uloz_seznam(self):
        """
        Funkce pomocí funkce "ukoly_na_dict()" uloží 
        zadané úkoly do souboru json.
        """
        with open("ulozene_ukoly.json", mode="w", encoding="utf-8") as file:
            json.dump(self.ukoly_na_dict(), file)


    def ziskani_uloz_ukolu(self) -> dict:
        """
        Funkce načte seznam úložených úkolů a vrátí 
        jej ve formátu dict.
        """
        with open("ulozene_ukoly.json", mode="r", encoding="utf-8") as file:
            seznam_ukolu = json.load(file)

        return seznam_ukolu

    def vypsani_uloz_ukolu(self):
        """
        Funkce pomocí funkce "ziskani_uloz_ukolu()" získá
        uložené úkoly a následně je vypíše do příslušného widgetu.
        """
        # procházení seznamu úkolů
        for key, value in (self.ziskani_uloz_ukolu()).items():
            if value == 0:
                check = False
            elif value == 2:
                check = True
                
            # vytvoření prázdného objektu
            ukol_widget = QtWidgets.QListWidgetItem()
            self.checkbox = QtWidgets.QCheckBox(key)

            # přidání získaného úkolu do nového objektu
            self.checkbox.setChecked(check)
            self.seznam_ukolu_widget.insertItem(0, ukol_widget)
            self.seznam_ukolu_widget.setItemWidget(ukol_widget, self.checkbox)
            self.checkbox.stateChanged.connect(self.pocet_ukolu)


    def closeEvent(self, event):
        """
        
        """

        if self.ukoly_na_dict() == self.ziskani_uloz_ukolu():
            event.accept()
        else:
            event.ignore()
            self.pozor_neulozeno = neni_ulozeno.OknoNeniUlozeno()
            self.pozor_neulozeno.show()


    def keyPressEvent(self, event):
        """
        Funkce umožňuje zavřít okno klávesovou zkratkou CTRL+W.
        """
        if event.modifiers() & QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_W:
                self.close()
        else:
            super().keyPressEvent(event)
            


aplikace = QtWidgets.QApplication(sys.argv)
okno = ToDoList()
sys.exit(aplikace.exec_())