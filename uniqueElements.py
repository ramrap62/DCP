def unique(n):
    l=[]
    for i in n:
        if i in l:
            yield i
        else:
            l.append(i)
    return



def main():

    n = list(map(int,input().split()))
    l = list(unique(n))
    if len(l) == 0:

        print("Elements are unique")
    else:
        print("Repeated element {}".format(l))

main()