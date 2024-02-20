base = 29
MOD = 1_000_000_007

def numify(char):
    return ord(char) - 96


def little_hash(in_str):
    in_str = [int(ord(c)-96) for c in in_str]
    n = len(in_str)
    result = 0
    for i in range(n):
        result += in_str[i]
        result *= base
    return result



def new_hashing(in_str, length_of_hash):
    MOD = 1_000_000_007
    BASE = 29
    MAX_POW = pow(BASE, length_of_hash - 1, MOD)
    s = [int(ord(c) - 96) for c in in_str]

    # Compute the initial hash value for the first substring of length length_of_hash
    hashes = set([])
    cur_hash = 0
    for i in range(length_of_hash):
        cur_hash = (cur_hash * BASE + s[i]) % MOD
    hashes.add(cur_hash)

    # Update hash values for subsequent substrings
    for i in range(length_of_hash, len(s)):
        # Update cur_hash using the rolling hash formula you provided
        cur_hash = ((cur_hash - s[i - length_of_hash] * MAX_POW) * BASE + s[i]) % MOD
        hashes.add(cur_hash)
    return hashes


def hash_len(in_str, length_of_hash):
    hashes = set([])

    for i in range(len(in_str) - length_of_hash + 1):
        hashes.add(little_hash(in_str[i: i + length_of_hash]) % MOD)

    return hashes


def len_intersection(lists):
    final_set = lists[0]
    for i in range(1, len(lists)):
        final_set = lists[i] & final_set
        if len(final_set) == 0:
            return 0
    return len(final_set)


def find_longest_sub_str(strings):
    smallest = len(strings[0])
    for string in strings:
        if len(string) < smallest:
            smallest = len(string)

    for i in range(smallest, 0, -1):
        all_hashes = []
        for string in strings:
            hashes = new_hashing(string, i)
            all_hashes.append(hashes)
        if len_intersection(all_hashes) != 0:
            print(i)
            exit()

    print(0)


how_many = int(input())
inputs = []
for k in range(how_many):
    inputs.append(input())

find_longest_sub_str(inputs)
