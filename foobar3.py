def checkafter(array,pos):
    count = 0
    for i in range(pos,len(array)):
        if array[i] == '<':
            count+=1
    return 2*count

def solution(s):
    # Your code here
    salutes = 0
    for i in range(len(s)):
        if array[i] == '>':
            salutes += checkafter(s,i)
print (salutes)