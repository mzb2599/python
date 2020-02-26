class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def AddNode(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node


    def RemoveNode(self, index):
        prev = None
        node = self.head
        i = 0
        while ((node != None) and (i < index)):
            prev = node
            node = node.next
            i += 1
        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next


    def PrintList(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next
List = LinkedList()
List.AddNode(1)
List.AddNode(2)
List.AddNode(3)
List.AddNode(4)
#List.PrintList()
List.RemoveNode(4) 
List.PrintList()
## Using python list library
List = []
List.append(1)
List.append(2)
List.append(3)
List.append(4)
for i in List:
    print(i)
