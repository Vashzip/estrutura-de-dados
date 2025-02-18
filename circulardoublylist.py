class Node:
    def __init__(self, dado):
        self.data = dado
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            last = self.head.prev  # Último nó antes da inserção
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def display(self, limit=8):  # Define um limite para evitar loop infinito
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

# Criando a lista circular
lista_circular = CircularDoublyLinkedList()
lista_circular.insert_at_end('A')
lista_circular.insert_at_end('B')
lista_circular.insert_at_end('C')
lista_circular.insert_at_end('D')

# Exibindo os elementos em ordem circular
lista_circular.display()