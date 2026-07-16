from PySide6.QtCore import QThread, Signal

from core.app import FenixPresence
from src.discord.rpc import DiscordRPC



class PresenceWorker(QThread):


    status = Signal(
        str
    )



    def __init__(
        self,
        wallets
    ):

        super().__init__()

        self.wallets = wallets



    def run(self):

        self.status.emit(
            "Starting Discord RPC..."
        )


        rpc = DiscordRPC()


        try:

            rpc.connect()

            self.status.emit(
                "Discord RPC connected"
            )


        except Exception as error:

            self.status.emit(
                f"RPC error: {error}"
            )



        app = FenixPresence(
            self.wallets,
            rpc
        )


        self.status.emit(
            "Mining monitor started"
        )


        app.start()