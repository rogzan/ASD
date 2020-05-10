"""
Dana jest zawsze działająca w czasie O(1) funkcja dict(word), która mówi, czy słowo word jest poprawnym słowem danego
języka. Dostajemy na wejściu stringa bez spacji. Podaj algorytm, który stwierdzi, czy da się tak powstawiać spacje
do wejściowego stringa, że ciąg słów który otrzymamy tworzą słowa z danego języka. Np. “alamakotainiemapsa” możemy
zapisać jako “ala ma kota i nie ma psa”. Podaj również, jak wykorzystać algorytm, aby uzyskać przykładowe poprawne
rodzielenie stringa spacjami, jeśli oczywiście ono istnieje.

"""


def func_dict(s):
    arr=["i","zatem","nowy","za","owy","ala","ma","kota","psa","nie","iza","mowy","te"]
    if s in arr:
        return True
    return False

def p(parent,spaces,n):
    if parent[n]:
        spaces.append(n)
        if parent[n]==n:
            return
        p(parent, spaces, parent[n])


def string(s):
    n=len(s)
    f=[False]*n
    parent=[None]*n

    for i in range(0,n):
        sp=s[0:i+1]
        if func_dict(sp):
            f[i]=True
            parent[i]=i

    for i in range(n):
        for j in range(i+1,n):
            sp=s[i+1:j+1]
            if f[i] and func_dict(sp) and f[j]==False:
                parent[j]=i
                f[j]=True
    spaces=[]
    p(parent,spaces,n-1)
    print(spaces)

    return f[n-1]

#w tablicy spaces jest informacja po któym indeksie jest spacja

s="izatemowy"
if string(s):
    print("true")
else:
    print("false")

s="alamakotainiemapsa"
if string(s):
    print("true")
else:
    print("false")

s="izatemowkoloy"
if string(s):
    print("true")
else:
    print("false")
