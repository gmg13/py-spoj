# result map
CACHE = {1: False, 2: False}


def foo(n):
    return (n + 1) / 2


def solve3(n):
    if n not in CACHE:
        # if not deep, then we are good
        if solve3(foo(n)):
            CACHE[n] = False
        else:
            CACHE[n] = not solve3(n - 1)

    return CACHE[n]


def main():
    nt = int(raw_input())

    for i in xrange(nt):
        n = int(raw_input())
        if solve3(n):
            print "ZiYES"
        else:
            print "HuseyNO"


if __name__ == "__main__":
    main()
