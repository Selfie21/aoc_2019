from fifth import Intcomputer
from utility import Utility


def test_amplifier(param, computer, inputs, previous):
    output = computer.execute_intcode(inputs, param, previous)
    return output


def get_permutation(current, mod):
    contains_doubles = True
    while contains_doubles:
        for i in range(5):
            if current[i] < mod:
                current[i] += 1
                break
            else:
                current[i] = 0
        contains_doubles = check_doubles(current)


def check_doubles(current):

    for i in range(5):
        instances = 0
        tocheck = current[i]
        for i in range(5):
            if current[i] == tocheck:
                instances += 1
        if instances > 1:
            return True
    return False


f = open("seventh.txt", "r")
inputs_original = Utility.read_commastxt(f.readline())
computer = Intcomputer(0, 0)


# First Exercise
tunings = [0, 0, 0, 0, 0]
previous = 0
maximum = 0

for i in range(256):
    previous = 0
    for _ in range(5):
        computer.counter = 0
        inputs = inputs_original.copy()
        previous = test_amplifier(tunings[_], computer, inputs, previous)
    if maximum < previous:
        maximum = previous
    get_permutation(tunings, 4)


# Second Exercise
tunings = [0, 0, 0, 0, 0]
previous = second = 0
inputs = inputs_original.copy()
last_halt = True
tapes = []
parameters = []


for i in range(5):
    tapes.append(inputs_original.copy())
    parameters.append([tunings[i], tunings[i], Intcomputer()])
parameters[0][1] = 0


while last_halt:
    for _ in range(5):
        if not(previous is None):

            previous = test_amplifier(parameters[_][0], parameters[_][2], tapes[_], parameters[_][1])
            parameters[(_+1) % 5][0] = parameters[(_+1) % 5][1]
            parameters[(_+1) % 5][1] = previous
            if not(previous is None):
                second = previous
        else:
            last_halt = False


Utility.print_solution(maximum, second)
