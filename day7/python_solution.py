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
    print("\n>>>>>>", enumeration_input)
    representation = {}
    _line = []
    current_directory = ""
    for index, line in enumerate(enumeration_input):
        _line = line.split(" ")
        if _line[1] == "cd":
            current_directory = current_directory + _line[2].strip("\n")
            representation[current_directory] = []
        elif _line[1].rstrip() == "ls":
            continue
        elif _line[0] == "dir":
            representation[current_directory].append(_line[1].strip("\n"))
        else:
            representation[current_directory.rstrip("/") + "/" + _line[1].rstrip("\n")] = int(_line[0])
    return representation


def dir_sizer(representation: dict) -> int:
    pass