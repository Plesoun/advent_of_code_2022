import logging

L = logging.getLogger(__name__)

"""
representation = {
    "/": ["folder1", "folder2", "folder3"],
    "/folder1": ["folder4"],
    "folder1/file.1": 321741,
}


decider_matrix = {
    "$ cd /\n": "begin list creation",
    "$ ls\n": "start reading folder contents",
    "dir": "add to dirlist",
    "not$ not dir": "add key with path and value of size",
}
"""

def dir_enumerator(enumeration_input: list) -> dict:
    representation = {}
    _line = []
    current_directory = ""
    for index, line in enumerate(enumeration_input):
        _line = line.split(" ")
        if _line[1] == "cd":
            current_directory = current_directory + _line[2].strip("\n")
            representation[current_directory] = []
            representation[current_directory + "_size"] = []
        elif _line[1].rstrip() == "ls":
            continue
        elif _line[0] == "dir":
            representation[current_directory].append(_line[1].strip("\n"))
        else:
            # list that can be aggregated
            representation[current_directory + "_size"].append(int(_line[0]))
        # else:
        #     representation[current_directory.rstrip("/") + "/" + _line[1].rstrip("\n")] = int(_line[0])
    return representation


def dir_sizer(representation: dict) -> int:
    size_sum = 0
    for key, value in representation.items():
        if "_size" in str(key):
            print("uaaa")
            size_sum += sum(value)
    return size_sum

if __name__ == "__main__":
    with open("./day7/input", "r") as f:
        inputs = f.readlines()
        dirtree = dir_enumerator(inputs)
        print("The combined size of the files in the system is: ", dir_sizer(dirtree))