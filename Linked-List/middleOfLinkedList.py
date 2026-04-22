class ListNode:
    def __init__(self, value, ref=None):
        self.value = value
        self.next = ref

def middleNode(head: ListNode) -> ListNode:
    if not head:
        return None
    
    slow, fast = head, head
    # The standard "Tortoise and Hare" approach
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# 1. Creating nodes
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(40)
node5 = ListNode(50)

# 2. Connecting them
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# 3. Getting the middle
result = middleNode(node1)
print(f"The middle node value is: {result.value}")