"""
K 2014/2015 Zadanie 3

Jak posortować n-elemenową tablicę liczb rzeczywistych, które przyjmują
tylko log n różnych wartości? Uzasadnić poprawność algorytmu i oszacować
złożoność.

ROZWIĄZANIE:
Rozwiązanie opierać się będzie na stworzeniu listy list dwuelementowych, w których na pierwszej
pozycji występować będzie jedna z logn wartości a na drugiej krotność wystąpień danej wartości.
np dla tablicy [1,3,4,1,2,1,3,1,3,1], utworzona tablica miałaby postac aux=[[1,5],[3,3],[4,1],[2,1]]
Nalezy zadbać o to żeby tablica była cały czas posortowana po pierwszej wartości.
Tworzenie tej tablicy:
na początku deklaruję pusta tablicę
następnie liniowo iteruję po wszyskich wartościach w danej początkowo tablicy
dla każdej wartości sprawdzam za pomocą algorytmu binary search czy występuje już ona w tablicy aux
jeśli nie to należy rozszerzyć aux o jedną dwuelementową tablicę - na pierwszej pozycji wartośc, na drugiej
krotność równa 1, w tym przypadku za każdym należy jeszcze posortować po wartościach,
jeśli z kolei dana wartość występuje już w tablicy aux to inkrementuję tylko wartość licznika na drugiej pozycji

po przeiterowaniu przez wszyskie elementy tablicy wejściowej w tablicy aux znajdują się już
wszystkie wartości wraz ich liczebnością w tablicy wejściowej
należy teraz po kolei przejść po tablicy aux i zapisać w tablicy wejściowej każdy kolejny element tyle
razy na ile wskazuje druga pozycja przy danej wartości w tablicy aux

Złożoność
iterowanie po tablicy wejściowej: O(n)
    wyszukiwanie binarne w tablicy aux o max logn elementach: O(log(logn))
    sortowanie tablicy: O(logn)
przepisanie wartości do tablicy wejściowej: O(n)

czyli: O(n*log(logn)))

Uwaga do sortowania tablicy aux: jako że tylko jeden element nie jest na swojej pozycji to posortowanie
takiej tablicy jest liniowe względem ilości elementów w aux (np za pomocą insertion sorta dla tej nowej wartości)


"""
