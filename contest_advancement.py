
def populate_advancement_list(team_list, amount_advance, limit):
    will_advance = []
    how_many_from_school = {}
    will_advance_fast = {}
    for current_rank, current_id, school_id in team_list:
        if school_id not in how_many_from_school:
            how_many_from_school[school_id] = 1
            will_advance.append(current_id)
            will_advance_fast[current_id] = 1
        else:
            if how_many_from_school[school_id] < limit:
                will_advance.append(current_id)
                will_advance_fast[current_id] = 1
                how_many_from_school[school_id] += 1

        if len(will_advance) == amount_advance:
            return will_advance

    for current_rank, current_id, school_id in team_list:
        if len(will_advance) == amount_advance:
            break
        if current_id not in will_advance_fast.keys():
            will_advance.append(current_id)
            will_advance_fast[current_id] = 1

    advance_in_order = []
    for current_rank, current_id, school_id in team_list:
        if len(advance_in_order) == amount_advance:
            return advance_in_order
        if current_id in will_advance_fast.keys():
            advance_in_order.append(current_id)

    return advance_in_order


first_line = input().split()

num_teams = int(first_line[0])
num_advance = int(first_line[1])
school_limit = int(first_line[2])
teams = []
for rank in range(num_teams):
    team = input().split()
    id = int(team[0])
    school = int(team[1])
    teams.append([rank + 1, id, school])

printer = populate_advancement_list(teams, num_advance, school_limit)

for thing in printer:
    print(thing)