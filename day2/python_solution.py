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

matrix_p2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
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
        raise Exception("You need to specify filename, or provide a strategy_list.")
    return score

def strategy_prediction_p2(filename: str = None, strategy_list: list = None) -> int:
    score = 0
    if filename is not None:
        with open(filename, "r") as f:
            for line in f.readlines():
                score += matrix_p2[line.rstrip()]
    elif strategy_list is not None:
        for rps_round in strategy_list:
            score += matrix_p2[rps_round.rstrip()]
    else:
        L.error("You need to specify filename, or provide a strategy_list.")
        raise Exception("You need to specify filename, or provide a strategy_list.")
    return score


if __name__ == "__main__":
    print(strategy_prediction(filename="./day2/input"))
    print(strategy_prediction_p2(filename="./day2/input"))