import requests



class StatsAPI:


    BASE_URL = "https://fenixpool.com/api"


    def __init__(
        self,
        pool_id,
        wallet
    ):

        self.pool_id = pool_id
        self.wallet = wallet



    def get(self):

        url = (
            f"{self.BASE_URL}/idle/"
            f"{self.pool_id}/"
            f"{self.wallet}"
        )


        response = requests.get(
            url,
            timeout=10
        )


        response.raise_for_status()


        return response.json()