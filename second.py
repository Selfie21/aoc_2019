def read_commastxt(line):
    inputs = []
    for number in line.split(','):
        inputs.append(int(number))
    return inputs


def print_solution(first, second):
    print("First: " + str(first) + ", Second " + str(second))


# First Exercise
def execute_intcode(inputs):
    counter = opcode = 0

    while not(opcode == 99):
        opcode = inputs[counter]
        first_param = inputs[counter + 1]
        second_param = inputs[counter + 2]

        if opcode is 1:
            inputs[inputs[counter + 3]] = inputs[first_param] + inputs[second_param]

        if opcode is 2:
            inputs[inputs[counter + 3]] = inputs[first_param] * inputs[second_param]
        counter += 4
    return inputs[0]


# Second Exercise
def change_noun_verb(noun, verb):
    if verb > 99:
        noun += 1
        return noun, 0
    else:
        verb += 1
        return noun, verb


def reiterate_intcode(inputs_stock):
    output = noun = verb = 0
    inputs = []

    while not(output == 19690720):
        inputs = inputs_stock.copy()
        noun, verb = change_noun_verb(noun, verb)

        inputs[1] = noun
        inputs[2] = verb
        output = execute_intcode(inputs)
    return noun, verb


f = open("second.txt", "r")
line = f.readline()
inputs_stock = read_commastxt(line)
inputs = inputs_stock.copy()
first = execute_intcode(inputs)

inputs_stock[1] = inputs_stock[2] = 0
noun, verb = reiterate_intcode(inputs_stock)
second = 100*noun + verb
print_solution(inputs[0], second)
