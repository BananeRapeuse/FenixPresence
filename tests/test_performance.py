import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent

sys.path.insert(
    0,
    str(ROOT)
)


from src.api.get_performance import FenixPerformance



POOL = "aur-ember"

WALLET = "AJHkRsoypMY77gTN6NcxgzP6YYFupSsiDD"



api = FenixPerformance(
    POOL,
    WALLET
)


data = api.get()



print(
    "=== PERFORMANCE ==="
)


print(
    "Hashrate:",
    api.format_hashrate(
        data["hashRate"]
    )
)


print(
    "Hashrate 5m:",
    api.format_hashrate(
        data["hashRate5m"]
    )
)



print(
    "\n=== WORKERS ==="
)


for worker in data["workers"]:

    print(
        worker["name"],
        ":",
        api.format_hashrate(
            worker["hashRate"]
        )
    )