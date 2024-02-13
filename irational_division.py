def get_score(h, w):
    if h == 1 and w == 1:
        return -1

    if h == 1:
        if w % 2 == 0:
            return 2

        return 1

    if w == 1:
        if h % 2 == 0:
            return 0

        return -1

    if h % 2 == 1 and w % 2 == 1:
        return 1
    if h % 2 == 0:
        return 0
    if w > h:
        return 2

    return 0


nums = input().split()

h = int(nums[0])
w = int(nums[1])

score = get_score(h, w)

print(score)