import math


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


def get_divisor(n, up_to):
    up_to += 1
    go_to = min(int(math.sqrt(n) + 1), up_to)
    divisors = []
    large = []
    for i in range(1, go_to):
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


def get_divisor_slower(n, up_to):
    divisors = []
    large = []
    up_to += 1
    for i in range(1, math.sqrt(n) + 1):
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


def find_prescriptions(total_needed, max_dosage, max_pills):
    valid_pills = []
    divisors = get_divisor_slower(total_needed, max_dosage)
    for divisor in divisors:
        if total_needed / divisor <= max_pills and divisor <= max_dosage:
            valid_pills.append(int(divisor))
    return valid_pills


# Input
total_needed, max_dosage, max_pills = map(int, input().split())

# Find prescriptions
prescriptions = find_prescriptions(total_needed, max_dosage, max_pills)

# Output
print(len(prescriptions))
for dosage in prescriptions:
    print(dosage)
