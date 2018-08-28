import re


def comparat(x, y):
    if x[0] == y[0]:
        if x[1] == y[1]:
            if x[2] < y[2]:
                return -1
            elif x[2] > y[2]:
                return 1
            return 0
        elif x[1] > y[1]:
            return 1
        return -1
    elif x[0] < y[0]:
        return -1
    return 1


def inp():
    while True:
        ret = raw_input()
        if ret.strip():
            return ret


def main():
    # numbr of testcases
    nt = int(inp())
    # all lookups
    # lookup = {}
    # all tuples
    # tuples = set()

    # go thru all of `em
    for _ in xrange(nt):
        n = int(inp())

        # base case
        if n < 3:
            print("0")
            continue

        # feed array
        arr = sorted(map(int, re.split('\s+', inp())))
        triples = thrtrips(arr, n)
        print len(triples)
        for i, j, k in triples:
            print i, j, k

        # # clear cache
        # lookup.clear()
        # tuples.clear()

        # # now put in lookup each element
        # for i in arr:
        #     lookup.add(i)

        # # for each element in the list, find if sum is a triplet
        # for j in xrange(n):
        #     # if arr[j + 1] == arr[j]:
        #     #     continue

        #     for k in xrange(j):
        #         if -(arr[j] + arr[k]) in lookup:
        #             tuples.add(
        #                 tuple(sorted((arr[k], arr[j], -(arr[j] + arr[k])))))

        # # print all the tuples
        # print len(tuples)
        # for i, j, k in sorted(tuples, cmp=comparat):
        #     print i, j, k


def thrtrips(arr, n):
    ret = []

    # sort array elements
    arr.sort()

    for i in range(0, n - 1):

        # initialize left and right
        ll = i + 1
        r = n - 1
        x = arr[i]
        while (ll < r):
            if (x + arr[ll] + arr[r] == 0):
                # print elements if it's sum is zero
                ret.append((x, arr[ll], arr[r]))
                ll += 1
                r -= 1

            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[ll] + arr[r] < 0):
                ll += 1

            # if sum is greater than zero than
            # decrement in right side
            else:
                r -= 1

    return ret


if __name__ == "__main__":
    main()
