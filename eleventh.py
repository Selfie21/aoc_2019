from intcomputer import Intcomputer
from utility import Utility

# For the first change starting tile of robot to 0
f = open("eleventh.txt", "r")
inputs_original = Utility.read_commastxt(f.readline())
Utility.enlarge_list(10000, inputs_original)
computer = Intcomputer()

solutions = computer.execute_intcode(inputs_original.copy())
first = solutions[0]

Utility.print_solution(len(first)-1, ':')

for line in solutions[1]:
    buffer = ''
    for c in line:
        if c == 0:
            buffer += ' '
        elif c == 1:
            buffer += '#'
    print(buffer)

