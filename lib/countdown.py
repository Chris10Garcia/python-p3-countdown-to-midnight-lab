import time


def countdown(val):
    while val > 0:
        print(f"{val} SECOND(S)!")
        val -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(val):
    while val > 0:
        print(f"{val} SECOND(S)!")
        val -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
    