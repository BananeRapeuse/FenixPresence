import json
from pathlib import Path


class WalletManager:


    def __init__(
        self,
        file="config/wallets.json"
    ):

        self.file = Path(file)


        self.file.parent.mkdir(
            exist_ok=True
        )


        if not self.file.exists():

            self.save(
                []
            )



    def load(self):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        return data.get(
            "wallets",
            []
        )



    def save(
        self,
        wallets
    ):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {
                    "wallets": wallets
                },
                f,
                indent=4
            )



    def add_wallet(
        self,
        coin,
        address
    ):

        wallets = self.load()


        wallets.append(
            {
                "coin": coin.upper(),
                "address": address
            }
        )


        self.save(
            wallets
        )



    def remove_wallet(
        self,
        address
    ):

        wallets = self.load()


        wallets = [
            w for w in wallets
            if w["address"] != address
        ]


        self.save(
            wallets
        )