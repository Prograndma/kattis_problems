import math


def circle_dist(list_one, list_two):
    x1, y1, r1 = list_one
    x2, y2, r2 = list_two
    return math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2)) - (r1 + r2)


num_inputs = int(input())
circles = []
for _ in range(num_inputs):
    circles.append(list(map(int, input().split())))

total_dist = 0

for i, circle_one in enumerate(circles):
    minimum = math.inf
    for j, circle_two in enumerate(circles):
        if i == j:
            continue
        distance = circle_dist(circle_one, circle_two)
        if distance < minimum:
            minimum = distance
    total_dist += minimum


print(total_dist)
