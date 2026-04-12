# defines the blueprint for a single node in the linked list
class ListNode:
    def __init__(self, value, ref = None):
        self.val = value
        self.next = ref

def hasCycle(head: ListNode) -> bool: # function return annotation used
    if not head or not head.next: # in both cases cycle is not possible
        return False
    
    slow = head # creates a pointer that will move 1 step at a time
    fast = head # creates a pointer that will move 2 steps at a time
    # both start at the begining
    
    """ (while fast): Ensures the fast pointer hasn't hit the end of the list (None).
    and (fast.next): Since the hare moves two steps (fast.next.next), we must ensure the next 
    node isn't None to avoid a "Null Pointer" type error. """
    while fast and fast.next is not None:

        slow = slow.next # Move 1 step
        print(slow.val)          
        fast = fast.next.next # Move 2 steps
        if (fast) is not None: # to prevent error
            print(fast.val) 
        print("-----")    
        
        # If they meet, a cycle exists
        if slow == fast:
            return True
            
    return False

# 1. Creating nodes
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(40)

# 2. Connecting them: 10 -> 20 -> 30 -> 40
node1.next = node2
node2.next = node3
node3.next = node4

# 3. Case A: No Cycle
print("CASE:A")
print(f"Cycle detected (Case A): {hasCycle(node1)}") # Expected: False
print("")

print("CASE:B")
# 4. Case B: Creating a Cycle (40 -> 20)
node4.next = node2 
print(f"Cycle detected (Case B): {hasCycle(node1)}") # Expected: True