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
        for coordinate in inputs:
            if coordinate == '#':



inputs = read_map(open("tenth.txt", "r"))
map = Map(len(inputs[0]), len(inputs))