from ball_clock import BallClock
from time import time


def print_state_naive(num_balls: int, num_ticks: int):
    ball_clock = BallClock(num_balls)
    for i in range(num_ticks):
        ball_clock.tick()
    print(ball_clock.state())


def get_state_naive(num_balls: int, num_ticks: int):
    ball_clock = BallClock(num_balls)
    for i in range(num_ticks):
        ball_clock.tick()
    return ball_clock.state()


def print_state_broken(num_balls, num_ticks):
    balls = []
    fives = []
    hours = []
    ones = []
    for i in range(num_balls):
        balls.append(i + 1)

    for i in range(1, 1 + num_ticks):
        ones.append(balls[0])
        balls = balls[1:]
        if i % 4 == 0:
            fives.append(balls[0])
            balls = balls[1:] + ones
            ones = []
        if i % 44 == 0:
            hours.append(balls[0])
            balls = balls[1:] + fives
            fives = []
        if i % 484 == 0:
            balls = balls[1:] + hours + [balls[0]]
            hours = []

    state = {"Min": ones,
             "FiveMin": fives,
             "Hour": hours, "Main": balls}
    print(state)


def get_state_broken(num_balls: int, num_ticks: int):
    balls = []
    fives = []
    hours = []
    ones = []
    for i in range(num_balls):
        balls.append(i + 1)

    num_actual_ticks = 0
    for i in range(1, 1 + num_ticks):
        if i % 4 == 0:
            fives.append(balls[0])
            balls = balls[1:] + ones
            ones = []
            i += 1
        if i % 44 == 0:
            hours.append(balls[0])
            balls = balls[1:] + fives
            fives = []
        if i % 484 == 0:
            balls = balls[1:] + hours + [balls[0]]
            hours = []
        ones.append(balls[0])
        balls = balls[1:]

        num_actual_ticks += 1

    return {"Min": ones,
            "FiveMin": fives,
            "Hour": hours, "Main": balls}


def get_time_until_refresh_naive(num_balls: int):
    ball_clock = BallClock(num_balls)
    amount_times = 0
    done = False
    reset = []
    for i in range(num_balls):
        reset.append(i + 1)
    while not done:
        ball_clock.tick()
        amount_times += 1
        if amount_times % 1440 == 0:
            if ball_clock.state()['Main'] == reset:
                return int(amount_times / 60 / 24)


def print_time_to_refresh_naive(num_balls: int):
    ball_clock = BallClock(num_balls)
    amount_times = 0
    done = False
    reset = []
    for i in range(num_balls):
        reset.append(i + 1)
    while not done:
        ball_clock.tick()
        amount_times += 1
        if amount_times % 1440 == 0:
            if ball_clock.state()['Main'] == reset:
                print(f"{num_balls} cycle after {int(amount_times / 60 / 24)} days.")
                return


def record_time_to_refresh_naive():
    days_taken = []
    start = time()
    for num_balls in range(27, 128):
        ball_clock = BallClock(num_balls)
        amount_times = 0
        done = False
        reset = []
        for i in range(num_balls):
            reset.append(i + 1)
        while not done:
            ball_clock.tick()
            amount_times += 1
            if amount_times % 1440 == 0:
                if ball_clock.state()['Main'] == reset:
                    days_taken.append(int(amount_times / 60 / 24))
                    print(f"{num_balls} cycle after {int(amount_times / 60 / 24)} days.")
                    done = True
    time_elapsed = time() - start

    with open("naive_days_taken.txt", 'w') as f:
        for i, amount_days in enumerate(days_taken):
            f.write(f"{i + 27}: {amount_days}\n")
        f.write(f"TIME: {time_elapsed}")


def compare_refresh_days(num_balls, days_taken):
    with open("naive_days_taken.txt", "r") as f:
        lines = f.readline()
    line = lines[num_balls - 26]
    data = line.split(": ")
    if num_balls != int(data[0]):
        raise Exception("compare_answer function in main not working!")

    return days_taken == int(data[1])


def compare_state(num_balls, num_ticks, state):
    return state == get_state_naive(num_balls, num_ticks)


def main():
    while True:
        numbers = input().split(' ')
        if len(numbers) == 2:
            num_balls = int(numbers[0])
            num_ticks = int(numbers[1])
            print_state_naive(num_balls, num_ticks)
        if len(numbers) == 1:
            num_balls = int(numbers[0])
            print_time_to_refresh_naive(num_balls)


if __name__ == "__main__":
    main()
