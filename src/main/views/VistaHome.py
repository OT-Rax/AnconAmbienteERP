from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from views.VistaListaOperatori import VistaListaOperatori
from views.VistaListaMezzi import VistaListaMezzi
from views.VistaListaServizi import VistaListaServizi
from views.VistaListaTurni import VistaListaTurni
from views.VistaListaClienti import VistaListaClienti
from views.VistaListaUtenti import VistaListaUtenti
from views.VistaReport import VistaReport

class VistaHome(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaHome, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/home.ui', self)  # Load the .ui file
        self.operatori_button.clicked.connect(self.go_listaoperatori)
        self.mezzi_button.clicked.connect(self.go_listamezzi)
        self.servizi_button.clicked.connect(self.go_listaservizi)
        self.turni_button.clicked.connect(self.go_listaturni)
        self.clienti_button.clicked.connect(self.go_listaclienti)
        self.utenti_button.clicked.connect(self.go_listautenti)
        self.report_button.clicked.connect(self.go_report)

    def go_listaoperatori(self):
        self.vista_listaoperatori=VistaListaOperatori()
        self.vista_listaoperatori.show()

    def go_listamezzi(self):
        self.vista_listamezzi=VistaListaMezzi()
        self.vista_listamezzi.show()

    def go_listaservizi(self):
        self.vista_listaservizi=VistaListaServizi()
        self.vista_listaservizi.show()

    def go_listaturni(self):
        self.vista_listaturni=VistaListaTurni()
        self.vista_listaturni.show()

    def go_listaclienti(self):
        self.vista_listaclienti=VistaListaClienti()
        self.vista_listaclienti.show()

    def go_listautenti(self):
        self.vista_listautenti=VistaListaUtenti()
        self.vista_listautenti.show()

    def go_report(self):
        self.vista_report=VistaReport()
        self.vista_report.show()
