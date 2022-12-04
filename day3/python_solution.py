import logging

L = logging.getLogger(__name__)


def split_compartment(input_data: str) -> tuple:
    # Sanitize
    print(input_data, type(input_data))
    pack_items = input_data.lstrip().rstrip()
    if len(pack_items)%2 != 0:
        L.error("The pack contains invalid number of items.")
        raise Exception("The pack contains invalid number of items.")
    else:
        compartment_size = len(pack_items)//2
        return (pack_items[:compartment_size], pack_items[compartment_size:])

def find_intersection(split_backpack: tuple) -> set:
    comp_1, comp_2 = split_backpack
    # Return common letters
    return set(comp_1).intersection(comp_2)

def calculate_priority(intersections: set) -> int:
    pass
    


if __name__ == "__main__":
    with open("./test/input", "r") as f:
        for backpack in f.readlines():
            split_backpack = split_compartment(backpack)
            print(calculate_priority(split_backpack))
