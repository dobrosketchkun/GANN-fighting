#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import generators
import random
import numpy

def median(lst):
    return numpy.median(numpy.array(lst))


def xselections(items, n):
    """
    Генерирует комбинации с повторениями размера n из
    листа объектов [a, b, ...].
    Чтобы получить лист из текстовых комбинаций:
    ["".join(t) for t in xselections(items, n)]

    """
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss



def all_xselections(items, n2, n1 = 1):
    """
    Генерирует комбинации с повторениями размера
    от n1 (по-умолчанию 1) до n из листа объектов
    [a, b, ...].
    """
    selections = []
    for num in range(n1, n2):
       selections += ["".join(t) for t in xselections(items,num)]
    return selections


#divider = all_xselections(['0','1'], 8, 7)
divider = ["".join(t) for t in xselections(['0','1'], 9)]



def split_length(divider, times = 100000):

    rez = []
    n = []
    tlens = []

    for item in divider:

        #times = 10000
        test = ''
        #item = '0'
        for i in range(times):
            #gene += random.choice("10")
            test += str(random.randint(0, 1))

        t = test.split(item)
        tlens.append(len(t))
        sum = 0
        for num in t:
           sum += len(num)
        sred = sum/float(len(t))

        #print item,   ':', sred
        rez.append(str(sred))
        n.append(str(int(item,2)))

    #print rez
    #print n
    print tlens


    from matplotlib import pyplot as plt
    import numpy as np
    x = range(len(divider))
    y =  [median(tlens) for i in range(len(divider))]

    #plt.plot(n,rez, 'ro')
    plt.plot(range(len(divider)), tlens, 'bo')
    plt.plot(x, y,'r--', markersize=100)


    plt.show()


split_length(divider, times = int(5*10E3))

