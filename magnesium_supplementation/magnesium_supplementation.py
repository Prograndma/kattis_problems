import math


def get_divisor(n, up_to):
    go_to = min(int(math.sqrt(n) + 1), up_to + 1)
    divisors = [1]
    large = []
    for i in range(2, go_to):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                if n / i <= up_to:
                    large.append(n / i)
    for divisor in reversed(large):
        divisors.append(divisor)
    if n <= up_to:
        divisors.append(n)
    return divisors


def do_the_other_work(how_much, biggest_pill, amount_willing_to_take):
    valid_pills = []
    divisors = find_divisors_chat_gpt(how_much)
    for divisor in divisors:
        if how_much / divisor <= amount_willing_to_take and divisor <= biggest_pill:
            valid_pills.append(int(divisor))
    return sorted(valid_pills)


def do_the_work(how_much, biggest_pill, amount_willing_to_take):
    valid_pills = []
    smallest = min(biggest_pill + 1, (how_much + 1))
    for i in range(1, smallest):
        # if len(valid_pills) == amount_willing_to_take:
        #     break
        if i == how_much:
            valid_pills.append(i)
            break
        if how_much % i == 0:
            if how_much / i <= amount_willing_to_take:
                valid_pills.append(i)
    return valid_pills


def niave(how_much, biggest_pill, amount_willing_to_take):
    valid_pills = []
    go_to = min(biggest_pill + 1, how_much + 1)
    for i in range(1, go_to):
        if how_much % i == 0:
            if how_much / i <= amount_willing_to_take:
                valid_pills.append(i)
    return valid_pills


def find_divisors_chat_gpt(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
        i += 1
    return divisors


def chat_gpt_solution(total_needed, max_dosage, max_pills):
    valid_pills = []
    divisors = find_divisors_chat_gpt(total_needed)
    for dosage in divisors:
        if dosage <= max_dosage and total_needed // dosage <= max_pills:
            valid_pills.append(dosage)
    return sorted(valid_pills)


def main():
    how_much_magnesium_needed, biggest_pill_size, amount_pills_willing_to_take = input().split()
    how_much_magnesium_needed = int(how_much_magnesium_needed)
    biggest_pill_size = int(biggest_pill_size)
    amount_pills_willing_to_take = int(amount_pills_willing_to_take)

    result = do_the_other_work(how_much_magnesium_needed, biggest_pill_size, amount_pills_willing_to_take)
    print(len(result))
    for i, pill in enumerate(result):
        if i == amount_pills_willing_to_take:
            break
        print(pill)


if __name__ == "__main__":
    main()
