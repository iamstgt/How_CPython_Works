import time
import dis


def tic():
    global start_time_tictoc
    start_time_tictoc = time.time()


def toc(tag="elapsed time"):
    if "start_time_tictoc" in globals():
        print("{}: {:.9f} [sec]".format(tag, time.time() - start_time_tictoc))
    else:
        print("tic has not been called")


# List comprehension is faster than using append method.
def multiplier():
    L = []
    for i in range (1, 1000):
        if i%3 == 0:
            L.append (i)

def multiplierByListComprehension():
    L = [i for i in range (1, 1000) if i%3 == 0]


def main():
    dis.dis(multiplier)
    tic()
    multiplier()
    print()
    toc()
    dis.dis(multiplierByListComprehension)
    tic()
    multiplierByListComprehension()
    print()
    toc()


if __name__ == "__main__":
    main()
    