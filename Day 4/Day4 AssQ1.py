class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def InsertBeg(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def DeleteEnd(self, data):
        new = Node(data)
        if self.head == None:
            print("No node to delete")
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp = temp.next





