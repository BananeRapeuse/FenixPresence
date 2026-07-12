from dataclasses import dataclass, field


@dataclass
class Miner:
    coin: str
    mode: str

    lifetime_earned: float = 0
    lifetime_blocks: int = 0

    session_earned: float = 0
    session_blocks: int = 0

    best_diff: float = 0
    last_block_finder: str = ""

    workers: dict = field(default_factory=dict)