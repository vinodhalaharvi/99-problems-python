def last(lst, k): 
    return lst[len(lst)-k]

def count(lst): 
    count = 0
    for i in range(len(lst)): 
        count += 1
    return count

def reverse(lst): 
    rev = []
    for i in range(len(lst)): 
        rev.append(lst[len(lst) - i - 1])
    return rev

def isPalindrome(lst): 
    for i in range(len(lst)):
        if lst[i] != lst[len(lst) - i - 1]: 
                return False
    return True

def isList(lst): 
    return isinstance(lst, list)

def flatten(nestedLst, rslt): 
    for i in range(len(nestedLst)): 
        if isList(nestedLst[i]): 
            flatten(nestedLst[i], rslt)
        else: 
            rslt.append(nestedLst[i])
    return rslt


def unique(lst):
    dct = {}
    for i in range(len(lst)):
        dct[lst[i]] = True
    return dct.keys()

def uniqueCons(lst): 
    rslt = []
    for i in range(len(lst)-1): 
        if lst[i] == lst[i+1]: 
            pass
        else: 
            rslt.append(lst[i])
    rslt.append(lst[i+1])
    return rslt

def runLength(lst): 
    dct = {}
    rslt = []
    for i in range(len(lst)): 
        try:
            dct[lst[i]]
        except:
            dct[lst[i]] = 0
        dct[lst[i]] += 1
    for k, v in dct.items(): 
        rslt.append((k, v))
    return rslt


def dupli(lst, n):
    rslt = []
    for i in range(len(lst)):
        for j in range(n):
            rslt.append(lst[i]) 
    return rslt

def drop(lst, n):
    rslt = []
    for i in range(len(lst)):
        if i == n-1: 
            continue 
        else: 
            rslt.append(lst[i])
    return rslt


def split(lst, n):
    if n > len(lst): 
        return lst, []
    rslt1, rslt2 = [], []
    for i in range(len(lst)):
        if i == n:
            rslt1.append(lst[i])
        else:
            rslt2.append(lst[i])
    return rslt1, rslt2


def slice(lst, l, h): 
    rslt = []
    for i in range(len(lst)): 
        if i >= l and i < h: 
            rslt.append(lst[i])
    return rslt

def rotate(lst, n): 
    from collections import deque
    print("here")
    q = deque([])
    for i in range(len(lst)): 
        q.append(lst[i])
    for i in range(n): 
        q.append(q.popleft())
    print ("q", q)
    return list(q)

def insertAt(lst, p, n):
    rslt = []
    for i in range(len(lst)): 
        if i == p: 
            rslt.append(n)
            rslt.append(lst[i])
        else: 
            rslt.append(lst[i])
    return rslt

def rangelh(l, h):
    if l > h: 
        return []
    i = l
    rslt = []
    while i <= h: 
        rslt.append(i)
        i += 1
    return rslt


def randomListWithReplacement(lst, n): 
    rslt  = []
    from random import randrange
    for i in range(n):
        rslt.append(lst[randrange(len(lst))])
    return rslt

if __name__ == "__main__":
    print "last =" , (last([1, 2, 3], 2))
    print "count =" , (count([1, 2,3]))
    print "reverse =" , (reverse([1, 2,3]))
    print "isPalindrome =" , (isPalindrome([1, 2, 3]))
    print "isPalindrome =" , (isPalindrome([1, 2, 1]))
    print "flatten =" , flatten([1, [2, [1, 2,3]]], [])
    print "unique =" , unique([1, 2, 2, 3])
    print "uniqueCons = " , uniqueCons([1, 2, 2, 3, 2])
    print  "runLength" , runLength([1, 2, 2, 3])
    print "duplicate", dupli([1, 2,3], 3)
    print "drop", drop([1,2,3], 2)
    print "split", split([1,2, 3], 3)
    print "slice", slice([1, 2, 3], 1, 5)
    print "rotate", rotate([1, 2, 3], 2)
    print "insertAt", insertAt([1, 2,3], 2, 5)
    print "rangelh", rangelh(2, 5)
    print "randomListWithReplacement", randomListWithReplacement([1,2,3, 4], 1000)
