"""
We have two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
We've to add the two numbers and return the sum as a linked list.

We may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
"""

'''
In this question there are lot of edge cases, so we've to take that in
mind and then solve the question carefully.
'''

class ListNode:
    def __init__(self, val = 0, ref = None):
        self.val = val
        self.next = ref


def addTwoNumbers(listNode1: ListNode, listNode2: ListNode) -> ListNode:
    dummy_head = ListNode() # it'll create a node with the value 0
    current = dummy_head
    carry: int = 0

    while listNode1 or listNode2 or carry:
        val1: int = listNode1.val if listNode1 else 0
        val2: int = listNode2.val if listNode2 else 0

        total: int = val1 + val2 + carry # adding the values of two linked list
        carry = total // 10 # setting the new value of carry (if carry is available)
        total %= 10 # we need the one's place in the new node
        
        current.next = ListNode(total)
        current = current.next

        if listNode1: listNode1 = listNode1.next
        if listNode2: listNode2 = listNode2.next
    
    return dummy_head.next


# node1 = ListNode(3, ListNode(4, ListNode(5, ListNode(6))))
# node2 = ListNode(2, ListNode(9, ListNode(8)))

# edge cases
node1 = ListNode(5)
node2 = ListNode(7)

resultant = addTwoNumbers(node1, node2)
while resultant is not None:
    print(resultant.val, end = ' -> ' if resultant.next else "")
    resultant = resultant.next