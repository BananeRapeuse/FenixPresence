import sys
from pathlib import Path


# Permet à Python de trouver src/ et models/
ROOT = Path(__file__).parent.parent

sys.path.insert(
    0,
    str(ROOT)
)

sys.path.insert(
    0,
    str(ROOT / "src")
)


from src.api.get_pools import FenixPoolFinder



WALLET = "AJHkRsoypMY77gTN6NcxgzP6YYFupSsiDD"



def main():

    print("=== FENIXPOOL POOL FINDER TEST ===")


    finder = FenixPoolFinder()


    try:

        pools = finder.find_pools(
            WALLET
        )


        print(
            f"\nPools trouvées : {len(pools)}"
        )


        if len(pools) == 0:

            print(
                "Aucune pool trouvée pour ce wallet."
            )

            return



        for pool in pools:

            print(
                "\n--------------------"
            )

            print(
                f"Nom     : {pool['label']}"
            )

            print(
                f"Pool ID : {pool['poolid']}"
            )

            print(
                f"Dernière share : {pool['lastShare']}"
            )

            print(
                f"Shares 24h      : {pool['shares24h']}"
            )


    except Exception as e:

        print(
            f"\nErreur : {e}"
        )



if __name__ == "__main__":

    main()