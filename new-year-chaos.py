import math
import os
import random
import re
import sys


def minimumBribes(q):
    counter = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):  # 2, 1, 5, 3, 4
            if q[j] > q[i]:
                counter += 1
    print(counter)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
