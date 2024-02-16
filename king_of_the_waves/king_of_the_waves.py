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
    for test in test_list:
        if loses_to_anyone_in_list(contestants, test, to_lose_to):
            ordered_winners.append(test)
    return ordered_winners


def order_people_who_beat_henk(contestants, henk_wins, henk_loses, limit=1000):
    ordered_winners = []
    start_of_list = []
    for person_who_beats_henk in henk_loses:
        if loses_to_anyone_in_list(contestants, person_who_beats_henk, henk_wins):
            ordered_winners.append(person_who_beats_henk)
        else:
            start_of_list.append(person_who_beats_henk)
    if len(start_of_list) != 0 and limit > 0:
        # limit -= 1
        to_append = get_ones_that_lose(contestants, ordered_winners + henk_wins, start_of_list)
        if len(to_append) == 0:
            limit -= limit
        for thing in to_append:
            ordered_winners.append(thing)
            start_of_list.remove(thing)
    ordered_winners.extend(start_of_list)
    ordered_winners.reverse()
    return ordered_winners


def do_stuff(win_losses):
    henk_loses, henk_wins = indexes_henk_wins_and_loses_to(win_losses)
    answer = []
    henk_loses = order_people_who_beat_henk(win_losses, henk_wins, henk_loses)
    for index in henk_loses:
        answer.append(index)
    for index in henk_wins:
        answer.append(index)
    answer.append(0)
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
