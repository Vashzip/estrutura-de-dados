class Node:
    def __init__(self, dado):
        self.data = dado
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertByPosition(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def display(self, limit=5):
        if not self.head:
            print("Lista vazia!")
            return
        current = self.head
        count = 0
        while count < limit:
            print(f"{current.data}", end=" -> ")
            current = current.next
            count += 1
        print("...")

lista_circular = CircularDoublyLinkedList()
lista_circular.insertByPosition('A')
lista_circular.insertByPosition('B')
lista_circular.insertByPosition('C')
lista_circular.insertByPosition('D')

lista_circular.display()
