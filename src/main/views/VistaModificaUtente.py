from PyQt5 import QtWidgets, uic
import sys
import xz_rc

class VistaModificaUtente(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaModificaUtente, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/modifica_utente.ui', self)  # Load the .ui file