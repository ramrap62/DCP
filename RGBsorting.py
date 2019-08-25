#Given an array of strictly the characters 'R', 'G', and 'B',
#Segregate the values of the array so that all the Rs come first,
#The Gs come second, and the Bs come last. You can only swap elements of the array.

#Do this in linear time and in-place.

def RBGsorting(n):
    left = 0
    piv = 0 #pivot
    right = len(n)-1

    while piv <= right :
        if n[piv]=='R':
            swap(n, piv,left)
            piv+=1
            left+=1
        elif n[piv] == 'G':
            piv+=1
        else:
            swap(n,piv,right)
            right-=1
    return

def swap(n,i,j):
    n[i],n[j] = n[j],n[i]
    return

def main():
    n = input().split()
    RBGsorting(n)
    print(n)

main()