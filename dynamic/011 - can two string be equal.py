"""
You can perform the following operations on the string a:
-Capitalize zero or more of a's lowercase letters.
-Delete all of the remaining lowercase letters in a.

Given two strings, a and b, determine if it's possible to make a equal to b as described.
If so, print YES on a new line. Otherwise, print NO.


"""


def abbreviation(a,b):

    ai=len(a)
    bi=len(b)


    f=[None]*(bi+1)
    for i in range(bi+1):
        f[i]=[False]*(ai+1)

    f[0][0]=True
    for i in range(ai+1):
        if a[i].islower():
            f[0][i+1]=True
        else:
            break

    for i in range(1,bi+1):
        for j in range(1,ai+1):
            if a[j-1]==b[i-1] or a[j-1].upper()==b[i-1]:
                f[i][j] = f[i - 1][j - 1] or f[i][j - 1]
            elif a[j-1].islower() and f[i][j-1]:
                f[i][j]=True
            else:
                f[i][j]=False
    print(f)
    if f[bi][ai]:
        return "YES"
    else:
        return "NO"


a="iiifPiiiiiii"
b="IP"
print(abbreviation(a,b))
