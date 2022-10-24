from fractions import Fraction
import math
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
    return output

def getProbs(list):
    for i in range(len(list)):
        listsum = sum(list[i])
        if sum(list[i]) != 0:
            for j in range(len(list[i])):
                list[i][j] = float(list[i][j]/listsum)
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
    for states in absstates: 
        sortedstates.append(states)
    nonabsstates = nonAbsStates(list)
    for states in nonabsstates: 
        sortedstates.append(states)   
    return sortedstates

def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

# matrix determinant
def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))

    return d

# matrix inversion
def getMatrixInverse(m):
    d = getMatrixDeternminant(m)

    if d == 0:
        raise Exception("Cannot get inverse of matrix with zero determinant")

    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/d, -1*m[0][1]/d],
                [-1*m[1][0]/d, m[0][0]/d]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/d
    return cofactors

def getFR(list):
    QandR_ = [[0]*len(list) for i in range(len(list) - NofAbsStates(list))]
    QandR = sortstates(list)[NofAbsStates(list):len(list)]
    for i in range(len(QandR)):
        for j in range(len(QandR[i])):
            QandR_[i] = sortarray(QandR[i], sortStateIdx(list))
    Q, R =[], []
    for i in range(len(list) - NofAbsStates(list)):
        R.append(QandR_[i][0:NofAbsStates(list)])
        Q.append(QandR_[i][NofAbsStates(list):len(list)])

    I = I_matrix(len(Q))
    Q_ = substact(I,Q)
    F = getMatrixInverse(Q_)
    FR = multiply(F,R)
    return FR

def solution(m):
    # Your code here
    nicelist = getProbs(m)
    FR = getFR(nicelist)
    FR_ = []
    denoms = []
    for element in FR[0]:
        FR_.append((Fraction(element)).limit_denominator())
    for p in FR_:
        denoms.append(p.denominator)
    lcm = 1
    for i in denoms:
        lcm = int(lcm*i/float(math.gcd(lcm,i)))
    finallist = []
    for i in FR_:
        p = i * lcm
        finallist.append(p.numerator)
    finallist.append(lcm)
    return finallist

print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
