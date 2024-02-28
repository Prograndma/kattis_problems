from string_matching import chars_to_arbitrary_numbers

PRE = "python_output_for_"
END = ".txt"
TEST_FILE = "test_strings.txt"


def generate_ouput_for_chars_to_arbitrary_numbers():
    with open(TEST_FILE, "r") as file:
        with open(f"{PRE}chars_to_arbitrary_numbers{END}", "w") as write_file:
            for line in file:
                write_file.write(chars_to_arbitrary_numbers(line))


def main():
    generate_ouput_for_chars_to_arbitrary_numbers()


if __name__ == "__main__":
    main()
