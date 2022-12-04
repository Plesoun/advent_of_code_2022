import logging

L = logging.getLogger(__name__)

def range_comparison(range_1: str, range_2: str) -> bool:
    # Parse the numbers from strings
    range_1 = [int(i) for i in range_1.split("-")]
    range_2 = [int(i) for i in range_2.split("-")]

    print(range_1, range_2)
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        return True
    elif range_2[0] <= range_1[0] and range_2[1] >= range_1[1]:
        return True 
    else:
        print("False")
        return False

if __name__ == "__main__":
    overlap_counter = 0
    with open("./day4/input", "r") as f:
        for line in f.readlines():
            range_1, range_2 = line.split(",")
            if range_comparison(range_1, range_2) is True:
                overlap_counter += 1
            else:
                continue
        print("Overlap occurs in {} cases".format(overlap_counter))
