import math
def h(width, first_height, second_height):
    diff=abs(first_height-second_height)
    if diff==0:
        return width
    return math.sqrt((width*width)+(diff*diff))
total_inputs = int(input())
for _ in range(total_inputs):
    [width, first_height, second_height, rider_height] = input().split()
    width=int(width)
    first_height=int(first_height)
    second_height=int(second_height)
    rider_height=int(rider_height)
    min_len = h(width, first_height, second_height)
    if first_height-rider_height==0 and second_height-rider_height==0:
        max_len=h(width, first_height, second_height)
    else:
        max_len= (h(width * ((second_height - rider_height) / ((second_height - rider_height) + (first_height - rider_height))), rider_height, second_height)) + (h(width * ((first_height - rider_height) / ((second_height - rider_height) + (first_height - rider_height))), first_height, rider_height))
    print("%.8f" % min_len, end=" ")
    print("%.8f" % max_len)