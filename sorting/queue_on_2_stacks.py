#In this method, in en-queue operation, the new element is entered
# at the top of stack1. In de-queue operation, if stack2 is empty
# then all the elements are moved to stack2 and finally top of stack2 is returned


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):
        self.s1.append(x)

    def deQueue(self):
        if len(self.s1) == 0 and len(self.s2) == 0:
            return
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1[-1])
                self.s1.pop()

            # Push item into self.s1
        x = self.s2[-1]
        self.s2.pop()
        return x

if __name__ == '__main__':
    q = Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
