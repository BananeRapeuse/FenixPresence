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

    lifetime_earned: float = 0
    lifetime_blocks: int = 0

    session_earned: float = 0
    session_blocks: int = 0

    best_diff: float = 0
    last_block_finder: Optional[str] = None

    workers: Dict[str, dict] = field(
        default_factory=dict
    )


    def add_worker(self, name, data):

        self.workers[name] = data



    def get_worker_names(self):

        return list(
            self.workers.keys()
        )



    def get_summary(self):

        return {

            "coin": self.coin,

            "pool": self.pool,

            "hashrate": self.hashrate,

            "earned": self.lifetime_earned,

            "blocks": self.lifetime_blocks,

            "workers": len(
                self.workers
            ),

            "best_diff": self.best_diff,

            "finder": self.last_block_finder

        }



    def __str__(self):

        return (
            f"{self.coin} {self.pool} | "
            f"{self.hashrate} H/s | "
            f"{self.lifetime_earned} earned | "
            f"{self.lifetime_blocks} blocks"
        )