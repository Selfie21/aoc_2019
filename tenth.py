def read_map(file):
    map = []
    graph = []
    for line in file.read().splitlines():
        for c in line:
            graph.append(c)
        map.append(graph)
        graph = []
    return map


class Map:

    def __init__(self, x_max, y_max):
        self.x_max = x_max
        self.y_max = y_max

    def check_bound(self, x, y):
        if x < 0 or y < 0:
            return False
        elif x > self.x_max or y > self.y_max:
            return False
        else:
            return True

    def check_asteroid(self, inputs):
        for x in range(len(inputs)):
            for y in range(len(inputs[0])):
                if inputs[x][y] == '#':
                    print(x, y, self.check_straight(inputs, x, y))

    def check_straight(self, inputs, x, y):
        bounds = [y+1, y-1, x+1, x-1]               #right, left, down, up

        while self.check_bound(x, bounds[0]) and inputs[x][bounds[0]] != '#':
            bounds[0] += 1
            if not(self.check_bound(x, bounds[0])):
                bounds[0] = -1
                break

        while self.check_bound(x, bounds[1]) and inputs[x][bounds[1]] != '#':
            bounds[1] -= 1
            if not(self.check_bound(x, bounds[1])):
                bounds[1] = -1
                break

        while self.check_bound(bounds[2], y) and inputs[bounds[2]][y] != '#':
            bounds[2] += 1
            if not(self.check_bound(bounds[2], y)):
                bounds[2] = -1
                break

        while self.check_bound(bounds[3], y) and inputs[bounds[3]][y] != '#':
            bounds[3] -= 1
            if not(self.check_bound(bounds[3], y)):
                bounds[2] = -1
                break

        return bounds

    def check_angles(self, inputs, bounds, x, y):
        pass







inputs = read_map(open("tenth.txt", "r"))
map = Map(len(inputs[0])-1, len(inputs)-1)
map.check_asteroid(inputs)