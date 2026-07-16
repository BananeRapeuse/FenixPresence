from core.scheduler import Scheduler
from core.miner_manager import MinerManager



class FenixPresence:


    def __init__(
        self,
        wallets,
        rpc
    ):

        self.rpc = rpc

        self.miner_manager = MinerManager(
            wallets
        )

        self.scheduler = Scheduler()



    def start(self):

        print(
            "FenixPresence engine started."
        )


        self.scheduler.add_task(
            self.update,
            8
        )


        self.scheduler.start()



    def stop(self):

        self.scheduler.stop()



    def update(self):

        self.miner_manager.update()


        miners = (
            self.miner_manager.get_miners()
        )


        for miner in miners.values():

            try:

                self.rpc.update_miner(
                    miner
                )


            except Exception as error:

                print(
                    f"RPC update error: {error}"
                )