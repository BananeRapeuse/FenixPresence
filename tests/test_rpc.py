import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent

sys.path.insert(
    0,
    str(ROOT)
)


from src.discord.rpc import DiscordRPC



print(
    "Starting FenixPresence RPC test..."
)


rpc = DiscordRPC()


print(
    "Connecting to Discord..."
)


rpc.connect()


rpc.update(
    details="Mining on FenixPool",
    state="Testing Discord Rich Presence"
)


print(
    "RPC running!"
)


input(
    "Press ENTER to close..."
)


rpc.close()