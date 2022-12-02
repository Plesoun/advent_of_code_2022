import logging

L = logging.getLogger(__name__)

matrix = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

def strategy_prediction(filename: str = None, strategy_list: list = None) -> int:
    score = 0
    if filename is not None:
        with open(filename, "r") as f:
            for line in f.readlines():
                score += matrix[line.rstrip()]
    elif strategy_list is not None:
        for rps_round in strategy_list:
            score += matrix[rps_round.rstrip()]
    else:
        L.error("You need to specify filename, or provide a strategy_list.")
        # TODO: raise some error here
    return score