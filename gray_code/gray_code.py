def get_unused_numbers():
    numbers = []
    for i in range(1024):
        numbers.append(get_binary_representation(i))
    return numbers


def get_binary_representation(number):
    return '{0:010b}'.format(number)


def find_two_step_difference(current, unused_numbers):
    for number in unused_numbers:
        num_diffs = 0
        for char1, char2 in zip(current, number):
            if char1 != char2:
                num_diffs += 1

        if num_diffs % 2 == 0:
            return number


def get_even_gray_code(index):
    unused = get_unused_numbers()
    gray = "00000000--"
    for i in range(index + 1):
        gray = find_two_step_difference(gray, unused)
        unused.remove(gray)
        # print(f"{i}: {gray}")
        # if i == 3:
        #     gray = find_two_step_difference(gray, unused)
        #     unused.remove(gray)
    return gray


# for i in range(501):
#     print(f"{i}: {get_even_gray_code(i)}")

print(get_even_gray_code(500))