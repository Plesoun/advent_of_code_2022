import logging

L = logging.getLogger(__name__)

def range_comparison(range_1: str, range_2: str) -> bool:
    # Parse the numbers from strings
    range_1 = [int(i) for i in range_1.split("-")]
    range_2 = [int(i) for i in range_2.split("-")]
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        print("True")
        return True
    else:
        print("False")
        return False