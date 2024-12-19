from time import sleep


def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        yield


def printer():
    counter = 0
    while True:
        if not counter % 3:
            print('Bang!')
        counter += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)


if __name__ == '__main__':
    g1 = counter()
    g2 = printer()

    queue = [g1, g2]

    try:
        main()
    except KeyboardInterrupt:
        print('Done!')