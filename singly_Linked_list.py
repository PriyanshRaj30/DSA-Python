class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.start = None
    def insert_last(self,data):
        Newnode = Node(data)
        if self.start == None:
            self.start = Newnode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = Newnode
    def Delete_first(self):
        if self.start == None:
            print("Emty")
        else:
            self.start = self.start.next
    def View(self):
        if self.start == None:
            print("Epty")
        else:
            temp = self.start
            while temp.next != None:
                print(temp.data,end=" ")
                temp = temp.next

mylist = Linked_list()
mylist.insert_last(2)
mylist.insert_last(3)
mylist.insert_last(4)
mylist.View()
mylist.Delete_first()
mylist.View()
mylist.Delete_first()
mylist.View()
