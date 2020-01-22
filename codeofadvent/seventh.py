from fifth import Intcomputer


def read_commastxt(line):
    inputs = []
    for number in line.split(','):
        inputs.append(int(number))
    return inputs


def test_amplifier(param, computer, inputs, previous):
    output = computer.execute_intcode(inputs, param, previous)
    return output


def number_tolist(number, list):
    number = str(number)
    for i in range(len(list)):
        list[i] = number[i]



f = open("seventh.txt", "r")
inputs_original = read_commastxt(f.readline())
computer = Intcomputer()

tunings = [0, 0, 0, 0, 0]
previous = 0

for _ in range(5):
    inputs = inputs_original.copy()
    previous = test_amplifier(tunings[_], computer, inputs, previous)
