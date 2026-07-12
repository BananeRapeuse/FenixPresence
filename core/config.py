import json



class Config:


    def __init__(
        self,
        path="config.json"
    ):

        self.path = path

        self.data = {}

        self.load()



    def load(self):

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as file:

            self.data = json.load(
                file
            )



    def get_wallets(self):

        return self.data.get(
            "wallets",
            {}
        )



    def get_refresh_time(self):

        return self.data.get(
            "refresh_time",
            8
        )



    def get_discord_id(self):

        return self.data.get(
            "discord",
            {}
        ).get(
            "client_id"
        )