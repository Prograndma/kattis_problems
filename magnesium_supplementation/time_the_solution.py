from magnesium_supplementation import do_the_work, do_the_other_work
from time import time


one = 16002131
two = 36010079
three = 84017

print("Starting")

start = time()

for i in range(25):
    do_the_other_work(one, two, three)

print(f"It took {(time() - start) / 25} on average.")







