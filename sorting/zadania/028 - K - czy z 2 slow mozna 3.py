"""
K 2012/2013 Zadanie 3

Proszę napisać funkcję possible(u,v,w), która zwraca prawdę, jeśli z liter słów u i v da się ułożyć słowo w
(nie jest konieczne wykorzystanie wszyskich liter) oraz fałsz w przeciwnym przypadku. Można założyć, że w i v składa
się wyłącznie z małych liter alfabetu łacińskiego.


"""


def possible(s1,s2,goal):

    counter=[0]*26
    for i in range(len(goal)):
        counter[ord(goal[i])-97]+=1

    for i in range(len(s1)):
        counter[ord(s1[i])-97]-=1
    for i in range(len(s2)):
        counter[ord(s2[i])-97]-=1

    for i in range(26):
        if counter[i]>0:
            return False

    return True

"""
O(n) gdzie n to długość najdłuższego słowa
"""

if __name__=="__main__":
    s1="ffdjoifgads"
    s2="eioutoeuo"
    goal="trahd"
    if possible(s1,s2,goal):
        print("tak")
    else:
        print("nie")
