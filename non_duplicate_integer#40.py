
# Given an array of integers where every integer occurs three times except for one integer,
# which only occurs once, find and return the non-duplicated integer.
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

def non_duplicate(n): #O(n)
    result=[]
    t=[]
    for i in n:
        if i in t:
            if i in result:
                result.remove(i)
        else:
            t.append(i)
            result.append(i)

    return result

def getsingle(n): #O(n) and O(1) space
    size = 16
    result = 0
    for i in range(size):

        bit_sum = 0
        bit_place = 1 << i

        for j in n:
            if j & bit_place:
                bit_sum+=1

        if bit_sum%3:
            result = result | bit_place
    return result

def main():
    n = list(map(int,input().split()))
    print(*non_duplicate(n))
    print("single occuring element is {}".format(getsingle(n)))
main()