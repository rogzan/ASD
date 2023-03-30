class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  

def insertionSort(head_ref): 
    sorted = None
    current = head_ref 
    while (current != None): 
        next = current.next
        sorted = sortedInsert(sorted, current) 
        current = next
    head_ref = sorted
    return head_ref 
  
def sortedInsert(head_ref, new_node): 
    current = None
    if (head_ref == None or (head_ref).data >= new_node.data):     
        new_node.next = head_ref 
        head_ref = new_node 
    else:     
        current = head_ref 
        while (current.next != None and current.next.data < new_node.data):          
            current = current.next          
        new_node.next = current.next
        current.next = new_node      
    return head_ref 
