def naive(s):
    n_operations = 0
    while "1" in s:
        if s[-1] == "0":
            n_operations += 1
            s = s[:-1]
        else:
            n_operations += 1
            s = s[:-1] + "0"
    return n_operations


def my_way(s):
    num_ones = 0
    num_zeroes = 0
    temp_zeroes = 0
    for char in reversed(s):
        if char == "1":
            num_ones += 1
            num_zeroes += temp_zeroes
            temp_zeroes = 0
        else:
            temp_zeroes += 1

    if num_ones == 0:
        return 0
    return num_zeroes + (2 * num_ones) - 1


def fuzz():
    for i in range(1_000_000_000):
        inp = format(i, '064b')
        if naive(inp) != my_way(inp):
            print(f"MISMATCH\ninput: {inp}\n{naive(inp)} <- naive\n{my_way(inp)} <- my way\n")


if __name__ == "__main__":
    fuzz()