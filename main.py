from src.api.fenix_api import FenixAPI

from core.cache import MinerCache
from core.updater import MinerUpdater



wallet = "AJHkRsoypMY77gTN6NcxgzP6YYFupSsiDD"


api = FenixAPI(
    wallet,
    "aur-ember"
)


cache = MinerCache()



updater = MinerUpdater(
    api,
    cache,
    interval=60
)


updater.start()



while True:

    miner = cache.get()


    if miner:

        print(
            miner.lifetime_earned
        )


    time.sleep(8)