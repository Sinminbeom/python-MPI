import time


def main():
    start = time.time()

    x = []
    for i in range(1000000):
        x.append(i)

    time_end = time.time()
    print("Total time taken = ", (time_end - start))

if __name__ == '__main__':
    main()
