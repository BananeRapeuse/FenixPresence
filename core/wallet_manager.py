import json
from pathlib import Path



class WalletManager:


    def __init__(
        self,
        file="config/wallets.json"
    ):

        self.file = Path(
            file
        )


        self.file.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        if not self.file.exists():

            self.save([])



    def load(self):

        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(
                    f
                )


            if isinstance(data, dict):

                return data.get(
                    "wallets",
                    []
                )


            return []


        except (
            json.JSONDecodeError,
            FileNotFoundError
        ):

            return []



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


        coin = coin.upper()



        for wallet in wallets:

            if (
                wallet.get("coin") == coin
                and wallet.get("address") == address
            ):

                return False



        wallets.append(
            {
                "coin": coin,
                "address": address
            }
        )


        self.save(
            wallets
        )


        return True



    def remove_wallet(
        self,
        address
    ):

        wallets = self.load()


        new_wallets = [
            wallet
            for wallet in wallets
            if wallet.get("address") != address
        ]


        self.save(
            new_wallets
        )


        return len(wallets) != len(new_wallets)



    def get_wallets_by_coin(
        self,
        coin
    ):

        coin = coin.upper()


        return [
            wallet
            for wallet in self.load()
            if wallet.get("coin") == coin
        ]



    def count(self):

        return len(
            self.load()
        )