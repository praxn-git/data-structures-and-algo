class ListNode:
    def __init__(self, value, ref=None):
        self.value = value
        self.next = ref

def middleNodeDeletion(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None
    
    # Use a dummy node to handle the "prev" pointer easily, 
    # especially for short lists.
    dummy = ListNode(0, head)
    slow, fast = dummy, head
    
    # When fast reaches the end, slow will be the node BEFORE the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # slow is now at the node before the middle, so delete the next one
    slow.next = slow.next.next
    
    return dummy.next

# 1. Creating nodes: 10 -> 20 -> 30 -> 40
node1 = ListNode(10, ListNode(20, ListNode(30, ListNode(40))))

# 2. Deletion
new_head = middleNodeDeletion(node1)

# 3. Printing the list to verify: 10 -> 20 -> 40 (30 deleted)
curr = new_head
while curr:
    print(curr.value, end=" -> " if curr.next else "")
    curr = curr.next