from dataclasses import dataclass


@dataclass
class Pool:

    name: str
    slug: str
    algo: str