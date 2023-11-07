from random import randint
from time import sleep

MOVEMENT_STEPS = 5

down = True
right = False
left = False

current_steps = 0

def print_blank_gap(length = 0):
    for x in range(length):
        print(' ', end="")

initial_gap = 1

for x in range(10_000):
    while current_steps < MOVEMENT_STEPS:
        sleep(1)
        if down:
            print()
            print('.', end="")
            print_blank_gap(initial_gap)
        elif right:
            print('.', end="")
            initial_gap += 1
        # elif left:
        #     print('.')
        current_steps += 1
    
    if down:
        down = False
        right = True
        print_blank_gap(initial_gap)
    elif right:
        down = True
        right = False
    current_steps = 0