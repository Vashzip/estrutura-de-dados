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
            print(current.data)
            print(current.next)

            while current.next:
                current = current.next
            current.next = new_node
        self._length+=1
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
    def delete_at_end(self):
        prev = None
        current = self._head
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        current = None
        self._length-=1

    def delete_at_beginning(self):
        if not self.head:
            print("Lista vazia!")
            return
        self.head = self.head.next
        self._length-=1
    def search_by_key(self, key):
        current = None
        pos = 0
        if self._head is not None:
            current = self._head

        while current:
            if current._data == key:
                print('Posição:',pos)
                print('Data:', current.data)
                print('Object', current)

                return current
            else:
                current = current.next

            pos+=1
        return current

    def insertByPosition(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self._head
            self._head = new_node
            self._length += 1
            return

        current = self._head
        pos = 0

        while current and pos < position - 1:
            current = current.next
            pos += 1

        if current is None:
            print("Posição inválida!")
            return

        new_node.next = current.next
        current.next = new_node
        self._length += 1

    def display (self):
        current = self._head
        str_return = ''
        print('-------')
        print('N° de Elementos:', self._length)
        while current:
            print(current.data, end='-->')
            current = current.next

linked = LinkedList()
linked.insert_at_end('A')
linked.insert_at_end('B')
linked.insert_at_end('C')
linked.insert_at_end('D')

linked.insertByPosition('X', 3)

linked.display()