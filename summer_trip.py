events = input()

itineraries = {}


def recursive_func(event_string, current_events_using):
    if len(event_string) == 0:
        return
    if len(current_events_using) == 0:
        recursive_func(event_string[1:], event_string[0])
        return
    first_char = event_string[0]
    if first_char not in current_events_using:
        itineraries[current_events_using + first_char] = 1

        if 1 != len(event_string):
            recursive_func(event_string[1:], current_events_using + first_char)
        return
    else:
        return
    # for i, char in enumerate(event_string):
    #     if char not in current_events_using:
    #         itineraries[current_events_using + char] = 1
    #         if i != len(event_string) - 1:
    #             recursive_func(event_string[i + 1:], current_events_using + char)
    #             return
    #     else:

        #     return

def remove_consecutive_repeats(string):
    new_str = string[0]
    for char in string:
        if char != new_str[-1]:
            new_str += char
    return new_str


def print_all_permutations(string):
    total = 0
    for i in range(len(string)):
        total += do_stuff(string[i:])
    print(f"TOTAL: {total}")


def do_stuff(string):
    temp_total = 0
    if len(string) == 2:
        temp_total += 1
        print(string)
    if len(string) == 1:
        return temp_total
    for i in range(len(string)):
        if i < 2:
            continue
        if no_repeats_whatsoever(string[:i]):
            temp_total += 1
            print(string[:i])

    return temp_total

def no_repeats_whatsoever(string):
    for char in string:
        if string.count(char) != 1:
            return False
    return True



events = remove_consecutive_repeats(events)
print(events)
print_all_permutations(events)
#
# recursive_func(events, "")
#
# print(len(itineraries.keys()))
# print(itineraries.keys())
# print("*******************")

for i in range(len(events)):
    recursive_func(events[i:], "")
for i in range(len(events), 1, -1):
    recursive_func(events[i:], "")

print(len(itineraries.keys()))
print(itineraries.keys())