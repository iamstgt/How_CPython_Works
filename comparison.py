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


#  Local names are faster thn global ones.
def yearByLocalName():
    seconds_per_day = 86400
    return seconds_per_day * 365


def yearByGlobalName():
    return 86400 * 365


def main():
    dis.dis(yearByLocalName)
    tic()
    yearByLocalName()
    print()
    toc()
    dis.dis(yearByGlobalName)
    tic()
    yearByGlobalName()
    print()
    toc()


if __name__ == "__main__":
    main()
    