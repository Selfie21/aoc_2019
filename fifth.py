from utility import Utility

class Intcomputer:

    def __init__(self):
        self.counter = 0
        self.relative_base = 0

    def get_setting(self, inputs):
        modes = ''
        opcode = str(inputs[self.counter])[-2:]
        if len(str(inputs[self.counter])) > 2:
            modes = str(inputs[self.counter])[0:-2]
        return int(opcode), modes

    def get_parameters(self, inputs, modes):
        params = [inputs[self.counter+1], inputs[self.counter+2], inputs[self.counter+3]]
        for i in range(len(modes)):
            if modes[-(i+1)] == '1':
                if i != 2:
                    params[i] = self.counter + i + 1
            if modes[-(i+1)] == '2':
                params[i] = self.relative_base + inputs[self.counter + i + 1]
        return params

    def execute_intcode(self, inputs, previous_output):
        opcode = 0

        while not(opcode == 99):
            opcode, modes = self.get_setting(inputs)
            params = self.get_parameters(inputs, modes)
            if opcode == 1:
                inputs[params[2]] = inputs[params[0]] + inputs[params[1]]
                self.counter += 4

            elif opcode == 2:
                inputs[params[2]] = inputs[params[0]] * inputs[params[1]]
                self.counter += 4

            elif opcode == 3:
                inputs[params[0]] = previous_output
                self.counter += 2

            elif opcode == 4:
                self.counter += 2
                return inputs[params[0]]

            elif opcode == 5:
                self.counter = inputs[params[1]] if inputs[params[0]] != 0 else self.counter + 3

            elif opcode == 6:
                self.counter = inputs[params[1]] if inputs[params[0]] == 0 else self.counter + 3

            elif opcode == 7:
                inputs[params[2]] = 1 if inputs[params[0]] < inputs[params[1]] else 0
                self.counter += 4

            elif opcode == 8:
                inputs[params[2]] = 1 if inputs[params[0]] == inputs[params[1]] else 0
                self.counter += 4

            elif opcode == 9:
                self.relative_base += inputs[params[0]]
                self.counter += 2

        return None
