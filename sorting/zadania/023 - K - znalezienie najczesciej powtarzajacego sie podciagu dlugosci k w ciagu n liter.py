"""
K 2016/2017 Zadanie 3

Proszę opisać (bez implementacji!) jak najszybszy algorytm, który orzymuje na wejściu pewien ciąg n liter
oraz liczbę k i wypisuje jak najczęściej powtarzający się podciąg długości k (jeśli ciągów mogących stanowić
rozwiązanie jest kilka, algorytm zwraca dowolny z nich). Można założyć, że ciąg składa się wyłącznie
z liter a i b.
Na przykład dla ciągu ababaaaabb oraz k=3 rozwiązaniem jest zarówno aba, który powtarza się dwa razy (to że
wystąpienia zachodzą na siebie nie jest istotne)
Zaproponowany algorytm opisać, uzasadnić jego poprawność oraz oszacować złożoność.



ROZWIĄZANIE:

W pierwszej kolejności zamieniam literę a na 0, a literę b na 1.                                                                    O(n)
Teraz kążdemu podciągowi będę mogła przypisać liczbę dziesiętną - np. bab (101) = 5                                                 
Tworzę nową tablicę w której będę gromadzić przypisane ciągom liczby dziesiętne, jej długość to (n-k+1), bo tyle maksymalnie        O(n)
mogę mieć różnych wartości.
Liniowo iteruję po ciągu n liter i dodaję liczby dziesiętne odpowiadające każdemu podciągowi do poprzednio utworzonej               O(n)
tablicy.
Sortuję zawartość tej tablicy używając bucket sort, ponieważ mogę założyć że wartości są rozłożone jednostajnie.                    O(n)
(uwaga: dla bardzo małych k=1,2,3 bardziej opłaca się użyć counting sorta)
Na samym końcu iteruję po już posortowanej tablicy szukając najczęściej występującej liczby (zapamiętując counter i wartosć)        O(n)
Otrzymaną wartośc zamieniam na liczbę binarną a następnie na ciąg liter i zwracam jako wynik.                                       O(1)

Złożonośc:
5*O(N)+O(1)=O(N)
