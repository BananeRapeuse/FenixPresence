from src.api.get_stats import StatsAPI
from src.api.get_performance import FenixPerformance
from src.api.get_pools import FenixPoolFinder

from models.miner import Miner



class FenixAPI:


    def __init__(
        self,
        wallet,
        coin
    ):

        self.wallet = wallet
        self.coin = coin



    def find_pool(self):

        finder = FenixPoolFinder()


        pools = finder.find_pools(
            self.wallet
        )


        for pool in pools:

            if pool["poolid"].startswith(
                self.coin.lower()
            ):

                return pool


        return None



    def get_full_miner(self):

        pool = self.find_pool()


        if not pool:

            print(
                "No pool found for wallet"
            )

            return None



        pool_id = pool["poolid"]



        stats_api = StatsAPI(
            pool_id,
            self.wallet
        )


        stats = stats_api.get()



        performance_api = FenixPerformance(
            pool_id,
            self.wallet
        )


        performance = performance_api.get()



        miner = Miner(

            coin=self.coin.upper(),

            pool=pool["label"],

            wallet=self.wallet

        )



        miner.hashrate = performance.get(
            "hashRate",
            0
        )


        miner.hashrate_5m = performance.get(
            "hashRate5m",
            0
        )


        miner.hashrate_1h = performance.get(
            "hashRate1h",
            0
        )



        miner.lifetime_earned = stats.get(
            "lifetimeEarned",
            0
        )


        miner.lifetime_blocks = stats.get(
            "lifetimeBlocks",
            0
        )


        miner.session_earned = stats.get(
            "sessEarned",
            0
        )


        miner.session_blocks = stats.get(
            "sessBlocks",
            0
        )


        miner.best_diff = stats.get(
            "sessBestDiff",
            0
        )



        for worker in performance.get(
            "workers",
            []
        ):

            miner.add_worker(
                worker["name"],
                worker
            )



        return miner