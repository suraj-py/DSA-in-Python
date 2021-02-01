class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

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
            node = Node(data, self.head)
            self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def insert_at(self, data, index):
        if index<0 and index>self.get_lenght():
            raise Exception('error')

        elif index == 0:
            self.insert_at_begining(data)
            return

        else:
            count = 0
            temp = self.head
            while temp:
                if count == index-1:
                    node = Node(data, temp.next)
                    temp.next = node
                    break
                temp = temp.next
                count += 1

    def remove_at(self, index):
        if index<0 and index>self.get_lenght():
            raise Exception('error')

        elif index == 0:
            self.head = self.head.next
            return

        else:
            count = 0
            temp = self.head
            while temp:
                if count == index-1:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                count += 1



    def print(self):
        temp = self.head
        llist = ''
        while temp:
            llist = llist + str(temp.data) + ' -> '
            temp = temp.next
        print(llist)

ll = LinkedList()
ll.insert_at_begining(2)
ll.insert_at_begining(3)
ll.insert_at_end(4)
ll.insert_values([1, 3, 4, 5])
ll.insert_at(9, 2)
ll.remove_at(2)
print(ll.get_lenght())

ll.print()
