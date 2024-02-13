from math import ceil, log2


def build(arr, tree):
    for n in range(base_seen_array_len):
        tree[base_seen_array_len + n] = arr[n]
    for n in range(base_seen_array_len - 1, 0, -1):
        tree[n] = tree[n << 1] + tree[n << 1 | 1]


def update_tree_node(where, value, tree):
    tree[where + base_seen_array_len] = value
    where = where + base_seen_array_len
    current = where
    while current > 1:
        tree[current >> 1] = tree[current] + tree[current ^ 1]
        current >>= 1


def query(query_start, query_end, tree):

    res = 0

    query_start += base_seen_array_len
    query_end += base_seen_array_len

    while query_start < query_end:

        if query_start & 1:
            res += tree[query_start]
            query_start += 1

        if query_end & 1:
            query_end -= 1
            res += tree[query_end]

        query_start >>= 1
        query_end >>= 1

    return res


def get_inv_count_slow_but_accurate(arr):
    n = len(arr)
    inv_count = 0
    for z in range(0, n-1):
        for j in range(z + 1, n):
            if arr[z] > arr[j]:
                for k in range(j + 1, n):
                    if arr[j] > arr[k]:
                        inv_count += 1
    return inv_count


highest_num = int(input())
base_seen_array_len = highest_num + 2
un_sorted = input().split()
un_sorted = [int(x) for x in un_sorted]

x = int(ceil(log2(base_seen_array_len)))
max_size = 2 * int(2 ** x) - 1

numbers_seen_left = [0] * base_seen_array_len
numbers_seen_right = [0] * base_seen_array_len
left_tree = [0] * max_size
right_tree = [0] * max_size
build(numbers_seen_left, left_tree)
build(numbers_seen_right, right_tree)

things_greater_to_my_left = [0] * highest_num
things_lesser_to_my_right = [0] * highest_num

for left_index in range(len(un_sorted)):
    right_index = len(un_sorted) - (left_index + 1)
    current_number_from_left = un_sorted[left_index]
    current_number_from_right = un_sorted[right_index]
    times_ive_seen_current_number_left = numbers_seen_left[current_number_from_left]
    times_ive_seen_current_number_right = numbers_seen_right[current_number_from_right]

    num_ive_seen_greater = query(current_number_from_left + 1, highest_num + 1, left_tree)
    things_greater_to_my_left[left_index] = num_ive_seen_greater
    update_tree_node(current_number_from_left, times_ive_seen_current_number_left + 1, left_tree)
    numbers_seen_left[current_number_from_left] += 1

    num_ive_seen_lesser = query(0, current_number_from_right, right_tree)
    things_lesser_to_my_right[right_index] = num_ive_seen_lesser
    update_tree_node(current_number_from_right, times_ive_seen_current_number_right + 1, right_tree)
    numbers_seen_right[current_number_from_right] += 1

total_inversions = 0
for i in range(len(un_sorted)):
    total_inversions += things_greater_to_my_left[i] * things_lesser_to_my_right[i]

print(total_inversions)

