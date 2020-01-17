# Exercise 1
def find_dupes(num1):
    value = False
    array1 = list(str(num1))
    for x in range(0, 5):
        if (array1[x] == array1[x + 1]):
            value = True
            break
    return value


def find_down(num1):
    value = True
    array1 = list(str(num1))
    for x in range(0, 5):
        if (array1[x] > array1[x + 1]):
            value = False
            break
    return value


count = 0

for i in range(165432, 707912):
    if find_dupes(i) and find_down(i):
        count += 1
print(count)


# Exercise 2
c = 0
for i in range(165432, 707912 + 1):

    inc, doub = True, False
    d_old = None
    while i > 0:
        d = i % 10
        i = i // 10
        d_ = i % 10

        if d_ > d:
            inc = False
            break

        if d_ == d and not ((i // 10) % 10 == d or d == d_old):
            doub = True
        d_old = d

    if not (inc and (doub == 1)):
        continue
    c += 1
print(c)
