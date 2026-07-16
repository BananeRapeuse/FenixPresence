from src.api.fenix_api import FenixAPI



class MinerManager:


    def __init__(
        self,
        wallets
    ):

        self.wallets = wallets

        self.miners = {}



    def update(self):

        print(
            "Updating miners..."
        )


        for coin, wallet in self.wallets.items():


            try:

                api = FenixAPI(
                    wallet,
                    coin
                )


                miner = api.get_full_miner()



                if miner:


                    self.miners[coin] = miner


                    print(
                        f"{coin.upper()} updated"
                    )


                else:


                    print(
                        f"{coin.upper()} no data"
                    )



            except Exception as error:


                print(
                    f"{coin.upper()} update error: {error}"
                )



    def get_miners(self):

        return self.miners



    def get_miner(
        self,
        coin
    ):

        return self.miners.get(
            coin
        )



    def get_total_hashrate(self):

        total = 0


        for miner in self.miners.values():

            total += miner.hashrate



        return total



    def get_coins(self):

        return list(
            self.miners.keys()
        )