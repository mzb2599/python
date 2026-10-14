# Circular Linked List Implementation in Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)
    
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = new_node  # Point to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = new_node  # Point to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def find(self, data):
        if self.is_empty():
            return None

        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                break

        return None

    def delete(self, data):
        if self.is_empty():
            return False

        current = self.head
        prev = None

        while True:
            if current.data == data:
                if prev is None:  # Deleting head node
                    if current.next == self.head:  # Only one node in the list
                        self.head = None
                    else:
                        # Find the last node to update its next pointer
                        last_node = self.head
                        while last_node.next != self.head:
                            last_node = last_node.next
                        last_node.next = current.next
                        self.head = current.next
                else:
                    prev.next = current.next
                
                return True
            
            prev = current
            current = current.next
            
            if current == self.head:
                break
        
        return False

#Example usage:
if __name__ == "__main__":
    circular_list = CircularLinkedList()
    circular_list.append(1)
    circular_list.append(2)
    circular_list.append(3)
    circular_list.prepend(0)

    print("Circular Linked List:")
    current = circular_list.head
    for _ in range(5):  # Print 5 elements to show the circular nature
        print(current.data, end=" -> ")
        current = current.next
    print("... (circular)")

    print("\nFinding 2:", circular_list.find(2))
    print("Finding 4:", circular_list.find(4))

    print("\nDeleting 2:", circular_list.delete(2))
    print("Deleting 4:", circular_list.delete(4))

    print("\nCircular Linked List after deletion:")
    current = circular_list.head
    for _ in range(5):  # Print 5 elements to show the circular nature
        print(current.data, end=" -> ")
        current = current.next
    print("... (circular)")