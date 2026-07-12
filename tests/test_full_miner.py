from pathlib import Path
import sys


ROOT = Path(__file__).parent.parent

sys.path.insert(
    0,
    str(ROOT)
)


from src.api.fenix_api import FenixAPI



wallet = "AJHkRsoypMY77gTN6NcxgzP6YYFupSsiDD"



api = FenixAPI(
    wallet,
    "aur"
)



miner = api.get_full_miner()



print(
    "=== FULL MINER ==="
)


print(
    miner
)


print()


print(
    "Hashrate:",
    miner.hashrate
)


print(
    "Earned:",
    miner.lifetime_earned,
    "AUR"
)


print(
    "Blocks:",
    miner.lifetime_blocks
)


print()


print(
    "Workers:"
)


for worker in miner.workers:

    print(
        worker
    )