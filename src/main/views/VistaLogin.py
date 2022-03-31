from PyQt5 import QtWidgets, uic
import sys
import xz_rc

from views.VistaHome import VistaHome

class VistaLogin(QtWidgets.QMainWindow):
    def __init__(self):
        super(VistaLogin, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('gui/login.ui', self)  # Load the .ui file
        self.login_button.clicked.connect(self.go_home)

    def go_home(self):
        self.vista_home=VistaHome()
        self.vista_home.show()
        self.close()