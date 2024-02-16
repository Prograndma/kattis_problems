### as always, chatgpt is little bit garbage, and so is this solution. Good rubber duck though.

def find_henk_beaten(matrix):
    henk_beaten = set()
    n = len(matrix)
    for i in range(1, n):
        if matrix[i][0] == '1':
            henk_beaten.add(i)
    return henk_beaten


def find_possible_challengers(matrix, results, challenger, beaten_by_henk):
    possible_challengers = []
    for i in range(len(matrix)):
        if matrix[challenger][i] == '1' and results[i] == -1:
            possible_challengers.append(i)
        elif matrix[challenger][i] == '0' and i != beaten_by_henk:
            return []
    return possible_challengers


def choose_challenger(matrix, results, current_king, beaten_by_henk):
    possible_challengers = find_possible_challengers(matrix, results, current_king, beaten_by_henk)
    if not possible_challengers:
        return -1
    min_beat_count = float('inf')
    chosen_challenger = -1
    for challenger in possible_challengers:
        beat_count = 0
        for i in range(len(matrix)):
            if matrix[challenger][i] == '1' and results[i] == -1:
                beat_count += 1
        if beat_count < min_beat_count:
            min_beat_count = beat_count
            chosen_challenger = challenger
    return chosen_challenger


def rig_tournament(matrix):
    n = len(matrix)
    results = [-1] * n
    results[0] = 1  # Henk starts as the king
    for i in range(1, n):
        challenger = choose_challenger(matrix, results, results.index(1), 0)
        if challenger == -1:
            return "impossible"
        results[challenger] = 1

    return results


# Input
n = int(input())
matrix = [input() for _ in range(n)]

# Find the rigging sequence
result = rig_tournament(matrix)

# Output
if result == "impossible":
    print("impossible")
else:
    for i, val in enumerate(result):
        if val == 1:
            print(i)
