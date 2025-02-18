class Node:
    def __init__(self, dado):
        self.data = dado
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
# Insere um nó no início
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
# Insere um nó no final
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    def delete_at_beginning(self):
        # Remove o primeiro nó
        if not self.head:
            print("Lista vazia!")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        # Remove o último nó
        if not self.head:
            print("Lista vazia!")
            return
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            current.prev.next = None
        else:
            self.head = None
    def display(self):
        #Exibe os elementos
        current = self.head
        while current:
            print(f"[{current.data}]", end=" ⇄ ")
            current = current.next
        print("None")

lista = DoublyLinkedList()

lista.insert_at_end('A')
lista.insert_at_end('B')
lista.insert_at_end('C')
lista.insert_at_end('D')
lista.display()