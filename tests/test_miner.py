from pathlib import Path
import sys


ROOT = Path(__file__).parent.parent

sys.path.insert(
    0,
    str(ROOT)
)


from models.miner import Miner



miner = Miner(

    coin="AUR",

    pool="AUR EMBER",

    wallet="AJHkJ..."

)



miner.hashrate = 2730000000000

miner.lifetime_earned = 35.00056587

miner.lifetime_blocks = 56


miner.add_worker(
    "bitaxe602",
    {
        "hashRate": 2170000000000
    }
)


miner.add_worker(
    "lv06",
    {
        "hashRate": 561000000000
    }
)



print(
    "=== MINER OBJECT ==="
)


print(
    miner
)


print()


print(
    "Workers:"
)


for worker in miner.get_worker_names():

    print(
        "-",
        worker
    )