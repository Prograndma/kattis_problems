it = ["2",
"* 30 20,25,30-33",
"9,15 30 *"]


def find_num_hours(thing):
    if thing[0] == "*":
        return 24
    amount = 0
    for burp in thing:
        if "-" in burp:
            temp = burp.split("-")
            amount += int(temp[1]) - int(temp[0])
        else:
            amount += 1
    return amount


def find_num_min_or_sec(thing):
    if thing[0] == "*":
        return 60
    amount = 0
    for burp in thing:
        if "-" in burp:
            temp = burp.split("-")
            amount += int(temp[1]) - int(temp[0])
            amount += 1
        else:
            amount += 1

    return amount


def do_stuff(stuff):
    arr = []
    arr = [0 for i in range(86400)]
    total_jobs = 0
    for thing in stuff:
        hour, minute, second = thing.split()
        hour = hour.split(",")
        minute = minute.split(",")
        second = second.split(",")

        num_hours = find_num_hours(hour)
        num_min = find_num_min_or_sec(minute)
        num_sec = find_num_min_or_sec(second)
        # print(num_hours)
        # print(num_min)
        # print(num_sec)
        total_jobs += num_hours * num_min * num_sec
    return total_jobs


num_jobs = int(it[0])
things = []
for i in range(1, num_jobs + 1):
    things.append(it[i])

da = do_stuff(things)
print(da)