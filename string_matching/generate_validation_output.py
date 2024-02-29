from string_matching import chars_to_arbitrary_numbers, hashy

PRE = "python_output_for_"
END = ".txt"
TEST_FILE = "test_strings.txt"


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


def main():
    generate_output_for_chars_to_arbitrary_numbers()
    generate_output_for_hashy()


if __name__ == "__main__":
    main()
