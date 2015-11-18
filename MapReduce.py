#!/usr/local/bin/python3

"""
Author: 	Clint Cooper, Hunter Oehrtman
Date:   	11/13/15 (3 hours)
CSCI 460:	Final Project

MapReduce for finding triangles in an undirected graph.

Naive Time Complexity:    (n^4)
Threaded Time Complexity: ((n^4)/(w^4)) + (w^3)
Current Time Complexity:  ((n^4)/(w^3)) + (w^3)
"""

import sys
from threading import Thread

Triangles = []
PotentialTriangles = []

def FindTriangles(data, start, end, result):

    TriPoints = []
    PotentialTriPoints = []
    P1 = start
    while P1 <= end:
        for P2 in range(len(data[P1])):
            if data[P1][P2] == 1:
                if P2 > end or P2 < start:
                    PotentialTriPoints.append([P1, P2])
                else:
                    for P3 in range(len(data[P2])):
                        if data[P2][P3] == 1 and P3 != P1:
                            if P3 > end or P3 < start:
                                if data[P1][P3] == 1:
                                    TriPoints.append([P1, P2, P3])
                            else:
                                for P4 in range(len(data)):
                                    if data[P3][P4] == 1 and P4 == P1:
                                        TriPoints.append([P1, P2, P3])
        P1 += 1

    TriPoints = [list(x) for x in set(tuple(sorted(x)) for x in TriPoints)]
    PotentialTriPoints = [list(x) for x in set(
        tuple(sorted(x)) for x in PotentialTriPoints)]

    result.append(TriPoints)
    result.append(PotentialTriPoints)


def ResolvePotentials(data):
    TriPoints = []
    for x in data:
        for y in data:
            if x[0] == y[0]:
                for z in data:
                    if (x[1] == z[0] and y[1] == z[1]) or \
                       (x[1] == z[1] and y[1] == z[0]):
                        TriPoints.append([x[0], x[1], y[1]])
            elif x[1] == y[0]:
                for z in data:
                    if (x[0] == z[0] and y[1] == z[1]) or \
                       (x[0] == z[1] and y[1] == z[0]):
                        TriPoints.append([x[0], x[1], y[1]])
            elif x[0] == y[1]:
                for z in data:
                    if (x[1] == z[0] and y[0] == z[1]) or \
                       (x[1] == z[1] and y[0] == z[0]):
                        TriPoints.append([x[0], x[1], y[0]])
            elif x[1] == y[1]:
                for z in data:
                    if (x[0] == z[0] and y[0] == z[1]) or \
                       (x[0] == z[1] and y[0] == z[0]):
                        TriPoints.append([x[0], x[1], y[0]])

    TriPoints = [list(x) for x in set(tuple(sorted(x)) for x in TriPoints)]

    return TriPoints


def Worker(data, start, end):
    result = []
    thread = Thread(target=FindTriangles, args=(data, start, end, result))
    return (thread, result)


def main(numWorkers):
    global Triangles
    global PotentialTriangles
    # Save this even if we read in file
    data = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
[0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
[0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
[0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
[0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
[0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0]]

    while len(data) % numWorkers != 0 or numWorkers > len(data):
        numWorkers -= 1

    stepSize = len(data) // numWorkers
    threads = [Worker(data, step, step + stepSize - 1) for step in range(0, len(data), stepSize)]
    for t in threads:
        t[0].start()
    for t in threads:
        t[0].join()
        Triangles.append(t[1][0])
        PotentialTriangles.append(t[1][1])

    print('Data:')
    for x in data:
        print(x)

    print('\nTriangles:')
    for i in range(len(Triangles)):
        print('Worker %d:' % i, Triangles[i])

    print('\nPotentials:')
    for i in range(len(PotentialTriangles)):
        print('Worker %d:' % i, PotentialTriangles[i])

    print('\nFlattened Potentials:')
    PotentialTriangles = sorted([list(x) for x in set(tuple(sorted(x)) for x in [
                                item for sublist in PotentialTriangles for item in sublist])])
    print(PotentialTriangles)

    NewTriangles = ResolvePotentials(PotentialTriangles)

    print('\nNew Triangles:')
    for x in NewTriangles:
        print(x)

    print('\nAll Triangles:')
    Triangles = [item for sublist in Triangles for item in sublist]
    Triangles += NewTriangles
    for x in sorted(Triangles):
        print(x)

    return Triangles

if __name__ == '__main__':
    main(6)
    # Make this read in file and worker number from command line
    # Also add comments
