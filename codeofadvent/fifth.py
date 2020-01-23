def read_commastxt(line):
    inputs = []
    for number in line.split(','):
        inputs.append(int(number))
    return inputs


def print_solution(first, second):
    print("First: " + str(first) + ", Second " + str(second))


class Intcomputer:

    def __init__(self, counter):
        self.counter = counter

    def get_setting(self, inputs):
        modes = ''
        opcode = str(inputs[self.counter])[-1:]
        if len(str(inputs[self.counter])) > 2:
            modes = str(inputs[self.counter])[0:-2]
        return int(opcode), modes

    def get_parameters(self, inputs, modes):
        params = [inputs[self.counter+1], inputs[self.counter+2], inputs[self.counter+3]]
        for i in range(len(modes)):
            if modes[-(i+1)] == '1':
                params[i] = self.counter + i + 1
        return params

    def execute_intcode(self, inputs, enviroment, previous_output):
        opcode = 0
        firstInput = True

        while not(opcode == 9) and self.counter < len(inputs)-2:
            opcode, modes = self.get_setting(inputs)
            params = self.get_parameters(inputs, modes)

            if opcode == 1:
                inputs[inputs[self.counter + 3]] = inputs[params[0]] + inputs[params[1]]
                self.counter += 4

            elif opcode == 2:
                inputs[inputs[self.counter + 3]] = inputs[params[0]] * inputs[params[1]]
                self.counter += 4

            elif opcode == 3:
                inputs[params[0]] = enviroment if firstInput else previous_output
                firstInput = False
                self.counter += 2

            elif opcode == 4:
                self.counter += 2
                return inputs[params[0]]

            elif opcode == 5:
                self.counter = inputs[params[1]] if inputs[params[0]] != 0 else self.counter + 3

            elif opcode == 6:
                self.counter = inputs[params[1]] if inputs[params[0]] == 0 else self.counter + 3

            elif opcode == 7:
                inputs[inputs[self.counter + 3]] = 1 if inputs[params[0]] < inputs[params[1]] else 0
                self.counter += 4

            elif opcode == 8:
                inputs[inputs[self.counter + 3]] = 1 if inputs[params[0]] == inputs[params[1]] else 0
                self.counter += 4

        return None


f = open("fifth.txt", "r")
inputs = read_commastxt(f.readline())