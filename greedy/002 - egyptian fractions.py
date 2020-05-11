"""
Egyptian Fractions
"""


from math import ceil


def substractFr(a,b):

    m1=a[1]

    a[0]*=b[1]
    a[1]*=b[1]
    b[0]*=m1
    b[1]*=m1

    a[0]-=b[0]


    return a



def fractions(fr):


    result=[]

    while fr[0]!=0:

        s=ceil(fr[1]/fr[0])
        p=[1,s]
        result.append(p)
        b=p[:]
        fr=substractFr(fr,b)



    print(result)


if __name__=="__main__":

    fr=[5,17]
    fractions(fr)
