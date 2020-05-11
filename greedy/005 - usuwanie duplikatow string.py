"""
Dany jest string, w którym niektóre litery się powtarzają. Należy zaproponować algorytm, który usunie
ze stringa duplikaty tak, że otrzymany string będzie leksykograficznie najmniejszy.
"""

def deleteDuplicate(s):

    counter=[0]*26
    visited=[False]*26

    for i in range(len(s)):
        counter[ord(s[i])-97]+=1

    result=[]

    for c in s:
        counter[ord(c)-97]-=1

        if not visited[ord(c)-97]:
            while len(result) and result[-1]>c and counter[ord(result[-1])-97]>0:
                visited[ord(result[-1])-97]=False
                result.pop(-1)

            result.append(c)
            visited[ord(c)-97]=True

        print(result)






if __name__=="__main__":
    s="cbacdcbc"
    deleteDuplicate(s)
