from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    blocks: int
    best_diff: float
    last_diff: float