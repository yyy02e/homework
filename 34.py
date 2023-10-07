class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        return

class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        return
    def isempty(self):
        if self.length == 0:
            return True
        else:
            return False
    def add(self,value):
        if not isinstance(value, Node):
            value = Node(value)
        if self.head is None:
            self.head = value
            self.tail = value
        else:
            self.tail.next = value
            self.tail = value
        self.length += 1
        return
    def delete(self,index):
        if self.isempty():
            print("Empty LinkList")
            return
        if index < 1 or self.length < index:
            print("index error: out of range")
            return
        pos = 1
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if pos == index:
                if prev_node is not None:
                    prev_node.next = current_node.next
                    return
                else:
                    self.head = current_node.next
                    return
            prev_node = current_node
            current_node = current_node.next
            pos += 1
        self.length -= 1
        return
    def search(self,value):
        current_node = self.head
        pos = 1
        result = []
        while current_node is not None:
            if current_node.value == value:
                result.append(pos)
            current_node = current_node.next
            pos += 1
        return result
    def change(self,position,value):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            if count == position:
               cur.value = value
               break
            else:
                cur = cur.next
        return
    def print_link(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
        return

Node1 = Node('1')
Node2 = Node('2')
Node3 = Node('3')
Node4 = Node('4')
link = Linklist()
for node in [Node1, Node2, Node3,Node4]:
    link.add(node)
link.print_link()
print('*********')
link.delete(3)
link.print_link()
print('*********')
link.change(2,'7')
link.print_link()
print('*********')
print(link.search('3'))