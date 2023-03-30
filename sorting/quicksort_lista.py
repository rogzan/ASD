class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class List:
    def __init__(self, first=None, last=Node):
        self.first = first
        self.last = last

    def is_empty(self):
        return self.first is None

    def make_from_array(self, array):
        if len(array) == 0:
            return
        self.first = Node(array[0])
        p = self.first
        self.last = p
        for i in range(1, len(array)):
            q = Node(array[i])
            p.next = q
            p = q
            self.last = p

    def wypisz(self):
        p = self.first
        while p is not None:
            print(p.val, end=" ")
            p = p.next

    def has_one_element(self):
        return self.first == self.last

    def add(self, val):
        node = Node(val)
        if self.is_empty():
            self.first = node
            self.last = node
            return
        self.last.next = node
        self.last = node

def concatenate_lists(array_of_lists):
    result = List()
    foundbegining = False
    for i in array_of_lists:
        if not i.is_empty():
            i.last.next = None
    for i in array_of_lists:
        if not foundbegining and not i.is_empty():
            foundbegining = True
            result.first = i.first
            result.last = i.last
        elif not i.is_empty():
            result.last.next = i.first
            result.last = i.last
    return result


def quick_sort_on_list(list):
    if list.is_empty() or list.has_one_element():
        return list
    smaller = List()
    equal = List()
    greater = List()
    p = list.first
    while p is not None:
        if p.val < list.last.val:
            smaller.add(p.val)
        elif p.val == list.last.val:
            equal.add(p.val)
        else:
            greater.add(p.val)
        p = p.next
    return concatenate_lists([quick_sort_on_list(smaller), equal, quick_sort_on_list(greater)])

def QuickSort(l):
    full_list = List()
    p = l[0]
    while p is not None:
        full_list.add(p.val)
        p = p.next
    l = quick_sort_on_list(full_list)
    return l


l = List()
arr = [12, 33, 56, 34, 7, 111, 2, 0, 23]
print(arr)
l.make_from_array(arr)
l.wypisz()
print("")
q = QuickSort((l.first, l.last))
q.wypisz()
