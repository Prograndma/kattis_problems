from queue import Queue, Empty, Full

MIN_BALLS = 27
MAX_BALLS = 127
FIRST_BALL_HOLDER_SIZE = 4
SECOND_BALL_HOLDER_SIZE = 11
THIRD_BALL_HOLDER_SIZE = 11


class BallClockStack:
    def __init__(self, max_size: int, perma_ball: bool = False):
        self.max_size: int = max_size
        self.perma_ball: bool = perma_ball
        self._stack: [int] = [0] * max_size
        self._ball_location: int = -1

    def get_ball(self) -> int:
        if self._ball_location < 0:
            raise Empty
        self._ball_location -= 1
        return self._stack[self._ball_location + 1]

    def put_ball(self, ball: int):
        if self._ball_location == self.max_size - 1:
            raise Full
        self._ball_location += 1
        self._stack[self._ball_location] = ball

    def num_balls_in_holder(self) -> int:
        return self._ball_location + 1

    def state(self) -> list[int]:
        if self._ball_location == -1:
            # if self.perma_ball:
            #     return [0]
            return []
        # if self.perma_ball:
        #     return [0] + self._stack[:self._ball_location]
        return self._stack[:self._ball_location + 1]


class BallClockQueue:
    def __init__(self, max_size: int):
        self.max_size = max_size
        self._queue = Queue(maxsize=max_size)

    def get_ball(self) -> int:
        try:
            ball = self._queue.get_nowait()
        except Empty:
            raise Exception("Tried to pull from a BallClockHolder  while it was empty. Likely the structure of the "
                            "entire ball clock has been changed and the MIN_BALLS and MAX_BALLS constants need to "
                            "be updated to reflect that.")
        return ball

    def put_ball(self, ball: int):
        """will throw any exception that put_nowait will throw. Is intended."""
        self._queue.put_nowait(ball)

    def num_balls_in_holder(self) -> int:
        return self._queue.qsize()

    def state(self) -> list[int]:
        """comparatively slow, so use sparingly."""
        size = self._queue.qsize()
        temp_ball_holder = [-1] * size
        state = [-1] * size
        for i in range(size):
            ball = self._queue.get_nowait()
            temp_ball_holder[i] = ball
            state[i] = ball

        for ball in temp_ball_holder:
            self._queue.put_nowait(ball)

        return state


class BallClock:
    def __init__(self, num_balls: int):
        if num_balls < MIN_BALLS:
            raise NotEnoughBallClockBalls(f"{num_balls} (< {MIN_BALLS}) is too not enough balls")
        if num_balls > MAX_BALLS:
            raise TooManyBallClockBalls(f"{num_balls} (> {MAX_BALLS} is too many balls")
        self.num_balls = num_balls
        self._time_tracking_ball_stacks = []
        self._time_tracking_ball_stacks.append(BallClockStack(max_size=FIRST_BALL_HOLDER_SIZE))  # minutes
        self._time_tracking_ball_stacks.append(BallClockStack(max_size=SECOND_BALL_HOLDER_SIZE))  # five minutes
        self._time_tracking_ball_stacks.append(
            BallClockStack(max_size=THIRD_BALL_HOLDER_SIZE, perma_ball=True))  # hours
        self._all_ball_holder = BallClockQueue(max_size=num_balls)
        self._fill_all_ball_holder()

    def tick(self):
        ball = self._all_ball_holder.get_ball()
        placed_ball = False
        for i, ball_holder in enumerate(self._time_tracking_ball_stacks):
            try:
                ball_holder.put_ball(ball)
                placed_ball = True
                break
            except Full:
                self._empty_balls(i)
        if not placed_ball:
            self._all_ball_holder.put_ball(ball)

    def state(self) -> dict[str, list[int]]:
        state = {"Min": self._time_tracking_ball_stacks[0].state(),
                 "FiveMin": self._time_tracking_ball_stacks[1].state(),
                 "Hour": self._time_tracking_ball_stacks[2].state(), "Main": self._all_ball_holder.state()}
        return state

    def _fill_all_ball_holder(self):
        for i in range(self.num_balls):
            self._all_ball_holder.put_ball(i + 1)

    def _empty_balls(self, index_of_ball_holder_to_empty):
        for i in range(self._time_tracking_ball_stacks[index_of_ball_holder_to_empty].num_balls_in_holder()):
            self._all_ball_holder.put_ball(self._time_tracking_ball_stacks[index_of_ball_holder_to_empty].get_ball())


class NotEnoughBallClockBalls(Exception):
    """A named exception for the case where there are not enough balls provided for the BallClock class"""


class TooManyBallClockBalls(Exception):
    """A named exception for the case where there are too many balls provided for the BallClock class"""
