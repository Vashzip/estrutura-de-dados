class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._head = None
        self._length = 0

    def insert_at_end(self, data):
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._length += 1

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self._length += 1

    def reverse(self):
        prev = None
        current = self._head

        while current:
            next_node = current.next  # Armazena o próximo nó
            current.next = prev  # Inverte o ponteiro do nó atual
            prev = current  # Move prev para o nó atual
            current = next_node  # Move current para o próximo nó

        self._head = prev  # Atualiza a cabeça da lista

    def display(self):
        current = self._head
        print('-------')
        print('N° de Elementos:', self._length)
        while current:
            print(current.data, end=' --> ')
            current = current.next


# Teste do código
linked = LinkedList()
linked.insert_at_end('A')
linked.insert_at_end('B')
linked.insert_at_end('C')
linked.insert_at_end('D')

linked.display()

linked.reverse()

linked.display()
