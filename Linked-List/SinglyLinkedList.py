# Singly Linked List implementation in Python

# defines the blueprint for a single node in the linked list
class Node:
    def __init__(self, data, ref = None):
        self.data = data
        self.next = ref

class SinglyLinkedList: # head is the first node of the linked list
    def __init__(self, head = None):
        self.head = head
    
    def insert_at_end(self, info):
        new_node = Node(info)
        if self.head is None:
            self.head = new_node
            return # Exit early if list was empty
        
        current = self.head
        while current.next: # Short for 'current.next is not None'
            current = current.next
        current.next = new_node

    def print_linked_list(self):
        current = self.head
        while current.next is not None:
            print(current.data, end = " ->")
            current = current.next
        print(current.data)

object = SinglyLinkedList() # creates an object of the SinglyLinkedList class
object.insert_at_end(10)    
object.insert_at_end(20)    
object.insert_at_end(30)    

object.print_linked_list()
