import math


def twosortedarrays(N1, N2):
    empty = []
    empty2 = []
    n = []
    l = 0
    median = 0.0
    median_num = 0.0

    n = N1 + N2
    n = sorted(n)
    l = len(n)
    div = math.ceil(l / 2)
    if (l % 2) == 1:
        median = n[div-1]
    else:
        median_num = ((n[div] + n[div - 1]) / 2.0)
        median = median_num
    print(median)


A = [1, 2, 3, 9,11]
B = [4, 5]
twosortedarrays(A, B)
