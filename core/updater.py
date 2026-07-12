import time
import threading


class MinerUpdater:


    def __init__(
        self,
        api,
        cache,
        interval=60
    ):

        self.api = api
        self.cache = cache

        self.interval = interval

        self.running = False



    def update_loop(self):

        while self.running:

            try:

                miner = self.api.get_miner()

                self.cache.update(
                    miner
                )

                print(
                    "[CACHE] Updated"
                )


            except Exception as e:

                print(
                    f"[CACHE ERROR] {e}"
                )


            time.sleep(
                self.interval
            )



    def start(self):

        self.running = True


        thread = threading.Thread(
            target=self.update_loop,
            daemon=True
        )


        thread.start()