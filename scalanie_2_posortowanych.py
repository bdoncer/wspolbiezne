from bisect import bisect_left
from math import inf
from multiprocessing import Process, Array


def merge(A, B, i, j, k, l, p, q, C):

    m = j - i
    n = l - k

    #swap A and B
    #swap m and m
    if m < n:
        tmp = A[:]
        A = B[:]
        B = tmp[:]
        
        m = n
        i_tmp = i
        j_tmp = j
        i = k
        j = l
        k = i_tmp
        l = j_tmp

    if m == 0:
        return

    r = (i + j) // 2
    s = bisect_left(B, A[r])
    t = p + r - i + s - k
    C[t] = A[r]


    p1 = Process(target=merge, args=(A, B, i, r, k, s, p, t, C))
    p2 = Process(target=merge, args=(A, B, r + 1, j, s, l, t + 1, q, C))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    left = [1, 3, 5, 7, 9,123,234324, inf]
    right = [2, 4, 6, 8, 10,123123,1231231232,inf]
    result = Array('i', [0] * (len(left)+len(right)-2))
    merge(left, right, 0, len(left)-1, 0, len(right)-1, 0, len(left)+len(right), result)
    print(result[:])