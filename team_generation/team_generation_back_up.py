# This is a valid solution to A problem but not THE RIGHT problem. I was returning all possible team combinations that
# could be sent, the desired solution is how many teams you could actually send. So yeah. Stupid.


import timeit
import itertools


def how_many_teams(candidates):
    potential_team_members_for_index = []
    for i in range(len(candidates)):
        _, minimum, maximum = candidates[i]
        potential_team_members_for_index.append(list(range(minimum, maximum + 1)))
    print(potential_team_members_for_index)
    team_set = get_potential_teams(potential_team_members_for_index)
    print(len(team_set.keys()))


def get_potential_teams(potential_team_members_for_index):
    good_team_set = {}
    bad_team_set = {}
    for potential_team_member_list in potential_team_members_for_index:
        potential_teams = list(itertools.combinations(potential_team_member_list, 3))
        if len(potential_teams) > 0:
            for potential_team in potential_teams:
                potential_team = list(potential_team)
                team_key = stringify(potential_team)
                if team_key not in good_team_set and team_key not in bad_team_set:
                    if valid_team(potential_team, potential_team_members_for_index):
                        good_team_set[team_key] = 1
                    else:
                        bad_team_set[team_key] = 1

    return good_team_set


def stringify(a_list):
    returner = ""
    for thing in a_list:
        returner += str(thing)
    return returner


def valid_team(potential_team, potential_team_members_for_index):
    for potential_team_member in potential_team:
        who_they_are_willing_to_work_with = potential_team_members_for_index[potential_team_member - 1]
        # Is this potential team member willing to work with everyone in the potential team?
        if not all(team_member in who_they_are_willing_to_work_with for team_member in potential_team):
            return False
    return True


num_input = int(input())
people = []
for input_rank in range(num_input):
    curr = input().split()

    people.append([input_rank + 1, int(curr[0]), int(curr[1])])

how_many_teams(people)

# print(timeit.timeit(lambda: how_many_teams(people), number=5))
