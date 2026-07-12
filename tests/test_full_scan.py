import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent

sys.path.insert(
    0,
    str(ROOT)
)


from src.scanner.wallet_scanner import WalletScanner



print(
    "=== FULL WALLET SCAN ==="
)



scanner = WalletScanner()


miners = scanner.scan_all()



for miner in miners:

    print(
        "\n----------------"
    )

    print(
        f"Coin : {miner['coin']}"
    )

    print(
        f"Wallet : {miner['address']}"
    )

    print(
        f"Pool : {miner['pool']['label']}"
    )

    print(
        f"ID : {miner['pool']['poolid']}"
    )