def parse_raw_inputs(string):
    listy = []
    for char in string:
        listy.append(char)
    return listy


def get_winner(contestants, contestant1, contestant2):
    if contestants[contestant1][contestant2] == "1":
        return contestant1
    return contestant2


def test_answer(contestants, order):
    winner = order[0]
    for i, index in enumerate(order[:-1]):
        winner = get_winner(contestants, winner, order[i + 1])
    if winner != 0:
        return False
    return True


def indexes_henk_wins_and_loses_to(contestants):
    henk_wins = []
    henk_loses = []
    for i, contestant in enumerate(contestants[1:]):
        if contestant[0] == "1":
            henk_loses.append(i + 1)
        else:
            henk_wins.append(i + 1)
    return henk_loses, henk_wins


def loses_to_anyone_in_list(contestants, contestant, test_list):
    for test in test_list:
        if get_winner(contestants, contestant, test) != contestant:
            return True
    return False


def get_ones_that_lose(contestants, to_lose_to, test_list):

    ordered_winners = []
    others = []
    for test in test_list:
        if loses_to_anyone_in_list(contestants, test, to_lose_to):
            ordered_winners.append(test)
        else:
            others.append(test)
    return ordered_winners, others


def do_stuff(win_losses):
    henk_loses, henk_wins = indexes_henk_wins_and_loses_to(win_losses)
    answer = [0]
    answer.extend(henk_wins)
    has_changed = True
    while len(henk_loses) != 0 and has_changed:
        loses_to_people_in_answer, henk_loses = get_ones_that_lose(win_losses, answer, henk_loses)
        if len(loses_to_people_in_answer) == 0:
            has_changed = False
        answer.extend(loses_to_people_in_answer)
    answer.extend(henk_loses)
    answer.reverse()
    if test_answer(win_losses, answer):
        return answer
    return "impossible"


def main():
    num_contestants = int(input())
    inputs = []
    for i in range(num_contestants):
        inputs.append(parse_raw_inputs(input()))

    result = do_stuff(inputs)
    if type(result) == str:
        print(result)
        return

    for thing in result[:-1]:
        print(thing, end=" ")
    print(result[-1])


if __name__ == "__main__":
    main()
