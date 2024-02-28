import sys

MOD = 1_000_000_007
BASE = 29


def chars_to_arbitrary_numbers(in_str):
    return_array = []
    for char in in_str:
        if char.isalpha():
            if char.isupper():
                return_array.append(ord(char) - 66 + 28)
            else:
                return_array.append(ord(char) - 96)
        else:
            return_array.append(53)

    return return_array


def hashy(in_str):
    # s = list(map(lambda x: ord(x) - 96 if x.islower() else ord(x) - 66 + 26, in_str))
    # s = [ord(x) - 96 if x.islower() else ord(x) - 66 + 28 for x in in_str]
    s = chars_to_arbitrary_numbers(in_str)

    cur_hash = 0
    for i in range(len(in_str)):
        cur_hash = (cur_hash * BASE + s[i]) % MOD
    return cur_hash


def where_hash_present(in_str, hash_len, search_hash):
    max_pow = pow(BASE, hash_len - 1)
    max_pow = max_pow % MOD
    # print(max_pow)
    # s = [int(ord(c) - 96) for c in in_str]
    # s = list(lambda x: ord(x) - 96 if x.islower() else ord(x) - 66 + 26, in_str)
    # s = [ord(x) - 96 if x.islower() else ord(x) - 66 + 28 for x in in_str]
    s = chars_to_arbitrary_numbers(in_str)
    # Compute the initial hash value for the first substring of length length_of_hash
    where = []
    cur_hash = 0
    for i in range(hash_len):
        cur_hash = (cur_hash * BASE + s[i]) % MOD
    if cur_hash == search_hash:
        where.append(0)

    # Update hash values for subsequent substrings
    for i in range(hash_len, len(s)):
        cur_hash = ((cur_hash - s[i - hash_len] * max_pow) * BASE + s[i]) % MOD
        if cur_hash == search_hash:
            where.append(i - hash_len + 1)
    return where


def main():
    is_pattern = True
    line_len = 0
    line_hash = 0
    for line in sys.stdin:
        line = line.strip()
        if is_pattern:
            line_hash = hashy(line)
            line_len = len(line)
            is_pattern = False
        else:
            locations = where_hash_present(line, line_len, line_hash)

            for location in locations:
                print(location, end=" ")
            print("")
            is_pattern = True


if __name__ == "__main__":
    main()
