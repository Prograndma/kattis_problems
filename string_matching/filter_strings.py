FILE = 'test_strings.txt'
ordered_set = {}
with open(FILE, "r") as file:
    for line in file:
        stripped_line = ""
        for char in line:
            if char.isalpha() or char.isspace():
                stripped_line += char
        ordered_set[stripped_line] = None

with open(FILE, "w") as file:
    for key in ordered_set.keys():
        file.write(key)
