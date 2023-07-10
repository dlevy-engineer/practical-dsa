"""
Given the head of a linked list with an odd number of nodes head, return the value of the node in the middle.

For example, given a linked list that represents 1 -> 2 -> 3 -> 4 -> 5, return 3.
"""

def getMiddle(head: ListNode) -> ListNode:

    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

    return slow.val