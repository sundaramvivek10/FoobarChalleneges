"""
Absorbing Markov Chain
"""

def numofabsorbingstates(list):
    count = 0
    for arr in list:
        for state in arr:
            if state != 0:
                count += 1
                break
    return (len(list)-count)

def absorbingstates(list):
    abslist = []
    for arr in list:
        if all(state == 0 for state in arr):
            abslist.append(arr)
    return abslist

def nonabsorbingstates(list):
    nonabslist = []
    for arr in list:
        for state in arr:
            if state != 0:
                nonabslist.append(arr)
                break
    return nonabslist

def sortstates(list):
    sortedstates = []
    absstates = absorbingstates(list)
    for states in absstates: sortedstates.append(states)
    nonabsstates = nonabsorbingstates(list)
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


lst = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

QandR = sortstates(lst)[numofabsorbingstates(lst):len(lst)]
Q, R =[], []
for i in range(len(lst) - numofabsorbingstates(lst)):
    R.append(QandR[i][0:numofabsorbingstates(lst)])
    Q.append(QandR[i][numofabsorbingstates(lst):len(lst)])

for i in (range(len(Q))):
    Q[i][i] =  1 - Q[i][i]

print(inverse(Q))


