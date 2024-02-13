import math


def pythag(width, first, second):
    diff = abs(first - second)
    if diff == 0:
        return width
    return math.sqrt((width * width) + (diff * diff))


def max_dist(width, first, second, r):
    if first - r == 0 and second - r == 0:
        return pythag(width, first, second)
    width_divis = (first - r) / ((second - r) + (first - r))
    other_divis = (second - r) / ((second - r) + (first - r))
    return (pythag(width * other_divis, r, second)) + (pythag(width * width_divis, first, r))


def do_stuff(width, first_height, second_height, r):
    min_dist = pythag(width, first_height, second_height)

    max_dizzy = max_dist(width, first_height, second_height, r)

    print("%.8f" % min_dist, end=" ")
    print("%.8f" % max_dizzy)


num_input = int(input())
for _ in range(num_input):
    things = input().split()
    do_stuff(int(things[0]), int(things[1]), int(things[2]), int(things[3]))