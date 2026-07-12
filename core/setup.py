from core.wallet_manager import WalletManager


SUPPORTED_COINS = [
    "BTC",
    "BCH",
    "AUR",
    "LTC",
    "DOGE",
    "LCC",
    "RVN",
    "FIRO",
    "DGB",
    "NMC",
    "PPC",
    "XMR",
    "DASH",
    "ETC",
    "ERG"
]


def run_first_setup():

    print("=" * 60)
    print("                First Time Setup")
    print("=" * 60)
    print()
    print("Please enter your wallet addresses.")
    print("Press ENTER to skip a coin.")
    print()

    manager = WalletManager()

    wallets = []

    for coin in SUPPORTED_COINS:

        while True:

            address = input(f"{coin} address: ").strip()

            if address == "":

                break

            wallets.append(
                {
                    "coin": coin,
                    "address": address
                }
            )

            break

    manager.save(wallets)

    print()
    print("=" * 60)
    print("Configuration saved successfully!")
    print(f"{len(wallets)} wallet(s) added.")
    print("=" * 60)