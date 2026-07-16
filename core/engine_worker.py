from PySide6.QtCore import QThread, Signal

from core.app import FenixPresence



class EngineWorker(QThread):


    status = Signal(str)



    def __init__(
        self,
        wallets,
        rpc
    ):

        super().__init__()

        self.wallets = wallets
        self.rpc = rpc

        self.engine = None



    def run(self):

        try:

            self.status.emit(
                "Starting engine..."
            )


            self.engine = FenixPresence(
                self.wallets,
                self.rpc
            )


            self.engine.start()


        except Exception as error:

            self.status.emit(
                str(error)
            )