from pathlib import Path
import sys


ROOT = Path(__file__).parent.parent

sys.path.insert(
    0,
    str(ROOT)
)


from core.formatter import (
    format_hashrate,
    format_diff,
    format_coin
)



print(
    "=== FORMATTER TEST ==="
)


print(
    "Hashrate:",
    format_hashrate(
        2730000000000
    )
)


print(
    "Diff:",
    format_diff(
        6461273937
    )
)


print(
    "Coin:",
    format_coin(
        35.00056587,
        "AUR"
    )
)