# Project:Single linked list
# Filename: c:\Users\MOHD ZAKI\helloworld\linkedList.py
# Path: c:\Users\MOHD ZAKI\helloworld
# Created Date: Sunday, June 20th 2021, 3:02:26 pm
# Author: Mohammed Zaki


#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.tail=None

#Linked List class  
class linkedList:
    def __init__(self):
        self.head = None

    #Add a new node
    def AddNode(self,data):
        newNode = Node(data)
        if (self.head == None):
            self.head = Node(data)
            self.tail=self.head
        else:
            #ptr = self.head
            # while (ptr.next):
            #     ptr = ptr.next
            # ptr.next = Node(data)'
            self.tail.next = Node(data)
            self.tail = self.tail.next

        prt=self.tail
        return self.head

    #Print the list 
    def Printlist(self):
        ptr = self.head
        if (ptr) == None:
            print("No element present in the linked list")
        while (ptr):
            print(ptr.data)
            ptr = ptr.next
        

l = linkedList()
l.AddNode(5)
l.AddNode(1)
l.AddNode(7)
l.Printlist()
            
        

        
        
