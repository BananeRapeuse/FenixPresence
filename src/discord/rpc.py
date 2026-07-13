from pathlib import Path
import json
from datetime import datetime, timezone

from pypresence import Presence

from core.formatter import (
    format_hashrate,
    format_coin,
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



    def is_recent_block(
        self,
        block_time
    ):

        if not block_time:

            return False


        try:

            date = datetime.fromisoformat(
                block_time.replace(
                    "Z",
                    "+00:00"
                )
            )


            now = datetime.now(
                timezone.utc
            )


            seconds = (
                now - date
            ).total_seconds()


            return seconds <= 300


        except Exception:

            return False



    def get_coin_icon(
        self,
        miner
    ):

        if miner.coin_icon:

            return miner.coin_icon


        return (
            miner.coin.lower()
            + "_x3"
        )



    def update_miner(
        self,
        miner
    ):


        if not self.rpc:

            return



        coin = miner.coin.upper()



        hashrate_text = format_hashrate(
            miner.hashrate
        )


        earned_text = format_coin(
            miner.lifetime_earned,
            coin
        )



        details = (
            f"⚡ {hashrate_text}"
        )



        state = (
            f"💰 {earned_text}"
            f" | "
            f"🧱 {miner.lifetime_blocks} Blocks"
        )



        if self.is_recent_block(
            miner.last_block_time
        ):

            state = (
                f"🎉 Block Found! "
                f"+{miner.last_block_reward:.8f} {coin}"
            )



        self.rpc.update(

            details=details,


            state=state,


            large_image="fenixpool",


            large_text="FenixPool",


            small_image=self.get_coin_icon(
                miner
            ),


            small_text=f"{coin} Mining",



            buttons=[

                {
                    "label": "Open FenixPool",
                    "url": "https://fenixpool.com"
                },

                {
                    "label": "GitHub",
                    "url": "https://github.com/BananeRapeuse/FenixPresence"
                }

            ],


            instance=False

        )