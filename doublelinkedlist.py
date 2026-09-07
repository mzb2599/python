#Double linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def find(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return current
            current = current.next

        return None

    def delete(self, data):
        node = self.find(data)
        if node is None:
            return False

        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        node.next = None
        node.prev = None
        return True

    def forward(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values

    def backward(self):
        values = []
        current = self.tail

        while current is not None:
            values.append(current.data)
            current = current.prev

        return values


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.prepend(5)

    print("Forward:", linked_list.forward())
    print("Backward:", linked_list.backward())

    linked_list.delete(10)
    print("After deleting 10:", linked_list.forward())
