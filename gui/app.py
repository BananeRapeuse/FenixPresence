import sys

from PySide6.QtWidgets import QApplication

from gui.setup_page import SetupPage



def run_gui():

    app = QApplication(
        sys.argv
    )


    app.setApplicationName(
        "FenixPresence Setup"
    )


    window = SetupPage()


    window.show()


    sys.exit(
        app.exec()
    )