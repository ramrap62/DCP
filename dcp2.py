def multiply_array(l):
    total=1
    for i in l:
        total = total * i
    m=[total for _ in range(len(l))]
    for i in range(len(l)):
        m[i]=m[i]//l[i]
    return m



def main():
    l=list(map(int,input().split()))
    print(multiply_array(l))

main()