from utility import Utility


def find_minimumchars(layers, charac):
    index = 0
    minimum = layers[0].count(charac)
    for i in range(len(layers)):
        if minimum > layers[i].count(charac):
            minimum = layers[i].count(charac)
            index = i
    return index


def get_final_pixel(layers, position):
    for layer in layers:
        if layer[position] != '2':
            return layer[position]
    return '2'


def convert_pixels(image):
    new_image = ''
    for _ in range(len(image)):
        if image[_] == '0':
            new_image += ' '
        elif image[_] == '1':
            new_image += '#'
        elif image[_] == '2':
            new_image += ' '
    return new_image


f = open("eigth.txt", "r")
layers = []
layerstring = ''
width = 25
height = 6
pixels_per_layer = width * height

# First Exercise
counter = 0
for x in f.readline():
    if counter >= pixels_per_layer:
        layers.append(layerstring)
        layerstring = ''
        counter = 0
    layerstring += str(x)
    counter += 1
layers.append(layerstring)
index = find_minimumchars(layers, '0')
first = layers[index].count('1') * layers[index].count('2')

# Second Exercise
# 0 Black 1 White 2 Transparent
final_image = ''
counter = row = 0
for pixel in range(len(layers[0])):
    final_image += get_final_pixel(layers, pixel)
final_image = convert_pixels(final_image)

Utility.print_solution(first, ':')
while counter < height:
    print(final_image[row:row+width])
    row += width
    counter += 1


