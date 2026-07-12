import requests


class FenixPoolFinder:


    def __init__(self):

        self.base_url = (
            "https://fenixpool.com/api"
        )


    def find_pools(
        self,
        address: str
    ):

        url = (
            f"{self.base_url}/miner-pools"
            f"?address={address}"
        )


        response = requests.get(
            url,
            timeout=10
        )


        response.raise_for_status()


        return response.json()["pools"]