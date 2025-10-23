def create_card(rank:str,suite:str):
    special_rank = {"j":11,"q":12, "k":13, "a":14}
    special_rank_keys = special_rank.keys()
    if rank in special_rank_keys:
        value = special_rank[rank]
    else:

        value = int(rank)

    card = dict(rank = rank, suite = suite, value = value  )

    return card









def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:

        return 'p1'
    elif p1_card["value"] < p2_card["value"]:

        return "p2"
    else:

        return "WAR"



def create_deck()-> list[dict]:
    deck_of_cards = []
    list_suite = ["h","c","d","s"]
    list_rank = ["2","3","4","5","6","7","8","9","10","j","k","q","a"]
    for suite in list_suite:
        for rank in list_rank:
            deck_of_cards.append(create_card(rank,suite))
    print(deck_of_cards)
    return deck_of_cards



import  random

def shuffle(deck:list[dict]) -> list[dict]:
    a = random.randint(0,51)
    b = random.randint(0,51)
    deck[a]

    list[dict] = [{}]
    return