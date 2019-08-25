# Given a list of integers S and a target number k,
# write a function that returns a subset of S that adds up to k.
# If such a subset cannot be made, then return null.
# Integers can appear more than once in the list.
# You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

def subset(n, sum, i,result):

    if sum == 0:
        print(result)
        return True
    if sum!= 0 and i == 0:
        return False
    if n[i-1]>sum:
        return subset(n,sum,i-1,result)

    return subset(n,sum-n[i-1],i-1,result + [n[i-1]])|subset(n,sum,i-1,result)


def main():
    n = list(map(int,input("Enter numbers separated by space").split()))
    k = int(input("Enter k"))
    result=[]
    print(subset(n,k,len(n),result))


main()