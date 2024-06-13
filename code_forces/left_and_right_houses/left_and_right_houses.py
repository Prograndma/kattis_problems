LEFT = "0"
RIGHT = "1"


def find_i(in_str, str_len):
    num_left = in_str.count("0")
    num_right = str_len - num_left
    num_happy_left = 0
    num_sad_left = 0
    num_happy_right = num_right
    num_sad_right = num_left

    # prev_happiness = num_happy_right - num_sad_right

    if num_sad_left <= num_happy_left and num_sad_right <= num_happy_right:
        max_happiness_location = 0
    else:
        max_happiness_location = -1
    # max_happiness_location = 0
    # max_happiness = prev_happiness
    for i, person in enumerate(in_str):
        if person == RIGHT:
            # prev_happiness -= 2

            num_sad_left += 1
            num_happy_right -= 1
        else:
            # prev_happiness += 2

            num_happy_left += 1
            num_sad_right -= 1

        if num_sad_left <= num_happy_left and num_sad_right <= num_happy_right:
            if max_happiness_location == -1 or abs(max_happiness_location - (str_len / 2.0)) > abs(((i + 1) - str_len / 2.0)):
                max_happiness_location = i + 1
            # max_happiness = prev_happiness

    return max_happiness_location


num_tests = int(input())

for _ in range(num_tests):
    it = int(input())
    print(find_i(input(), it))
