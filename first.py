f = open("first.txt", "r")
input = []
sum = 0

for line in f:
    if line is not '\n':
        input.append(int(line))

for x in input:
    s = int(x/3)-2
    sum += s
    while int(s / 3) - 2 > 0:
        s = int(s / 3) - 2
        sum += s

print(sum)
f.close()
