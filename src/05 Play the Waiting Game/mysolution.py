import time
import random


def waitinggame():

    target = random.randint(2, 4)

    print("Press enter after " + str(target) + " seconds!")
    input("Press enter to begin")
    starttime = time.perf_counter()

    input("Press enter again after " + str(target) + " seconds!")
    totaltime = time.perf_counter() - starttime

    return ("Your time was " + str(round(totaltime, 3)) + " seconds")
