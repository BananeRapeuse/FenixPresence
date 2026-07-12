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



from src.scanner.wallet_scanner import WalletScanner
from src.api.fenix_api import FenixAPI



WALLET = "AJHkRsoypMY77gTN6NcxgzP6YYFupSsiDD"



print(
    "=== WALLET SCANNER TEST ==="
)



scanner = WalletScanner(
    WALLET
)



pool = scanner.get_active_pool()



if pool:

    print(
        "Pool trouvée:"
    )

    print(
        f"Nom : {pool['label']}"
    )

    print(
        f"ID : {pool['poolid']}"
    )



    print(
        "\n=== MINER DATA ==="
    )


    api = FenixAPI(
        WALLET,
        pool["poolid"]
    )


    miner = api.get_miner()


    print(
        f"Coin : {miner.coin}"
    )

    print(
        f"Mode : {miner.mode}"
    )

    print(
        f"Earned : {miner.lifetime_earned}"
    )

    print(
        f"Blocks : {miner.lifetime_blocks}"
    )


else:

    print(
        "Aucune pool trouvée"
    )