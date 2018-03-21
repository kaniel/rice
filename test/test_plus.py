# -*- coding:utf-8 -*-
import os


def getPlus(a, b):

    k1 = len(str(a))
    s1= str(a)
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
        if p[x] / 10 == 0:
            p[x] = str(p[x])
            print x, type(p[x]), p[x]
            continue
        elif p[x] / 10 != 0:
            m = p[x] / 10
            p[x + 1] += m
            p[x] = str(p[x] % 10)
    end = "".join(p[::-1])
    print len(end), end


if __name__=="__main__":
    t = list([1, 2, 3])
    # print t.ma
    print t
    # print t[3]
    print type(str(type(20 % 10))), 20 % 10
    getPlus(str(180890890909089090890890890678723451231231231231239879780789789789808704234234234223423432432423423423423423423423545463423123)*1000, str(123451231234234234234234231231231230808908790879079089079089078907890789087907890789012322342342342342352343243242342342342342342342342342342343241))
