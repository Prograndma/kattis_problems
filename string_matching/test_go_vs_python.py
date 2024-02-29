def test_chars_to_arbitrary_numbers():
    print("Testing chars_to_arbitrary_numbers\n")
    with open("test_strings.txt") as file:
        inputs = [line for line in file]

    with open("python_output_for_chars_to_arbitrary_numbers.txt") as file:
        python_outputs = []
        for line in file:
            line = line.strip()
            index = line.rfind(" ")
            line_with_last_number_removed = line[:index].strip()
            python_outputs.append(line_with_last_number_removed)
        # python_outputs = [line[:-] for line in file]
    with open("python_output_for_chars_to_arbitrary_numbers.txt") as file:
        python_farts = [line for line in file]

    with open("goOutputForcharsToArbitraryNumbers.txt") as file:
        go_outputs = [line[:-1] for line in file]
    mis_matches = 0
    for in_val, py_out, go_out in zip(inputs, python_outputs, go_outputs):
        if py_out != go_out:
            print(f"An error for input (len={len(in_val)}): {in_val}")
            print(f"py_out (len={len(py_out.split())}): {py_out}")
            print(f"go_out (len={len(go_out.split())}): {go_out}\n")
            mis_matches += 1
    print(f"{mis_matches=}")
    print(f"total_tests={len(inputs)}")


def main():
    test_chars_to_arbitrary_numbers()
    print("ALL DONE")


if __name__ == "__main__":
    main()
