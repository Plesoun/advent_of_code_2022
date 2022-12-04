import logging

L = logging.getLogger(__name__)


def split_compartments(input_data: list) -> list:
    backpacks_split = []
    for pack_items in input_data:
        # Sanitize
        pack_items = pack_items.lstrip().rstrip()
        if len(pack_items)%2 != 0:
            L.error("The pack contains invalid number of items.")
        else:
            compartment_size = len(pack_items)//2
            backpacks_split.append((pack_items[:compartment_size], pack_items[compartment_size:]))
    return backpacks_split

def calculate_priority(backpacks_split: list) -> int:
    pass

if __name__ == "__main__":
    with open("./test/input", "r") as f:
        backpacks = split_compartments(f.readlines())

            
