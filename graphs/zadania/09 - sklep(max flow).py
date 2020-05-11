"""
Mamy dany graf skierowany oraz funkcję opisującą przepustowość każdej krawędzi (liczbę jednostek
towaru na godzinę, które mogą się przemieszczać krawędzią). Poza tym mamy zbiór wierzchołków-fabryk
oraz zbiór wierzchołków-sklepów. Dla każdej fabryki znamy liczbę, określającą ile jednostek
towaru na godzinę fabryka może maksymalnie produkować. Jednocześnie dla każdego sklepu mamy
liczbę, która mówi ile jednostek towaru na godzinę musi do sklepu docierać.
Proszę podać algorytm, który sprawdza czy da sie zapewnić, żeby do każdego sklepu docierało
z fabryk dokładnie tyle jednostek towaru, ile sklep wymaga jednocześnie nie zmuszając żadnej
fabryki do przekroczenia swoich możliwości produkcyjnych i nie przekraczając przepustowości
krawędzi.


Graf jest dwudzielny
Dopinamy duże źródło do źródeł - każda krawędź ma przepustowość równą max liczbie towaru
produkowanej przez daną fabrykę
dopinamy ujście - każda krawędż ma przepustowość równą liczbie towaru potrzebnego w sklepie

sprawdzamy czy max przepływ jest równy sumie potrzebnego towaru

"""
