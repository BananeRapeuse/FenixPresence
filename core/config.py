from pathlib import Path
import json



class Config:


    def __init__(
        self,
        path
    ):

        self.path = Path(
            path
        )

        self.data = {}


        self.load()



    def load(self):

        if not self.path.exists():

            self.data = {}

            return


        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as file:

            self.data = json.load(
                file
            )



    def save(self):

        self.path.parent.mkdir(
            exist_ok=True
        )


        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.data,
                file,
                indent=4
            )



    def get_wallets(self):

        return self.data.get(
            "wallets",
            {}
        )



    def save_wallets(
        self,
        wallets
    ):

        self.data["wallets"] = wallets

        self.save()