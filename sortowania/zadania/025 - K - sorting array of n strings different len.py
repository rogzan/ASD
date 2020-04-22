"""
K 2014/2015 Zadanie 1

Napisać funkcję sortString(a), która sortuje tablicę n stringów różnej długości. Można założyć, że stringi składają
się wyłącznie z małych liter alfabetu łacińskiego.

"""

def countingSort(a,p):
    counter=[0]*26

    for i in range(len(a)):
        if len(a[i])<=p:
            counter[ord("a")-97]+=1
        else:
            counter[ord(a[i][p])-97]+=1

    for i in range(1,26):
        counter[i]+=counter[i-1]

    output=[None]*len(a)

    for i in range(len(a)-1,-1,-1):
        if len(a[i])<=p:
            output[counter[0]-1]=a[i]
            counter[0]-=1
        else:
            output[counter[ord(a[i][p])-97]-1]=a[i]
            counter[ord(a[i][p])-97]-=1

    return output

def sortString(a):

    mx_len=0
    for i in range(len(a)):
        if mx_len<len(a[i]):
            mx_len=len(a[i])


    for i in range(mx_len-1,-1,-1):
        a=countingSort(a,i)

    return a

if __name__=="__main__":
    a=["lalka","ala","ekson","zaraza","bazg","aaa","aneta","jo","aa","baba","masa"]
    a=sortString(a)
    print(a)
