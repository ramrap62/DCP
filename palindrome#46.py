def makingStrings(n,res,i):
    if i == 0:
        return res
    if palindrome(res):
        print(len(res))
    res = makingStrings(n,res+n[i],i-1)


def palindrome(n):


def main():
    n = input()
    palindrome(n)

main()