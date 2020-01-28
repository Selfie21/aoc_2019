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
        maximum = 0
        for x in range(len(inputs)):
            for y in range(len(inputs[0])):
                if inputs[x][y] == '#':
                    test = self.check_angles(inputs, x, y)
                    if test[0] > maximum:
                        maximum = test[0]
                        print(test)


    def check_angles(self, inputs, x, y):
        angles = []
        points = []

        for x_new in range(len(inputs)):
            for y_new in range(len(inputs[0])):
                if inputs[x_new][y_new] == '#' and x_new-x != 0:
                    angle = (y_new-y)/(x_new-x) if x_new-x != 0 else 180
                    if angle not in angles:
                        angles.append(angle)
                        distance = (x_new - x) + (y_new - y)
                        points.append((x_new, y_new, distance))
                    else:
                        distance = (x_new - x) + (y_new - y)
                        if distance < points[angles.index(angle)][2]:
                            points[angles.index(angle)] = (x_new, y_new, distance)
        return len(angles), x, y






inputs = read_map(open("tenth.txt", "r"))
map = Map(len(inputs[0])-1, len(inputs)-1)
map.check_asteroid(inputs)