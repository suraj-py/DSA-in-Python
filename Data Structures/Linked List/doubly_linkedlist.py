class Node:

    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def get_lenght(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data, None, temp)

    def insert_at(self, data, index):
        if index<0 or index>self.get_lenght():
            raise Exception('index out of range!')

        elif index == 0:
            self.insert_at_begining(data)
            return

        else:
            count = 0
            temp = self.head
            while temp:
                if count == index-1:
                    node = Node(data, temp.next, temp)
                    if node.next:
                        node.next.prev = node
                    temp.next = node
                    break
                temp = temp.next
                count += 1

    def remove_at(self, index):
        if index<0 or index>self.get_lenght():
            raise Exception('error')

        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        else:
            count = 0
            temp = self.head
            while temp:
                if count == index:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                    break
                temp = temp.next
                count += 1

    def push(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)


    def print(self):
        temp = self.head
        List = ''
        while temp:
            List += str(temp.data) + ' -> '
            temp = temp.next
        return List

    def get_tail(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp
        # return temp.prev.data ( second last node)

    def print_reverse(self):
        temp = self.get_tail()
        List = ''
        while temp:
            List += str(temp.data) + ' -> '
            temp = temp.prev
        return List

dll = DoublyLinkedList()
dll.insert_at_begining(3)
dll.insert_at_begining(5)
dll.insert_at_end(8)
dll.insert_at(12, 1)
dll.remove_at(3)
dll.push(['C++', 'Python', 'Java', 'Golang', 'Javascript'])
print(dll.print())
print(dll.print_reverse())

