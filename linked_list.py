class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.append(data)

    def len(self):
        if self.head is None:
            return 0
        cont = 0
        itr = self.head
        while itr:
            cont += 1
            itr = itr.next
        return cont

    def remove(self, index):
        if index < 0 or index >= self.len():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        if itr.data == data:
            self.head = self.head.next
            return

        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            if not itr.next:
                raise Exception('Value not Found')

    def insert_at(self, index, data):
        if index < 0 or index > self.len():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    my_linked_list = Linked_list()
    my_linked_list.insert_values([5, 6, 7, 1, 2, 3])
    my_linked_list.remove_by_value(6)
    my_linked_list.print()
