from core.wallet_manager import WalletManager
from src.api.fenix_api import FenixAPI



class WalletScanner:


    def __init__(self):

        self.wallet_manager = WalletManager()



    def scan_all(self):

        wallets = self.wallet_manager.load()

        miners = []


        for wallet in wallets:

            address = wallet["address"]


            api = FenixAPI(
                address
            )


            pools = api.get_pool_list()


            for pool in pools.get(
                "pools",
                []
            ):

                miners.append(
                    {
                        "coin": wallet["coin"],
                        "address": address,
                        "pool": pool
                    }
                )


        return miners