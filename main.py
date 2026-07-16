from pathlib import Path
import sys


from PySide6.QtWidgets import QApplication


from core.config import Config
from gui.app import run_gui
from core.logger import logger


from core.startup import (
    enable_startup,
    is_startup_enabled
)


from core.tray import FenixTray
from core.engine_worker import EngineWorker


from src.discord.rpc import DiscordRPC



CONFIG_FILE = Path(
    "config/wallets.json"
)



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


    result = {}


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


    return result



def setup_startup():

    try:

        if not is_startup_enabled():

            enable_startup()

            logger.info(
                "Startup enabled"
            )


    except Exception as error:

        logger.error(
            f"Startup error: {error}"
        )



def main():

    logger.info(
        "Starting FenixPresence"
    )


    if should_run_setup():

        logger.info(
            "Opening setup wizard"
        )


        run_gui()

        return



    logger.info(
        "Loading wallets"
    )


    wallets = load_wallets()


    if not wallets:

        logger.warning(
            "No wallets configured"
        )

        return



    for coin in wallets:

        logger.info(
            f"Wallet loaded: {coin.upper()}"
        )



    setup_startup()



    app = QApplication(
        sys.argv
    )



    tray = FenixTray()

    tray.show()



    rpc = DiscordRPC()


    try:

        rpc.connect()

        logger.info(
            "Discord RPC connected"
        )


    except Exception as error:

        logger.error(
            f"Discord RPC error: {error}"
        )



    worker = EngineWorker(
        wallets,
        rpc
    )


    worker.status.connect(
        logger.info
    )


    worker.start()



    logger.info(
        "Engine worker started"
    )



    sys.exit(
        app.exec()
    )



if __name__ == "__main__":

    main()