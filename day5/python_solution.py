import logging
import copy

L = logging.getLogger(__name__)


def crane_rearrange_step(move: str, starting_point: dict) -> dict:
    step = copy.deepcopy(starting_point)
    move_list = move.split(" ")
    how_many = int(move_list[1])
    from_where = int(move_list[3])
    to_where = int(move_list[5].lstrip())
    for i in range(how_many):
        popped_thing = step[from_where].pop()
        step[to_where].append(popped_thing)
    return step

def crane_rearrange_bulk(move: str, starting_point: dict) -> dict:
    step = copy.deepcopy(starting_point)
    move_list = move.split(" ")
    how_many = int(move_list[1])
    from_where = int(move_list[3])
    to_where = int(move_list[5].lstrip())
    for i in range(how_many):
        popped_thing = step[from_where].pop()
        step[to_where].append(popped_thing)
    return step


if __name__ == "__main__":
    current_setup = {
            1: ["N", "S", "D", "C", "V", "Q", "T"],
            2: ["M", "F", "V"],
            3: ["F", "Q", "W", "D", "P", "N", "H", "M"],
            4: ["D", "Q", "R", "T", "F"],
            5: ["R", "F", "M", "N", "Q", "H", "V", "B"],
            6: ["C", "F", "G", "N", "P", "V", "Q"],
            7: ["W", "F", "R", "L", "C", "T"],
            8: ["T", "Z", "N", "S"],
            9: ["M", "S", "D", "J", "R", "Q", "H", "N"]
        }
    answer = []
    with open("./day5/input", "r") as f:
        for move in f.readlines():
            current_setup = crane_rearrange_step(move, current_setup)
        for key, value in current_setup.items():
            answer.append(value[-1:][0])
        print("Aaaand the answer is: ", "".join(answer))
