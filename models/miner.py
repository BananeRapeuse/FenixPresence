from dataclasses import dataclass, field
from typing import Dict, Optional



@dataclass
class Miner:

    coin: str
    pool: str
    wallet: str

    hashrate: float = 0
    hashrate_5m: float = 0
    hashrate_1h: float = 0
    hashrate_24h: float = 0

    lifetime_earned: float = 0
    lifetime_blocks: int = 0

    session_earned: float = 0
    session_blocks: int = 0

    best_diff: float = 0
    last_block_finder: Optional[str] = None

    # Nouveau : bloc récent
    last_block_time: Optional[str] = None
    last_block_reward: float = 0

    # Permet de choisir l'image Discord
    coin_icon: Optional[str] = None

    workers: Dict[str, dict] = field(
        default_factory=dict
    )



    def add_worker(
        self,
        name,
        data
    ):

        self.workers[name] = data



    def get_worker_names(self):

        return list(
            self.workers.keys()
        )



    def get_worker_count(self):

        return len(
            self.workers
        )



    def get_summary(self):

        return {

            "coin": self.coin,

            "pool": self.pool,

            "wallet": self.wallet,

            "hashrate": self.hashrate,

            "earned": self.lifetime_earned,

            "blocks": self.lifetime_blocks,

            "workers": self.get_worker_count(),

            "best_diff": self.best_diff,

            "finder": self.last_block_finder,

            "last_block_time": self.last_block_time,

            "last_block_reward": self.last_block_reward

        }



    def __str__(self):

        return (
            f"{self.coin.upper()} {self.pool} | "
            f"{self.hashrate} H/s | "
            f"{self.lifetime_earned} earned | "
            f"{self.lifetime_blocks} blocks"
        )