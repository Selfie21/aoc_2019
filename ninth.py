from fifth import Intcomputer

def read_commastxt(line):
    inputs = []
    for number in line.split(','):
        inputs.append(int(number))
    return inputs


def print_solution(first, second):
    print("First: " + str(first) + ", Second " + str(second))


def enlarge_list(offset, list):
    for i in range(offset):
        list.append(0)


f = open("ninth.txt", "r")
inputs_original = read_commastxt(f.readline())
enlarge_list(10000, inputs_original)
computer = Intcomputer(0, 0)
computer.execute_intcode(inputs_original, 1, 1)
