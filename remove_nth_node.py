class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def remove_nth_node(head: ListNode, n : int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy

    for _ in range(n+1):
        fast  = fast.next

    while fast:
        fast = fast.next
        slow = slow.next
    slow = slow.next.next

    return dummy.next






