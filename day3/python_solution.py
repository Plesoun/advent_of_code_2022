import logging

L = logging.getLogger(__name__)


def split_compartment(input_data: str) -> tuple:
    # Sanitize
    pack_items = input_data.lstrip().rstrip()
    if len(pack_items) % 2 != 0:
        L.error(
            "The pack contains invalid number of items."
        )
        raise Exception(
            "The pack contains invalid number of items."
        )
    else:
        compartment_size = len(pack_items) // 2
        return (
            pack_items[:compartment_size],
            pack_items[compartment_size:],
        )


def find_intersection(split_backpack: tuple) -> set:
    comp_1, comp_2 = split_backpack
    # Return common letters
    return set(comp_1).intersection(comp_2)


def find_triplets_intersection(triplet: tuple) -> set:
    one, two, three = triplet
    return set(one).intersection(two).intersection(three)


def calculate_priority(intersections: set) -> int:
    priority = 0
    if len(intersections) == 0:
        return priority
    else:
        for item in intersections:
            if item.isupper():
                priority += ord(item) - 38
            else:
                priority += ord(item) - 96
        return priority


if __name__ == "__main__":
    sum_of_priorities_part_one = 0
    sum_of_priorities_part_two = 0
    with open("./day3/input", "r") as f:
        for backpack in f.readlines():
            split_backpack = split_compartment(backpack)
            sum_of_priorities_part_one += (
                calculate_priority(
                    find_intersection(split_backpack)
                )
            )

        print(
            "Item priorities part one: ",
            sum_of_priorities_part_one,
        )

    # Part two
    with open("./day3/input", "r") as f:
        iterator = iter(f)
        for backpack_1, backpack_2, backpack_3 in zip(
            iterator, iterator, iterator
        ):
            sum_of_priorities_part_two += (
                calculate_priority(
                    find_triplets_intersection(
                        (
                            backpack_1.lstrip().rstrip(),
                            backpack_2.lstrip().rstrip(),
                            backpack_3.lstrip().rstrip(),
                        )
                    )
                )
            )
        print(
            "Item priorities part two: ",
            sum_of_priorities_part_two,
        )
