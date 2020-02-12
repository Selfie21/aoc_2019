from intcomputer import Intcomputer
from utility import Utility


def count_twodim(new_list, item):
    counter = 0
    for row in new_list:
        counter += row.count(item)
    return counter


f = open("thirteenth.txt", "r")
inputs_original = Utility.read_commastxt(f.readline())
Utility.enlarge_list(10000, inputs_original)
inputs_original[0] = 2
computer = Intcomputer()

gameboard = computer.execute_intcode(inputs_original)
first = count_twodim(gameboard, 2)
print(first)
