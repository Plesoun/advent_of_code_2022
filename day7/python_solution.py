import logging

L = logging.getLogger(__name__)

"""
representation = {
    "/": ["folder1", "folder2", "folder3"],
    "/folder1": ["folder4"],
    "folder1/file.1": 321741,
}
"""

decider_matrix = {
    "$ cd /\n": "begin list creation",
    "$ ls\n": "start reading folder contents",
    "dir": "add to dirlist",
    "not$ not dir": "add key with path and value of size",
}

def dir_enumerator(enumeration_input: list) -> dict:
    print("\n>>>>>>", enumeration.index("$ cd /\n"))
    for i in enumeration_input:



def dir_sizer(representation: dict) -> int:
    pass