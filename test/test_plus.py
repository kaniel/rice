# -*- coding:utf-8 -*-
import os


def getPlus(a, b):

    k1 = len(str(a))
    s1 = str(a)
    k2 = len(str(b))
    s2 = str(b)
    print k1, type(s1), s1, "  |--|  ",  k2, type(s2), s2
    p = list()
    k = 0
    for item_b in s2[::-1]:
        index = k
        for item_a in s1[::-1]:
            num = int(item_a) * int(item_b)
            if len(p) == index:
                p.append(num)
                index += 1
                continue
            p[index] += num
            index += 1
        k += 1

    print len(p), p
    for x in range(len(p)):
        if x == len(p) - 1:
            p[x] = str(p[x])
            continue
        if p[x] / 10 == 0:
            p[x] = str(p[x])
            print x, type(p[x]), p[x]
            continue
        elif p[x] / 10 != 0:
            m = p[x] / 10
            p[x + 1] += m
            p[x] = str(p[x] % 10)
    res = "".join(p[::-1])
    print len(res), res
    return res


if __name__ == "__main__":
    t = list([1, 2, 3])
    print max(t), min(t)
    print t
    print type(20 % 10), 20 % 10
    res = getPlus(str(999999999999999999999999), str(9996646168496898169999999))
    print "res:", type(res), res
