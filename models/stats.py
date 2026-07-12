from dataclasses import dataclass


@dataclass
class MinerStats:
    tracked: bool

    session_blocks: int
    session_earned: float
    session_best_diff: float

    lifetime_blocks: int
    lifetime_earned: float


    @classmethod
    def from_json(cls, data: dict):
        return cls(
            tracked=data.get("tracked", False),

            session_blocks=data.get("sessBlocks", 0),
            session_earned=data.get("sessEarned", 0),
            session_best_diff=data.get("sessBestDiff", 0),

            lifetime_blocks=data.get("lifetimeBlocks", 0),
            lifetime_earned=data.get("lifetimeEarned", 0)
        )