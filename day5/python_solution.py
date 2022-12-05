import logging
import copy

L = logging.getLogger(__name__)


# self.StartingPoint = {
#             1: ["Z", "N"],
#             2: ["M", "C", "D"],
#             3: ["P"]
#         } move 1 from 2 to 1

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