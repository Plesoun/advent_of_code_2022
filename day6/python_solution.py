import logging

L = logging.getLogger(__name__)

def start_of_packet_filter(input_signal:str, window:int) -> int:
    datastream = []
    for index, letter in enumerate(input_signal):
        datastream.append(letter)
        if len(set(datastream[-abs(window):])) == window:
            return index + 1
    return 0


if __name__ == "__main__":
    with open("./day6/input", "r") as f:
        in_put = f.readlines()[0]
        print(in_put)
        print("Initial packet starts at: ", start_of_packet_filter(in_put, 4))
        print("Initial message starts at: ", start_of_packet_filter(in_put, 14))