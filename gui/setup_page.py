from pathlib import Path
import json


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QMessageBox
)



class SetupPage(QWidget):


    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "🔥 FenixPresence Setup"
        )


        self.setFixedSize(
            500,
            600
        )


        self.inputs = {}


        self.coins = [
            "BTC",
            "BCH",
            "AUR",
            "LTC",
            "DOGE",
            "LCC",
            "RVN",
            "FIRO",
            "DGB",
            "PPC",
            "DASH",
            "ETC"
        ]


        self.build_ui()



    def build_ui(self):

        layout = QVBoxLayout(
            self
        )


        title = QLabel(
            "🔥 Welcome to FenixPresence\n\nConfigure your mining wallets"
        )


        title.setStyleSheet(
            """
            font-size:18px;
            font-weight:bold;
            """
        )


        layout.addWidget(
            title
        )



        scroll = QScrollArea()


        container = QWidget()


        wallet_layout = QVBoxLayout(
            container
        )



        for coin in self.coins:

            label = QLabel(
                f"{coin} Wallet"
            )


            input_box = QLineEdit()


            input_box.setPlaceholderText(
                f"Enter your {coin} address"
            )


            self.inputs[
                coin.lower()
            ] = input_box



            wallet_layout.addWidget(
                label
            )


            wallet_layout.addWidget(
                input_box
            )



        scroll.setWidget(
            container
        )


        scroll.setWidgetResizable(
            True
        )


        layout.addWidget(
            scroll
        )



        save = QPushButton(
            "Save configuration"
        )


        save.clicked.connect(
            self.save
        )


        layout.addWidget(
            save
        )



    def save(self):

        wallets = {}



        for coin, widget in self.inputs.items():

            address = widget.text().strip()



            if address:

                wallets[coin] = address



        if not wallets:

            QMessageBox.warning(
                self,
                "Error",
                "Please enter at least one wallet."
            )

            return



        config_dir = Path(
            "config"
        )


        config_dir.mkdir(
            exist_ok=True
        )



        with open(
            "config/wallets.json",
            "w",
            encoding="utf-8"
        ) as file:


            json.dump(
                {
                    "wallets": wallets
                },
                file,
                indent=4
            )



        QMessageBox.information(
            self,
            "Done",
            "Wallet configuration saved.\nYou can now start FenixPresence."
        )


        self.close()