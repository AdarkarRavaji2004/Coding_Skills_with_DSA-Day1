import sys
class Node:
    def __init__(self,data):
        self.data= data #instance variable
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    #add node
    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def display(self):
        print("---------------------------------------------")
        while self.head is not None:
            print(self.head.data,'|','->', end=' ')
            self.head = self.head.next   
        print()    
        print("---------------------------------------------")

    def addNodeBeginning(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
    
    def addNodeEnd(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addNodeBetween(self,index,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for _ in range(1,index-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node

    def searchNode(self,value):
        temp = self.head
        while temp is not None:
            if temp.data == value:
                print("Node found in linked list")
                return
            temp = temp.next
        print("Node not found in linked list")
        
if __name__ == '__main__': 
    object = LinkedList()
    #Menu driven Operation
    while True:
        print("1.Add Node LinkedList")
        print("2.Add Node in beginning")
        print("3.Add Node in between")
        print("4.Add Node in end")
        print("5.Display LinkedList")
        print("6.Search Node in LinkedList")
        print("7.Exit")

        ch = int(input("Enter your choice : "))
        if ch == 1:
            value = int(input("Enter value for node : "))
            object.addNode(value)
            print("Node added successfully in single linked list")
        elif ch == 2:
            value = int(input("Enter value for node : "))
            object.addNodeBeginning(value)
            print("Node added successfully in Beginning")
        elif ch == 3:
            value = int(input("Enter value for node : "))
            index = int(input("Enter position after that you have to insert : "))
            object.addNodeBetween(index,value)
            print("Node added successfully in Between")
        elif ch == 4:
            value = int(input("Enter value for node : "))
            object.addNodeEnd(value)
            print("Node added successfully in End")
        elif ch == 5:   
            object.display()
        elif ch == 6:
            value = int(input("Enter value for node : "))
            object.searchNode(value)
        elif ch == 7:
            print("Exiting...")
            sys.exit()