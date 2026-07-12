from pathlib import Path
import sys
import time


from core.setup import run_first_setup
from core.config import Config

from src.api.fenix_api import FenixAPI
from src.discord.rpc import DiscordRPC



CONFIG_FILE = Path(
    "config/wallets.json"
)



def print_banner():

    print("=" * 60)
    print("                Welcome to FenixPresence!")
    print("=" * 60)
    print()
    print("Thank you for using this project.")
    print()
    print("Created by Frelon111 for the FenixPool community.")
    print()
    print("Need help?")
    print("• Contact me on Discord")
    print("• Open an issue on GitHub")
    print()
    print("See CONTACTS.md for more information.")
    print()
    print("Happy mining! 🔥")
    print()
    print("=" * 60)
    print()



def should_run_setup():


    if "--setup" in sys.argv:

        return True



    if not CONFIG_FILE.exists():

        return True



    if CONFIG_FILE.stat().st_size == 0:

        return True



    return False



def load_wallets():

    config = Config(
        "config/wallets.json"
    )


    wallets = config.get_wallets()



    # Format:
    # {
    #   "wallets": {...}
    # }

    if isinstance(wallets, dict) and "wallets" in wallets:

        wallets = wallets["wallets"]



    result = {}



    # Format:
    # {
    #   "aur": "address"
    # }

    if isinstance(wallets, dict):


        for coin, value in wallets.items():


            if isinstance(value, str):

                result[coin] = value



            elif isinstance(value, dict):


                address = value.get(
                    "address"
                )


                if address:

                    result[coin] = address



    # Format:
    # [
    #   {
    #      "coin":"aur",
    #      "address":"..."
    #   }
    # ]

    elif isinstance(wallets, list):


        for wallet in wallets:


            coin = wallet.get(
                "coin"
            )


            address = wallet.get(
                "address"
            )


            if coin and address:

                result[coin] = address



    return result


def main():


    print_banner()



    if should_run_setup():


        print(
            "Starting wallet setup...\n"
        )


        run_first_setup()


        print()



    print(
        "Loading wallets..."
    )



    wallets = load_wallets()



    if not wallets:


        print(
            "No wallets configured."
        )


        print(
            "Run: py main.py --setup"
        )


        return



    print()


    print(
        "Wallets loaded:"
    )



    for coin in wallets:


        print(
            f"- {coin.upper()}"
        )



    print()



    print(
        "Starting FenixPresence..."
    )



    rpc = DiscordRPC()



    try:

        rpc.connect()


    except Exception as error:

        print(
            "Discord RPC error:",
            error
        )



    while True:


        for coin, wallet in wallets.items():


            try:


                print()

                print(
                    f"Scanning {coin.upper()}..."
                )



                api = FenixAPI(

                    wallet,

                    coin

                )



                miner = (
                    api.get_full_miner()
                )



                if miner:


                    print(
                        miner
                    )


                    try:

                        rpc.update_miner(
                            miner
                        )

                    except Exception as error:

                        print(
                            "RPC update error:",
                            error
                        )



                else:


                    print(
                        "No miner found"
                    )



            except Exception as error:


                print(
                    f"{coin.upper()} scan error:",
                    error
                )



        time.sleep(
            8
        )




if __name__ == "__main__":

    main()