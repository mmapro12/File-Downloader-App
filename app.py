from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
from os import path
import sys
import urllib.request

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))

class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent = None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()

    
    def Handel_UI(self):
        self.setWindowTitle("MDownload")
        self.setFixedSize(795, 443)
    
    def Handel_Buttons(self):
        self.download_button.clicked.connect(self.Download)

    def Handel_Browse(self):
        pass

    def Handel_Progress(self, blocknum, blocksize, totalsize):
        read = blocknum*blocksize
        if totalsize > 0:
            percent = read*100 / totalsize
            self.progressBar.setValue(round(percent))

    def Download(self):
        url = self.url_line.text()
        save_loc = self.location_line.text()
        self.progressBar.setValue(0)

        urllib.request.urlretrieve(url, save_loc, self.Handel_Progress)

        try:
            QMessageBox.information(self, "Completed!", "Download Finished!")
        except Exception:
            QMessageBox.warning(self, "Error!", "Download Failed!")

        self.progressBar.setValue(0)
        self.url_line.setText("")
        self.location_line.setText("")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
