from datetime import datetime
from time import sleep

queue = []


def tim():
    count = 1
    while True:
        print(count, datetime.now())
        count += 1
        yield


def banger():
    count = 1
    while True:
        s = str(datetime.now())
        if count % 4 == 0:
            s += ' - quadreven'
        print(s)
        count += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(1)


if __name__ == '__main__':
    queue.append(tim())
    queue.append(banger())
    main()
