#Dana jest listaIprzedziałów domkniętych[a1, b1],[a2, b2], . . . ,[an, bn]. 
# Napisz funkcjęintervals(I ),  która  oblicza  dla  każdegoi∈{1,2, . . . , n} długość  najdłuższego  ciągłego  przedziału,
# który można  osiągnąć  sumując  wybrane  przedziały  spośród  pierwszychiprzedziałów  z  listy.  Funkcja powinna być 
# możliwie jak najszybsza.Przedziały reprezentowane są w postaci listy par. Funkcja powinna zwrócić listę liczb, w której i-ty 
# element to długość poszukiwanego najdłuższego przedziału zbudowanego z pierwszychielementówwejścia. Na przykład, dla listy odcinków:
# [(1,3),(5,6),(4,7),(6,9)]rozwiązaniem jest lista[2, 2, 3, 5]zawierająca długości odcinków:[1, 3],[1, 3],[4, 7]oraz[4, 9]



from inttree import *

def intervals(I):
    result = [I[0][1] - I[0][0]]
    edges = [edge for tpl in I for edge in tpl]

    print("-----------------------------------")

    edges = sorted(edges)

    uniq_edges = [edges[0]]

    for edge in edges:
        if edge != uniq_edges[len(uniq_edges) - 1]:
            uniq_edges.append(edge)

    T = tree(uniq_edges)
    tree_insert(T, I[0])

    for i in range(1, len(I)):
        res = max(result[i - 1], I[i][1] - I[i][0])
        print(res)
        new_span = I[i]
        tree_insert(T, new_span)

        left = tree_intersect(T, new_span[0])
        right = tree_intersect(T, new_span[1])


        if len(left) > 1 and len(right) > 1:
            a = min([tup[0] for tup in left])
            b = max([tup[1] for tup in right])
            for tup in left:
                tree_remove(T, tup)
            for tup in right:
                tree_remove(T, tup)
            if b - a > res:
                res = b - a

            tree_insert(T, (a, b))
        else:
            if len(right) > 1:
                a = min([tup[0] for tup in right])
                b = max([tup[1] for tup in right])
                print(a,b)
                for tup in right:
                    tree_remove(T, tup)

                if b - a > res:
                    res = b - a

                tree_insert(T, (a, b))
            if len(left) > 1:
                a = min([tup[0] for tup in left])
                b = max([tup[1] for tup in left])
                for tup in left:
                    tree_remove(T, tup)

                if b - a > res:
                    res = b - a

                tree_insert(T, (a, b))

        result.append(res)

    return result

run_tests(intervals)
