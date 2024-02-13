from math import ceil, log2


def get_mid(s, e):
    return s + (e - s) // 2


def get_sum_util(segment_tree, ss, se, qs, qe, si):
    if qs <= ss and qe >= se:
        return segment_tree[si]
    if se < qs or ss > qe:
        return 0
    mid = get_mid(ss, se)
    return get_sum_util(segment_tree, ss, mid, qs, qe, 2 * si + 1) + get_sum_util(segment_tree, mid + 1, se, qs, qe, 2 * si + 2)


def get_sum(segment_tree, n, query_start, query_end):
    if query_start < 0 or query_end > n - 1 or query_start > query_end:
        raise Exception(f"Invalid Input! n={n} start:{query_start} - end:{query_end}")
    return get_sum_util(segment_tree, 0, n - 1, query_start, query_end, 0)


def update_value_util(segment_tree, ss, se, i, diff, si):
    if i < ss or i > se:
        return

    segment_tree[si] = segment_tree[si] + diff

    if se != ss:
        mid = get_mid(ss, se)
        update_value_util(segment_tree, ss, mid, i, diff, 2 * si + 1)
        update_value_util(segment_tree, mid + 1, se, i, diff, 2 * si + 2)


def update_value(base_array, segment_tree, where, new_val):
    base_len = len(base_array)
    if where < 0 or where > base_len - 1:
        raise Exception(f"Invalid Input! where: {where} What value? {new_val}")
    diff = new_val - base_array[where]

    # Update the value in array
    base_array[where] = new_val

    # Update the values of nodes in segment tree
    update_value_util(segment_tree, 0, base_len - 1, where, diff, 0)


def construct_segment_tree_util(base_array, ss, se, segment_tree, current_index):
    if ss == se:
        segment_tree[current_index] = base_array[ss]
        return base_array[ss]
    mid = get_mid(ss, se)

    segment_tree[current_index] = (construct_segment_tree_util(base_array, ss, mid, segment_tree, current_index * 2 + 1)
                                   + construct_segment_tree_util(base_array, mid + 1, se, segment_tree, current_index * 2 + 2))

    return segment_tree[current_index]


def construct_segment_tree(base_array):
    # Allocate memory for the segment tree
    # Height of segment tree
    array_len = len(base_array)
    x = int(ceil(log2(array_len)))
    # print(f"X: {x}")
    # Maximum size of segment tree
    max_size = 2 * int(2 ** x) - 1
    # print(f"{max_size=}")
    # Allocate memory
    segment_tree = [0] * max_size

    # Fill the allocated memory segment_tree
    construct_segment_tree_util(base_array, 0, array_len - 1, segment_tree, 0)
    return segment_tree


def getInvCount(arr):
    n = len(arr)
    invcount = 0  #Initialize result
    for i in range(0, n-1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                for k in range(j + 1, n):
                    if arr[j] > arr[k]:
                        invcount += 1
    return invcount


highest_num = int(input())
base_seen_array_len = highest_num + 2
un_sorted = input().split()
un_sorted = [int(x) for x in un_sorted]

numbers_seen_left = [0] * base_seen_array_len
numbers_seen_right = [0] * base_seen_array_len
left_tree = construct_segment_tree(numbers_seen_left)
right_tree = construct_segment_tree(numbers_seen_right)
sum = 0
things_greater_to_my_left = [0] * highest_num
things_lesser_to_my_right = [0] * highest_num

for left_index in range(len(un_sorted)):
    right_index = len(un_sorted) - (left_index + 1)
    current_number_from_left = un_sorted[left_index]
    current_number_from_right = un_sorted[right_index]
    times_ive_seen_current_number_left = numbers_seen_left[current_number_from_left]
    times_ive_seen_current_number_right = numbers_seen_right[current_number_from_right]

    num_ive_seen_greater = get_sum(left_tree, base_seen_array_len, current_number_from_left + 1, highest_num + 1)
    things_greater_to_my_left[left_index] = num_ive_seen_greater
    update_value(numbers_seen_left, left_tree, current_number_from_left, times_ive_seen_current_number_left + 1)

    num_ive_seen_lesser = get_sum(right_tree, base_seen_array_len, 0, current_number_from_right - 1)
    things_lesser_to_my_right[right_index] = num_ive_seen_lesser
    update_value(numbers_seen_right, right_tree, current_number_from_right, times_ive_seen_current_number_right + 1)

total_inversions = 0
for i in range(len(un_sorted)):
    total_inversions += things_greater_to_my_left[i] * things_lesser_to_my_right[i]

print(total_inversions)
# print(f"Wrong: {total_inversions}")
# print(f"Right: {getInvCount(un_sorted)}")


# print(things_greater_to_my_left)
# print(things_lesser_to_my_right)
# print(f"Len of left tree: {len(left_tree)}")
