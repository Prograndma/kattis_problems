
def pre_process(arr):
    interesting_indices = []
    for j in range(1, len(arr)):
        if arr[j] != arr[j - 1]:
            interesting_indices.append(j)
    return interesting_indices


def find_closest_index(arr, lower_bound):
    n = len(arr) - 1
    result = arr[0]
    if result > lower_bound:
        return 0
    if n < 2:
        return 0
    result = arr[1]
    index = 1
    while result < lower_bound:
        index += 100
        if index >= n:
            return index - 100
        result = arr[int(index)]
    return index - 100


num_arrays = int(input())

for _ in range(num_arrays):
    array_size = int(input())
    array = list(map(int, input().split()))
    num_queries = int(input())
    swaps = pre_process(array)
    for _ in range(num_queries):
        query = list(map(int, input().split()))
        do_print = True
        start = find_closest_index(swaps, query[0] - 1)
        for b in range(int(start), len(swaps)):
            swap = swaps[b]
            if swap > query[1]:
                break
            if query[0] - 1 < swap < query[1]:
                print(query[0], swap + 1)
                do_print = False
                break
        if do_print:
            print(-1, -1)
