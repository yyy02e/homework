class Node():
    def init(self,value):
        self.value = value
        self.next = None
class Linklist():
    def init(self):
        self.head = None
    def empty(self):
        return self.head == None
    def length(self):
        if self.empty():
            return 0
        else:
            cur = self.head
            count = 1
            while cur.next != None:
                count += 1
                cur = cur.next
            return count
    def add(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
    def delete(self,index):
        if index < 0 or index > (self.length()-1):
            print("No")
        elif index == 0:
            self.head = self.head.next
        else:
            count = 1
            pre,cur = self.head,self.head.next
            while count < index:
                count += 1
                pre,cur = cur,cur.next
            pre.next = cur.next
    def search(self,value):
        count = 0
        cur = self.head
        index = []
        while cur != None:
            if cur.value == value:
                index.append(count)
            count += 1
            cur = cur.next
        if not index:
            return False
        else:
            return index
    def change(self,position,value):
        cur = self.head
        count = 0
        while cur != None:
            count += 1
            if count == position:
               cur.value = value
               break
            else:
                cur = cur.next
x = input()
Node(x)
y = input()
Linklist(y)
