import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent


sys.path.insert(
    0,
    str(ROOT)
)


from core.wallet_manager import WalletManager



manager = WalletManager()



print(
    "=== WALLET MANAGER TEST ==="
)



print(
    "\nWallets actuels:"
)


for wallet in manager.load():

    print(
        f"- {wallet['coin']} : {wallet['address']}"
    )



print(
    "\nAjout test wallet..."
)


manager.add_wallet(
    "BTC",
    "test_btc_wallet"
)



for wallet in manager.load():

    print(
        f"- {wallet['coin']} : {wallet['address']}"
    )



print(
    "\nSuppression test wallet..."
)


manager.remove_wallet(
    "test_btc_wallet"
)



print(
    "\nFinal:"
)


for wallet in manager.load():

    print(
        f"- {wallet['coin']} : {wallet['address']}"
    )