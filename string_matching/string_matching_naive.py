import sys


def where_hash_present(in_str, search):
    where = []
    search_len = len(search)
    for i in range(0, len(in_str) - search_len + 1):
        if in_str[i:i + search_len] == search:
            where.append(i)
    return where


def main():
    is_pattern = True
    search = ""
    for line in sys.stdin:
        line = line.strip()
        if is_pattern:
            search = line
            is_pattern = False
        else:
            locations = where_hash_present(line, search)

            for location in locations:
                print(location, end=" ")
            print("")
            is_pattern = True


if __name__ == "__main__":
    main()
