class Node:
    def __init__(self, dado):
        self.data = dado
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None  # Apenas referência para o primeiro nó

    def insertByPosition(self, data):
        new_node = Node(data)
        if not self.head:
            # Lista vazia: o novo nó se liga a si mesmo
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            # Acessamos o último nó usando head.prev
            last = self.head.prev

            # Inserimos o novo nó entre last e head
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def display(self, limit=5):  # Exibe os elementos, evitando loop infinito
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
