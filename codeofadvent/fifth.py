def read_commastxt(line):
    inputs = []
    for number in line.split(','):
        inputs.append(int(number))
    return inputs


def print_solution(first, second):
    print("First: " + str(first) + ", Second " + str(second))


class Intcomputer:

    def __init__(self):
        pass

    def get_setting(self, inputs, counter):
        modes = ''
        opcode = str(inputs[counter])[-1:]
        if len(str(inputs[counter])) > 2:
            modes = str(inputs[counter])[0:-2]
        return int(opcode), modes

    def get_parameters(self, inputs, counter, modes):
        params = [inputs[counter+1], inputs[counter+2], inputs[counter+3]]
        for i in range(len(modes)):
            if modes[-(i+1)] == '1':
                params[i] = counter + i + 1
        return params

    def execute_intcode(self, inputs, enviroment, previous_output):
        counter = opcode = 0
        firstInput = True

        while not(opcode == 9) and counter < len(inputs)-2:
            opcode, modes = self.get_setting(inputs, counter)
            params = self.get_parameters(inputs, counter, modes)

            if opcode == 1:
                inputs[inputs[counter + 3]] = inputs[params[0]] + inputs[params[1]]
                counter += 4

            elif opcode == 2:
                inputs[inputs[counter + 3]] = inputs[params[0]] * inputs[params[1]]
                counter += 4

            elif opcode == 3:
                inputs[params[0]] = enviroment if firstInput else previous_output
                firstInput = False
                counter += 2

            elif opcode == 4:
                return inputs[params[0]]

            elif opcode == 5:
                counter = inputs[params[1]] if inputs[params[0]] != 0 else counter + 3

            elif opcode == 6:
                counter = inputs[params[1]] if inputs[params[0]] == 0 else counter + 3

            elif opcode == 7:
                inputs[inputs[counter + 3]] = 1 if inputs[params[0]] < inputs[params[1]] else 0
                counter += 4

            elif opcode == 8:
                inputs[inputs[counter + 3]] = 1 if inputs[params[0]] == inputs[params[1]] else 0
                counter += 4

        return inputs[0]


f = open("fifth.txt", "r")
inputs = read_commastxt(f.readline())
computer = Intcomputer()
computer.execute_intcode(inputs)
