days = [0] * 365
days_held = []
num_companies = int(input())

for company in range(num_companies):
    num_records = int(input())
    days_comp_held = {}
    for record in range(num_records):
        listy = input().split()
        num_shares = int(listy[0])
        which_day = int(listy[1])

        days_held.append(which_day)
        days_comp_held[which_day] = num_shares
    company_days = list(days_comp_held.keys())
    company_days.sort()
    last = 0
    for i, day in enumerate(company_days):
        how_many = days_comp_held[day]
        to = 365
        if i + 1 < len(company_days):
            to = company_days[i + 1]
        for j in range(day, to):
            days[j] += how_many

days_held = list(set(days_held))
days_held.sort()

for day in days_held:
    print(days[day], end=" ")
print("")
