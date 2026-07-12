from models.miner import Miner


class MinerCache:

    def __init__(self):
        self.miner: Miner | None = None


    def update(self, miner: Miner):

        self.miner = miner


    def get(self):

        return self.miner