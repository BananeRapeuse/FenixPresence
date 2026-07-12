import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent


sys.path.insert(
    0,
    str(ROOT)
)


sys.path.insert(
    0,
    str(ROOT / "src")
)


from src.api.fenix_api import FenixAPI



WALLET = "AJHkRsoypMY77gTN6NcxgzP6YYFupSsiDD"



api = FenixAPI(
    wallet=WALLET,
    coin="aur-ember"
)



print("\n=== MINER OBJECT ===")


miner = api.get_miner()



print(
    f"Coin : {miner.coin}"
)

print(
    f"Mode : {miner.mode}"
)


print(
    f"Lifetime earned : {miner.lifetime_earned} AUR"
)


print(
    f"Lifetime blocks : {miner.lifetime_blocks}"
)


print(
    f"Session earned : {miner.session_earned} AUR"
)


print(
    f"Session blocks : {miner.session_blocks}"
)


print(
    f"Best diff : {miner.best_diff}"
)


print(
    f"Last block finder : {miner.last_block_finder}"
)



print("\n=== WORKERS ===")


for worker, blocks in miner.workers.items():

    print(
        f"{worker} : {blocks} blocks"
    )