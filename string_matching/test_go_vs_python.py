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

    with open("goOutputForcharsToArbitraryNumbers64.txt") as file:
        go64_outputs = [line for line in file]
    mis_matches = 0
    for in_val, py_out, go_out, go64_out in zip(inputs, python_outputs, go_outputs, go64_outputs):
        if py_out != go_out or go_out != go64_out:
            print(f"An error for input (len={len(in_val)}): {in_val}")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}")
            print(f"go64_t (len={len(go64_out.split())}): {go64_out}\n")
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

    with open("goOutputForHashy64.txt") as file:
        go64_outputs = [line for line in file]
    mis_matches = 0
    for in_val, py_out, go_out, go64_out in zip(inputs, python_outputs, go_outputs, go64_outputs):
        if py_out != go_out or go_out != go64_out:
            print(f"An error for input (len={len(in_val)}): {in_val}")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}")
            print(f"go64_t (len={len(go64_out.split())}): {go64_out}\n")
            mis_matches += 1
    print(f"{mis_matches}/{len(inputs)} tests failed\n")


def test_where_hash_present():
    print("Testing where_hash_present")
    with open(TEST_SEARCH_FILE) as file:
        inputs = [line for line in file]

    with open("python_output_for_where_hash_present.txt") as file:
        python_outputs = [line for line in file]

    with open("goOutputForWhereHashPresent.txt") as file:
        go_outputs = [line for line in file]

    with open("goOutputForWhereHashPresent64.txt") as file:
        go64_outputs = [line for line in file]
    mis_matches = 0
    for i, (in_val, py_out, go_out, go64_out) in enumerate(zip(inputs, python_outputs, go_outputs, go64_outputs)):
        if i % 2 == 0:
            py_prev = py_out
            go_prev = go_out
            in_prev = in_val
            go64_prev = go64_out
        if py_out != go_out or go_out != go64_out:
            print(f"An error for {i}th input (len={len(in_val[1])}): {in_val}")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}")
            print(f"go64_t (len={len(go64_out.split())}): {go64_out}")

            print(f"Previous input : {in_prev}")
            print(f"Previous python: {py_prev}")
            print(f"Previous golang: {go_prev}")
            print(f"Previous gola64: {go64_prev}\n")
            mis_matches += 1
    print(f"{mis_matches}/{len(inputs)} tests failed\n")


def test_rolling_hash():
    print("Testing rolling_hash")

    with open("python_output_for_rolling_hash.txt") as file:
        python_outputs = [line for line in file]

    with open("goOutputForRollingHash.txt") as file:
        go_outputs = [line for line in file]

    with open("goOutputForRollingHash64.txt") as file:
        go64_outputs = [line for line in file]
    mis_matches = 0
    for i, (py_out, go_out, go64_out) in enumerate(zip(python_outputs, go_outputs, go64_outputs)):
        if py_out != go_out or go_out != go64_out:
            print(f"An error for {i}th input")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}")
            print(f"go64_t (len={len(go64_out.split())}): {go64_out}")
            mis_matches += 1
    print(f"{mis_matches}/{len(python_outputs)} tests failed\n")


def test_compare():
    print("Testing compare")

    with open("python_output_for_compare.txt") as file:
        python_outputs = [line.lower() for line in file]

    with open("goOutputForCompare.txt") as file:
        go_outputs = [line for line in file]

    with open("goOutputForCompare64.txt") as file:
        go64_outputs = [line for line in file]
    mis_matches = 0
    for i, (py_out, go_out, go64_out) in enumerate(zip(python_outputs, go_outputs, go64_outputs)):
        if py_out != go_out or go_out != go64_out:
            print(f"An error for {i}th input")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}")
            print(f"go64_t (len={len(go64_out.split())}): {go64_out}")
            mis_matches += 1
    print(f"{mis_matches}/{len(python_outputs)} tests failed\n")


def main():
    test_chars_to_arbitrary_numbers()
    test_hashy()
    test_where_hash_present()
    # test_rolling_hash()
    # test_compare()
    print("ALL DONE")


if __name__ == "__main__":
    main()
