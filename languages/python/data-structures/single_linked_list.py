class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # 노드 객체를 저장

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

n1 = LinkedList()
n1.insert_at_head(1)
n1.insert_at_head(2)
n1.insert_at_head(3)
n1.print_list()

            