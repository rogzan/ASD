"""
Znany operator telefonii komórkowej w Polsce postanowił zakończyć działalność w Polsce. Jednym z głownych elementów
całej procedury jest wyłączenie wszyskich stacji nadawczych (które tworzą spójny graf połączeń). Ze względów
technologicznych urządzeni należy wyłączać pojedynczo a operatorowi dodatkowo zależy na tym, by podczas całego procesu
wszyscy abonenci znajdujący się w zasięgu działających stacji mogli się ze sobą łączyć (czyli by graf pozostał spójny).
Proszę zaproponować algorytm podający kolejność wyłączania stacji.
"""
def quickSort(arr,idx,left,right):
    if left<right:
        pi=partition(arr,idx,left,right)
        quickSort(arr,idx,left,pi-1)
        quickSort(arr,idx,pi+1,right)

def partition(arr,idx,left,right):
    i=left-1
    pivot=arr[right]
    for j in range(left,right):
        if arr[j]>=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            idx[i],idx[j]=idx[j],idx[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    idx[i+1],idx[right]=idx[right],idx[i+1]
    return i+1


def Rtel(g,visited,level,l,v):
    visited[v]=True
    level[v]=l

    for i in range(len(g)):
        if g[v][i]==1 and visited[i]==False:
            Rtel(g,visited,level,l+1,i)

def tel(g):
    n=len(g)
    visited=[False]*n
    level=[-1]*n
    v=0
    level[v]=0
    visited[v]=True
    l=0
    for i in range(n):
        if g[v][i]==1 and visited[i]==False:
            Rtel(g,visited,level,l+1,i)

    idx=[0]*n
    for i in range(n):
        idx[i]=i
    quickSort(level,idx,0,n-1)

    return idx


if __name__=="__main__":
    g=[[0,1,1,0,0,0],[1,0,1,0,0,0],[1,1,0,1,1,0],[0,0,1,0,0,0],[0,0,1,0,0,1],[0,0,0,0,1,0]]
    print(tel(g))
