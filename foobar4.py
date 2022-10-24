"""
Absorbing Markov Chain
"""

from fractions import Fraction
import math
from typing_extensions import final

def I_matrix(n):
    matrix = [[0]*n for i in range(n)]
    for i in range(n):
        matrix[i][i] += 1
    return matrix

def multiply(A, B):
    C = [[0]*len(A) for i in range(len(B[0]))]
    result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*B)]
                                for A_row in A]
    return result

def sortarray(array,arr2):
    sortedarray = []
    for i in range(len(array)):
        sortedarray.append(array[arr2[i]])
    return sortedarray

def substact(matr_a, matr_b):
    output = []
    for idx in range(len(matr_a)):
        tmp = []
        for valA, valB in zip(matr_a[idx], matr_b[idx]):
            tmp.append(valA - valB)
        output.append(tmp[:])
    return output[:]

def getProbs(list):
    for i in range(len(list)):
        listsum = sum(list[i])
        if sum(list[i]) != 0:
            for j in range(len(list[i])):
                list[i][j] = list[i][j]/listsum
    return list

def NofAbsStates(list):
    count = 0
    for arr in list:
        for state in arr:
            if state != 0:
                count += 1
                break
    return (len(list)-count)

def sortStateIdx(list):
    index = []
    for i in range(len(list)):
        if all(state == 0 for state in list[i]):
            index.append(i)

    for i in range(len(list)):
        if any(state != 0 for state in list[i]):
            index.append(i)
    return index

def AbsStates(list):
    abslist = []
    for arr in list:
        if all(state == 0 for state in arr):
            abslist.append(arr)
    return abslist

def nonAbsStates(list):
    nonabslist = []
    for arr in list:
        for state in arr:
            if state != 0:
                nonabslist.append(arr)
                break
    return nonabslist

def sortstates(list):
    sortedstates = []
    absstates = AbsStates(list)
    for states in absstates: sortedstates.append(states)
    nonabsstates = nonAbsStates(list)
    for states in nonabsstates: sortedstates.append(states)   
    return sortedstates

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def getFR(list):
    QandR_ = [[0]*len(list) for i in range(len(list) - NofAbsStates(list))]
    QandR = sortstates(list)[NofAbsStates(list):len(list)]
    for i in range(len(QandR)):
        for j in range(len(QandR[i])):
            QandR_[i] = sortarray(QandR[i], sortStateIdx(list))
    Q, R =[], []
    for i in range(len(list) - NofAbsStates(list)):
        R.append(QandR_[i][0:NofAbsStates(lst)])
        Q.append(QandR_[i][NofAbsStates(lst):len(lst)])

    I = I_matrix(len(Q))
    Q_ = substact(I,Q)
    F = inverse(Q_)
    FR = multiply(F,R)
    return FR

lst = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
nicelist = getProbs(lst)

FR = getFR(nicelist)
FR_ = []
denoms = []
for element in FR[0]:
    FR_.append((Fraction(element)).limit_denominator())
for p in FR_:
    denoms.append(p.denominator)
lcm = 1
for i in denoms:
    lcm = lcm*i//math.gcd(lcm,i)
finallist = []
for i in FR_:
    p = i * lcm
    finallist.append(p.numerator)
finallist.append(lcm)

