"""

Mamy dany pewnien rozkład pociągów, dany jako (arrival_time,departure_time), przy czym są one posortowane niemalejąco
wedlug arrival time. Chcemy wiedzieć, czy nasza stacja mająca m peronów jest w stanie bezkonfliktowo obsłużyć te pociągi
(w żadnym momencie nie będzie "rywalizacji" pociągów o kolejne perony.)
Przedstaw algorytm, który poda odpowiedź True lub False na to pytanie

"""
#zakładam że w drugiej kolejności jest posortowany po departure time


def station(trains,m):




    i=0
    j=0

    counter=0

    while i<len(trains) and j<len(trains):
        if trains[i][0]<trains[j][1]:
            counter+=1
            i+=1
            if counter>m:
                return False
        else:
            counter-=1
            j+=1


    return True



if __name__=="__main__":
    trains=[[1,4],[1,5],[2,3],[3,5],[4,6],[5,8],[6,7],[6,7],[8,10]]
    m=4
    if(station(trains,m)):
        print("True")
    else:
        print("False")
