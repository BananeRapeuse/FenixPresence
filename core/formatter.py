def format_hashrate(value):
    """
    Convertit un hashrate en H/s lisible
    Exemple:
    2730000000000 -> 2.73 TH/s
    """

    if value is None:
        return "0 H/s"


    value = float(value)


    if value >= 1_000_000_000_000:

        return f"{value / 1_000_000_000_000:.2f} TH/s"


    if value >= 1_000_000_000:

        return f"{value / 1_000_000_000:.2f} GH/s"


    if value >= 1_000_000:

        return f"{value / 1_000_000:.2f} MH/s"


    if value >= 1_000:

        return f"{value / 1_000:.2f} KH/s"


    return f"{value:.0f} H/s"



def format_diff(value):
    """
    Convertit une difficulté en notation courte
    Exemple:
    6461273937 -> 6.46G
    """

    if value is None:
        return "0"


    value = float(value)


    if value >= 1_000_000_000:

        return f"{value / 1_000_000_000:.2f}G"


    if value >= 1_000_000:

        return f"{value / 1_000_000:.2f}M"


    if value >= 1_000:

        return f"{value / 1_000:.2f}K"


    return f"{value:.0f}"



def format_coin(value, ticker):
    """
    Format une récompense crypto
    Exemple:
    35.00056587 AUR
    """

    if value is None:
        return f"0 {ticker}"


    return f"{float(value):.8f} {ticker}"



def format_workers(workers):
    """
    Transforme les workers en texte Discord
    """

    if not workers:

        return "No workers"


    result = []


    for name, data in workers.items():

        if isinstance(data, dict):

            hashrate = data.get(
                "hashRate",
                0
            )

        else:

            hashrate = data


        result.append(
            f"{name}: {format_hashrate(hashrate)}"
        )


    return "\n".join(result)

def format_wallet(wallet):

    if not wallet:
        return "No wallet"


    return wallet



def format_block_reward(value, ticker):

    if value is None or value == 0:

        return None


    return (
        f"+{float(value):.8f} {ticker.upper()}"
    )

def format_multicoin_hashrate(miners):
    """
    Format:
    ⚡ 3.24 TH/s AUR | 1.43 TH/s BTC
    """

    result = []


    for coin, miner in miners.items():

        result.append(
            f"{format_hashrate(miner.hashrate)} {coin.upper()}"
        )


    if not result:

        return "No mining activity"


    return " | ".join(result)



def format_multicoin_earned(miners):
    """
    Format:
    💰 35.00056587 AUR | 1.00000000 BTC
    """

    result = []


    for coin, miner in miners.items():

        result.append(
            f"{format_coin(miner.lifetime_earned, coin.upper())}"
        )


    if not result:

        return "No rewards"


    return " | ".join(result)



def format_multicoin_blocks(miners):
    """
    Format:
    🧱 56 Blocks AUR | 1 Blocks BTC
    """

    result = []


    for coin, miner in miners.items():

        result.append(
            f"{miner.lifetime_blocks} Blocks {coin.upper()}"
        )


    if not result:

        return "No blocks"


    return " | ".join(result)