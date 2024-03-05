TEST_FILE = "test_strings.txt"
TEST_SEARCH_FILE = "test_search_strings.txt"


def test_chars_to_arbitrary_numbers():
    print("Testing chars_to_arbitrary_numbers")
    with open(TEST_FILE) as file:
        inputs = [line for line in file]

    with open("python_output_for_chars_to_arbitrary_numbers.txt") as file:
        python_outputs = [line for line in file]

    with open("goOutputForcharsToArbitraryNumbers.txt") as file:
        go_outputs = [line for line in file]
    mis_matches = 0
    for in_val, py_out, go_out in zip(inputs, python_outputs, go_outputs):
        if py_out != go_out:
            print(f"An error for input (len={len(in_val)}): {in_val}")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}\n")
            mis_matches += 1
    print(f"{mis_matches}/{len(inputs)} tests failed\n")


def test_hashy():
    print("Testing hashy")
    with open(TEST_FILE) as file:
        inputs = [line for line in file]

    with open("python_output_for_hashy.txt") as file:
        python_outputs = [line for line in file]

    with open("goOutputForHashy.txt") as file:
        go_outputs = [line for line in file]
    mis_matches = 0
    for in_val, py_out, go_out in zip(inputs, python_outputs, go_outputs):
        if py_out != go_out:
            print(f"An error for input (len={len(in_val)}): {in_val}")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}\n")
            mis_matches += 1
    print(f"{mis_matches}/{len(inputs)} tests failed\n")


def test_where_hash_present():
    print("Testing where_hash_present")
    with open(TEST_SEARCH_FILE) as file:
        i = 0
        inputs = []
        to_append = []
        for line in file:
            if i % 2 == 0:
                to_append = [line]
            else:
                to_append.append(line)
                inputs.append(to_append)
            i += 1

    with open("python_output_for_where_hash_present.txt") as file:
        python_outputs = [line for line in file]

    with open("goOutputForWhereHashPresent.txt") as file:
        go_outputs = [line for line in file]
    mis_matches = 0
    for i, (in_val, py_out, go_out) in enumerate(zip(inputs, python_outputs, go_outputs)):
        if py_out != go_out:
            print(f"An error for {i*2 + 1} and {i*2 + 2}th input (len={len(in_val[1])}): {in_val}")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}\n")
            mis_matches += 1
    print(f"{mis_matches}/{len(inputs)} tests failed\n")


def main():
    test_chars_to_arbitrary_numbers()
    test_hashy()
    test_where_hash_present()
    print("ALL DONE")


if __name__ == "__main__":
    main()
