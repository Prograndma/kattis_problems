import sys


def min_max_range(line):
    how_many = int(line[0])
    max = -1000001
    min = 1000001
    for i in range(1, how_many + 1):
        if int(line[i]) > max:
            max = int(line[i])
        if int(line[i]) < min:
            min = int(line[i])

    return min, max, max - min


lines = ["2 4 10\n",
         "9 2 5 6 4 5 9 2 1 4\n",
         "7 6 10 1 2 5 10 9\n",
         "1 9\n"]

for i, line in enumerate(lines):
    line = line.strip().split()
    min, max, rangey = min_max_range(line)

    print(f"Case {i + 1}: {min} {max} {rangey}")