class Arcade:

    def __init__(self):
        self.canvas = [[0 for x in range(40)] for y in range(40)]
        self.counter = 1
        self.positionx = 0
        self.positiony = 0
        self.ballpositionx = 0
        self.paddlepositionx = 0

    def get_tile(self):
        return self.canvas[self.positiony][self.positionx]

    def set_tile(self, tileparam):
        if self.counter == 1:
            self.positionx = tileparam
        elif self.counter == 2:
            self.positiony = tileparam
        elif self.counter == 3:
            if self.positionx == -1 and self.positiony == 0:
                print(tileparam)
            else:
                self.check_blocks(tileparam)
                self.counter = 0
        self.counter += 1

    def check_blocks(self, new_tiletype):
        old_tiletype = self.get_tile()
        if old_tiletype == 0:
            self.canvas[self.positiony][self.positionx] = new_tiletype
        elif (old_tiletype == 2) and (new_tiletype == 4):
            self.canvas[self.positiony][self.positionx] = 0
        # if ball or paddle is being updated
        if new_tiletype == 4:
            self.ballpositionx = self.positionx
        if new_tiletype == 3:
            self.paddlepositionx = self.positionx

    def update_joystick(self):
        if self.ballpositionx < self.paddlepositionx:
            return -1
        elif self.ballpositionx > self.paddlepositionx:
            return 1
        else:
            return 0


class Intcomputer:

    def __init__(self):
        self.counter = 0
        self.relative_base = 0
        self.arcade = Arcade()

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

    def execute_intcode(self, inputs):
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
                inputs[params[0]] = self.arcade.update_joystick()
                self.counter += 2

            elif opcode == 4:
                self.arcade.set_tile(inputs[params[0]])
                self.counter += 2

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

        return self.arcade.canvas


class Robot:

    def __init__(self):
        self.canvas = [[0 for x in range(100)] for y in range(100)]
        self.canvas[50][50] = 1
        self.angle = 0
        self.positionx = 50
        self.positiony = 50
        self.counter = {(0, 0)}

    def get_colour(self):
        return self.canvas[self.positiony][self.positionx]

    def set_colour(self, colour):
        self.counter.add((self.positiony, self.positionx))
        self.canvas[self.positiony][self.positionx] = colour

    def set_position(self, direction):
        angles_movement = {
            0: (-1, 0),
            90: (0, 1),
            180: (1, 0),
            270: (0, -1)
        }
        self.set_angle(direction)
        self.positiony += angles_movement[self.angle][0]
        self.positionx += angles_movement[self.angle][1]

    # 0 = left, 1 = right
    def set_angle(self, direction):
        if direction == 0:
            self.angle -= 90
        elif direction == 1:
            self.angle += 90
        self.angle = self.angle % 360
