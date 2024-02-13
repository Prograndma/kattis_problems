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


def get_sum(segment_tree, n, qs, qe):
    if qs < 0 or qe > n - 1 or qs > qe:
        print("Invalid Input", end="")
        return 0
    return get_sum_util(segment_tree, 0, n - 1, qs, qe, 0)


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
        print("Invalid Input", end="")
        return
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
    # Maximum size of segment tree
    max_size = 2 * int(2 ** x) - 1

    # Allocate memory
    segment_tree = [0] * max_size

    # Fill the allocated memory segment_tree
    construct_segment_tree_util(base_array, 0, array_len - 1, segment_tree, 0)
    return segment_tree


def custy_xor(thing):
    return int(bool(thing) != bool(1))


[bits, num] = input().split()
bits = int(bits)
num = int(num)
arr_me_matey = [0] * bits
tree = construct_segment_tree(arr_me_matey)

for _ in range(num):
    inputs = input().split()
    if inputs[0] == "F":
        update_value(arr_me_matey, tree, int(inputs[1]), custy_xor(arr_me_matey[int(inputs[1])]))
    else:
        start = int(inputs[1])
        end = int(inputs[2])
        print(get_sum(tree, bits, start, end))
