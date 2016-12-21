# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:15:45 2016

Find the maximum total from top to bottom of the triangle below:
"""
triangle ='\
75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

triangle = triangle.split()

triangle = [int(i) for i in triangle]

# Let's see how many total paths there are:
            
z = 1
a = 0
while a < 14:
    z = z*2
    print 'a is', a
    print 'z is', z
    a += 1
z

# Turn the triangle into a dictionary, where keys are depth:

tree = {}
x = 0
for i in xrange(15):
    tree[i] = triangle[x: x + i + 1]
    x += i+1


def iterate(n):
    y = 1
    for i in range(n):
        for z in xrange(len(tree[i])):
            print list((tree[i][z], tree[i+1][z]))
            print y
            y += 1
            print list((tree[i][z], tree[i+1][z+1]))
            print y
            y += 1