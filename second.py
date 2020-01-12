f = open("second.txt", "r")
input = []
inputori = []
s = f.readline()
i = 0
counter = 0
opcode = 0
verb = 0
noun = 0

for i in s.split(','):
    i = int(i)
    inputori.append(i)

input = inputori.copy()

while input[0] != 19690720:

    input = inputori.copy()
    opcode = 0
    counter = 0
    input[1] = noun
    input[2] = verb

    while opcode is not 99:
        opcode = input[counter]

        if opcode is 1:
            input[input[counter+3]] = input[input[counter+1]] + input[input[counter+2]]

        if opcode is 2:
            input[input[counter+3]] = input[input[counter+1]] * input[input[counter+2]]
        counter += 4

    noun += 1
    if noun is 100:
        noun = 0
        verb += 1

print(str(noun) + " " + str(verb))

