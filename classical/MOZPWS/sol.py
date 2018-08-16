import re

from collections import deque


def subarr(arr, n, k):
    """
    return the arr A such that

    A[i] = k-min-subarray starting from i
    """
    # basic cases
    if k <= 0 or k > n:
        return []

    if len(arr) <= 1:
        return arr

    # k-window
    window = deque(arr[:1], k)
    last = None

    # fill it up till length k
    # for each element in array, any increase or hump is trimmed
    # down.. which means everytime the number goes down, we remove
    # all elements smaller than the number itself. this is because
    # those elements which are removed have no chance of being the
    # k-min-subarray
    for i in xrange(1, k):
        broken = False
        while window:
            last = window.pop()
            if last <= arr[i]:
                broken = True
                break
        # if window is emptied, only add the new element
        if not broken:
            window.append(arr[i])
        else:
            # o/w add removed element and the new element
            window.append(last)
            window.append(arr[i])

    # now slide the window and fill in the A[i]
    # i goes from 0 to n - k + 1
    A = [] * (n - k + 1)

    for i in xrange(n - k):
        # the leftmost element in window is the k-min-subarray
        left = arr[i]
        right = arr[k + i]
        A.append(window[0])
        broken = False

        # and then slide and evict old and/or insert new
        if left == A[-1]:
            window.popleft()

        while window:
            last = window.pop()
            if last <= right:
                broken = True
                break

        if not broken:
            window.append(right)
        else:
            # finally is not broken, then add the remaining elements
            window.append(last)
            window.append(right)

    # finally feed the last guy
    A.append(window.popleft())

    return A


def main():
    # get the number of cases
    nocases = int(raw_input())

    # loop through all the cases
    for case in xrange(1, nocases + 1):
        print("Case %d:" % case)

        # get size and k
        n, k = map(int, re.split('\s*', raw_input()))
        # get the array
        arr = map(int, re.split('\s*', raw_input()))

        # calculate the k min subarr for all i in 1..n-k+1
        kminarr = subarr(arr, n, k)

        # get the number of queries
        q = int(raw_input())

        # get the individual queries
        for _ in xrange(q):
            l_ind, r_ind = map(int, re.split('\s*', raw_input()))

            # get the right index
            lt = l_ind - 1
            rt = r_ind - k
            # between l and r, compute the max element now
            # TODO .. read segment tree
            try:
                print(max(kminarr[lt:rt + 1]))
            except (IndexError, ValueError):
                print("Impossible")


if __name__ == "__main__":
    main()
