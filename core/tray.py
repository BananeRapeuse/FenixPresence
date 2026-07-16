from PySide6.QtWidgets import (
    QSystemTrayIcon,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QApplication
)

from PySide6.QtGui import (
    QIcon,
    QPixmap,
    QPainter
)

from PySide6.QtCore import Qt



class TrayWindow(QWidget):


    def __init__(self, tray):

        super().__init__()

        self.tray = tray

        self.setWindowTitle(
            "FenixPresence"
        )

        self.setFixedSize(
            250,
            120
        )


        layout = QVBoxLayout(
            self
        )


        restart = QPushButton(
            "🔄 Restart FenixPresence"
        )


        close = QPushButton(
            "❌ Close FenixPresence"
        )


        restart.clicked.connect(
            self.restart
        )


        close.clicked.connect(
            self.close_app
        )


        layout.addWidget(
            restart
        )


        layout.addWidget(
            close
        )



    def restart(self):

        print(
            "Restart requested"
        )



    def close_app(self):

        QApplication.quit()



class FenixTray:


    def __init__(self):

        self.tray = QSystemTrayIcon()


        self.tray.setIcon(
            self.create_icon()
        )


        self.window = TrayWindow(
            self
        )


        self.tray.activated.connect(
            self.clicked
        )



    def create_icon(self):

        pixmap = QPixmap(
            64,
            64
        )

        pixmap.fill(
            Qt.transparent
        )


        painter = QPainter(
            pixmap
        )


        painter.drawEllipse(
            10,
            10,
            44,
            44
        )


        painter.end()


        return QIcon(
            pixmap
        )



    def show(self):

        self.tray.show()


        print(
            "Tray shown"
        )



    def clicked(
        self,
        reason
    ):

        print(
            "Tray clicked:",
            reason
        )


        self.window.show()

        self.window.raise_()

        self.window.activateWindow()