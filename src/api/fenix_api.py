import requests

from models.stats import MinerStats
from models.miner import Miner


class FenixAPI:

    def __init__(
        self,
        wallet: str,
        pool_id: str | None = None
    ):

        self.wallet = wallet
        self.pool_id = pool_id

        self.base_url = "https://fenixpool.com/api"


    def _get(self, endpoint: str):

        url = f"{self.base_url}/{endpoint}"

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        return response.json()


    def get_pool_list(self):

        return self._get(
            f"miner-pools?address={self.wallet}"
        )


    def get_stats(self):

        if not self.pool_id:

            raise Exception(
                "Aucun pool_id défini"
            )


        return self._get(
            f"idle/{self.pool_id}/{self.wallet}"
        )


    def get_stats_object(self):

        data = self.get_stats()

        return MinerStats.from_json(
            data
        )


    def get_shares(self):

        if not self.pool_id:

            raise Exception(
                "Aucun pool_id défini"
            )


        return self._get(
            f"shares/{self.pool_id}/{self.wallet}"
        )


    def get_hashrate(
        self,
        span="1h",
        algo="sha"
    ):

        if not self.pool_id:

            raise Exception(
                "Aucun pool_id défini"
            )


        return self._get(
            f"miner-hashrate/"
            f"{self.pool_id}/"
            f"{self.wallet}"
            f"?span={span}"
            f"&algo={algo}"
        )


    def get_miner(self):

        stats = self.get_stats()
        shares = self.get_shares()


        return Miner(

            coin=self.pool_id.split("-")[0],

            mode=self.pool_id.split("-")[1],


            lifetime_earned=stats.get(
                "lifetimeEarned",
                0
            ),

            lifetime_blocks=stats.get(
                "lifetimeBlocks",
                0
            ),


            session_earned=stats.get(
                "sessEarned",
                0
            ),

            session_blocks=stats.get(
                "sessBlocks",
                0
            ),


            best_diff=shares.get(
                "bestDiffLifetime",
                0
            ),


            last_block_finder=shares.get(
                "lastBlockFinder",
                ""
            ),


            workers=shares.get(
                "workerBlockCounts",
                {}
            )
        )