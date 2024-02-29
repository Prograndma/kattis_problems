FILE = 'test_search_strings.txt'
READ_FILE = 'test_strings.txt'


def create_substring(line, i):
    line = line.strip()
    line_len = len(line)
    if i % 10 == 9 and len(line) > 3:
        return "zZ\n"                 ## intended to not exist. At least not often.

    if line_len < 8:
        return line + "\n"

    len_search = line_len // 7

    sub_string_start = i % 5
    return line[sub_string_start:sub_string_start + len_search] + "\n"


def create_file():

    with open(READ_FILE, "r") as file:
        lines = [line for line in file]

    with open(FILE, "w") as file:
        for i, line in enumerate(lines):
            file.write(create_substring(line, i))
            file.write(line)


if __name__ == "__main__":
    create_file()