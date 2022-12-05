import logging

L = logging.getLogger(__name__)

def complete_overlap(range_1: str, range_2: str) -> bool:
    # Parse the numbers from strings
    range_1 = [int(i) for i in range_1.split("-")]
    range_2 = [int(i) for i in range_2.split("-")]
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        return True
    elif range_2[0] <= range_1[0] and range_2[1] >= range_1[1]:
        return True 
    else:
        return False


def partial_overlap(range_1: str, range_2: str) -> bool:
    # Parse the numbers from strings
    range_1 = [int(i) for i in range_1.split("-")]
    range_2 = [int(i) for i in range_2.split("-")]
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[0]:
        return True
    elif range_2[0] <= range_1[0] and range_2[1] >= range_1[0]:
        return True 
    else:
        return False


if __name__ == "__main__":
    complete_overlap_counter = 0
    partial_overlap_counter = 0
    with open("./day4/input", "r") as f:
        for line in f.readlines():
            range_1, range_2 = line.split(",")
            if complete_overlap(range_1, range_2) is True:
                complete_overlap_counter += 1
            else:
                continue

    with open("./day4/input", "r") as f:
        for line in f.readlines():
            range_1, range_2 = line.split(",")
            if partial_overlap(range_1, range_2) is True:
                partial_overlap_counter += 1
        print("Complete overlap occurs in {} cases".format(complete_overlap_counter))
        print("Partial overlap occurs in {} cases".format(partial_overlap_counter))
