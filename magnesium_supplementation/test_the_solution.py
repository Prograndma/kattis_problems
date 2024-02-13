from magnesium_supplementation import do_the_work, do_the_other_work, niave, chat_gpt_solution
import random
from time import time

inputs = [[6, 6, 4],
          [6, 2, 3],
          [1, 1, 10],
          [10000, 10000, 1],
          ]

answers = [[3, 2, 3, 6],
           [1, 2],
           [1, 1],
           [1, 1]]


def check_answer(answer, result):
    for i in range(len(answer)):
        if result[i] != answer[i]:
            return False
    return True


def get_random_input():
    return random.randint(1, 1e11), random.randint(1, 1e11), random.randint(1, 1e11)


def test_random():
    i = 0
    time_accurate = 0
    time_perhaps_false = 0
    while(True):
        one, two, three = get_random_input()
        start = time()
        answer = chat_gpt_solution(one, two, three)
        time_accurate += time() - start
        start = time()
        suspect = do_the_other_work(one, two, three)
        time_perhaps_false += time() - start
        if len(answer) != len(suspect):
            print("ERROR")
            print(one, two, three)
            print(answer)
            print(suspect)
            return
        for a, b in zip(answer, suspect):
            if a != b:
                print("ERROR")
                print(one, two, three)
                print(answer)
                print(suspect)
                return
        i += 1
        if i % 100 == 0:
            print(f"Have tested {i} inputs and gotten identical answers!")
            print(f"Accurate average time: {time_accurate / i}")
            print(f"Fast     average time: {time_perhaps_false / i}")


def main():
    for [one, two, three] in inputs:
        print(f"for {one}, {two}, {three}:")
        result = chat_gpt_solution(one, two, three)
        other_result = do_the_other_work(one, two, three)
        # other_result.insert(0, len(other_result))
        b_other_result = check_answer(result, other_result)

        if not b_other_result:
            print(other_result, end=" <---")
            print(f"{b_other_result} ---> {result}")
        else:
            print(b_other_result)
    test_random()


if __name__ == "__main__":
    main()
