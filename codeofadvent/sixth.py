def read_linestxt(file):
    return file.read().splitlines()


f = open("sixth.txt", "r")


first = []
second = []
for line in read_linestxt(f):
    first.append(line.split(')')[0])
    second.append(line.split(')')[1])


queue = []
counter = 0
increment = 0
next_layer = ""
queue.append("COM")
new_layer = True

while len(queue) > 0:
    indices = [i for i, x in enumerate(first) if x == queue[0]]

    for _ in indices:
        queue.append(second[_])
        counter += increment
        if new_layer:
            next_layer = second[_]

    new_layer = False


    if next_layer == queue[0]:
        increment += 1
        new_layer = True
    queue.pop(0)

    print(counter)

