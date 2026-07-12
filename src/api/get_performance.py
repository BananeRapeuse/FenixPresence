import requests


class FenixPerformance:


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
            f"{self.BASE_URL}/ff-pool/"
            f"{self.pool_id}/miners/"
            f"{self.wallet}"
        )


        response = requests.get(
            url,
            timeout=10
        )


        response.raise_for_status()


        return response.json()



    def format_hashrate(
        self,
        value
    ):

        if value >= 1_000_000_000_000:

            return (
                f"{value / 1_000_000_000_000:.2f} TH/s"
            )


        elif value >= 1_000_000_000:

            return (
                f"{value / 1_000_000_000:.2f} GH/s"
            )


        elif value >= 1_000_000:

            return (
                f"{value / 1_000_000:.2f} MH/s"
            )


        return f"{value:.0f} H/s"