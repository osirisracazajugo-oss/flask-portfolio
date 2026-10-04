class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove_beginning(self):
        if self.head is None:
            return None
        
        data = self.head.data

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return data

    def remove_at_end(self):
        if self.tail is None:
            return None
        
        data = self.tail.data

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else: 
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node

        return data

    def remove_at(self, data):
        current_node = self.head
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None

        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next

        if current_node is self.tail:
            self.tail = previous_node

        return current_node.data
        
    def insert_after(self, nodedata, data):
        current_node = self.head
        while current_node and current_node.data != nodedata:
            current_node = current_node.next

        if current_node is None:
            return None

        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node

        if current_node is self.tail:
            self.tail = new_node


if __name__ == "__main__":
    ll = LinkedList()
    for value in [10, 20, 30]:
        ll.insert_at_end(value)
    ll.printLinkedList()
