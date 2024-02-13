# This is just stupid code that chat gpt said I should use. It's trash.


def maximum_teams(n, competitors):
    teams = 0
    end = float('-inf')

    for i in range(n):
        if competitors[i][0] > end:
            teams += 1
            end = competitors[i][1]

    return teams

# Input
n = int(input())
competitors = [tuple(map(int, input().split())) for _ in range(n)]
competitors.sort()

# Calculate and output the maximum number of teams
print(maximum_teams(n, competitors))