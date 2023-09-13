import sys
import time


def loading_icon():
    icons = ['/', '-', '\\', '|']
    index = 0
    while True:
        sys.stdout.write("\r" + icons[index])
        sys.stdout.flush()
        time.sleep(0.1)
        index = (index + 1) % len(icons)
        sys.stdout.flush()


loading_icon()
