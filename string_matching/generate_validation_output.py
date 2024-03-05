from string_matching import chars_to_arbitrary_numbers, hashy, where_hash_present

PRE = "python_output_for_"
END = ".txt"
TEST_FILE = "test_strings.txt"
TEST_SEARCH_FILE = "test_search_strings.txt"


def list_to_space_separated_strings(to_convert):
    return " ".join(list(map(str, to_convert))) + "\n"


def generate_output_for_chars_to_arbitrary_numbers():
    with open(TEST_FILE, "r") as file:
        with open(f"{PRE}chars_to_arbitrary_numbers{END}", "w") as write_file:
            for line in file:
                numbers = chars_to_arbitrary_numbers(line)
                write_file.write(list_to_space_separated_strings(numbers))


def generate_output_for_hashy():
    with open(TEST_FILE) as file:
        with open(f"{PRE}hashy{END}", "w") as write_file:
            for line in file:
                hashed = hashy(line)
                write_file.write(str(hashed) + "\n")


def generate_output_for_where_hash_present():
    with open(TEST_SEARCH_FILE) as file:
        with open(f"{PRE}where_hash_present{END}", "w") as write_file:
            lines = [line for line in file]
            for i in range(0, len(lines), 2):           # every other element.
                search = lines[i].strip()
                line = lines[i + 1].strip()             # assume file has an even number of lines.
                search_hash = hashy(search)
                where = where_hash_present(line, len(search), search_hash)
                # write_file.write(str(search_hash))
                write_file.write(str(search_hash) + "\n" + list_to_space_separated_strings(where))


def main():
    generate_output_for_chars_to_arbitrary_numbers()
    generate_output_for_hashy()
    generate_output_for_where_hash_present()


if __name__ == "__main__":
    main()
