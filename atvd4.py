class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._length = 0

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._length += 1

    def insertAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self._length += 1

    def reverse(self):
        prev = None
        current = self._head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self._head = prev

    def display(self):
        current = self._head
        print('\nN° de Elementos:', self._length)
        while current:
            print(current.data, end=' --> ')
            current = current.next


# Teste do código
linked = LinkedList()
linked.insertAtEnd('A')
linked.insertAtEnd('B')
linked.insertAtEnd('C')
linked.insertAtEnd('D')

linked.display()

linked.reverse()

linked.display()
