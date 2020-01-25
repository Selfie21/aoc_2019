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
inputs_2 = inputs_original.copy()
computer1 = Intcomputer()
computer2 = Intcomputer()

first = computer1.execute_intcode(inputs_original.copy(), 1, 1)
second = computer2.execute_intcode(inputs_2, 2, 2)
print_solution(first, second)

