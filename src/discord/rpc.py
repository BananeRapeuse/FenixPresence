from pathlib import Path
import json

from pypresence import Presence

from core.formatter import (
    format_hashrate,
    format_coin,
    format_diff
)



class DiscordRPC:


    def __init__(self):

        self.client_id = self.load_client_id()

        self.rpc = None



    def load_client_id(self):

        path = Path(
            "config/config.json"
        )


        if not path.exists():

            return None



        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )


        return data.get(
            "discord_client_id"
        )



    def connect(self):


        if not self.client_id:

            raise Exception(
                "Missing Discord client ID in config/config.json"
            )



        self.rpc = Presence(
            self.client_id
        )


        self.rpc.connect()



    def update_miner(
        self,
        miner
    ):


        if not self.rpc:

            return



        self.rpc.update(

            details=(
                f"⚡ "
                f"{format_hashrate(miner.hashrate)}"
            ),


            state=(
                f"💰 "
                f"{format_coin(miner.lifetime_earned, miner.coin)}"
                f" | "
                f"🧱 {miner.lifetime_blocks} Blocks"
            ),


            large_image="fenixpool",


            large_text=miner.pool,


            small_text=(
                f"{len(miner.workers)} workers"
            )

        )