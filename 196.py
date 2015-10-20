#!/usr/bin/python

# [2015-01-05] Challenge #196 [Practical Exercise] Ready... set... set!

import random


class IntegerSet(object):
    def __init__(self, values):
        self.values = values

    def Contains(self,  value):
        return value in self.values

    def Equals(self, setb):
        if len(self.values) is not len(setb.values):
            return False

        if sorted(self.values) == sorted(setb.values):
            return True
        else:
            return False

    @staticmethod
    def Union(seta, setb):
        setc = seta.values + setb.values
        setd = []
        for n in setc:
            if n not in setd:
                setd.append(n)
        return setd

    @staticmethod
    def Intersection(seta, setb):
        setc = []
        for i in seta.values:
            for j in setb.values:
                if i == j:
                    setc.append(i)
        return setc

    def __repr__(self):
        return str(self.values)


def main():
    a = IntegerSet(random.sample(range(10), 4))
    b = IntegerSet(random.sample(range(10), 4))

    print("A = {}".format(a.values))
    print("B = {}".format(b.values))

    print("Does {} contain '3'? {}".format(a, a.Contains(3)))
    print("Does {} contain '5'? {}".format(b, b.Contains(5)))

    print("{} union {} = {}".format(a, b, IntegerSet.Union(a, b)))
    print("{} intersect {} = {}".format(a, b, IntegerSet.Intersection(a, b)))

if __name__ == '__main__':
    main()
