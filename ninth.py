from fifth import Intcomputer
from utility import Utility


def enlarge_list(offset, list):
    for i in range(offset):
        list.append(0)


f = open("ninth.txt", "r")
inputs_original = Utility.read_commastxt(f.readline())
enlarge_list(10000, inputs_original)
inputs_2 = inputs_original.copy()
computer1 = Intcomputer()
computer2 = Intcomputer()

first = computer1.execute_intcode(inputs_original.copy(), 1)
second = computer2.execute_intcode(inputs_2, 2)
Utility.print_solution(first, second)

