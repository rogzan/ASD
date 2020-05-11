"""
Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można osiągnąć ścieżką
skierowaną wychodzącą z v.
Proszę zaproponować algorym, który stwierdza czy dany graf zawiera dobry początek.


If there exist mother vertex (or vertices), then one of the mother vertices is the last finished vertex in DFS.
 (Or a mother vertex has the maximum finish time in DFS traversal).

Algorithm :

    Do DFS traversal of the given graph. While doing traversal keep track of last finished vertex ‘v’. 
    This step takes O(V+E) time.
    
    If there exist mother vertex (or vetices), then v must be one (or one of them). 
    Check if v is a mother vertex by doing DFS/BFS from v. This step also takes O(V+E) time.


"""
