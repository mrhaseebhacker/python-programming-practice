# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def hasCycle(head):
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next         # Move slow by 1
#         fast = fast.next.next    # Move fast by 2
#         if slow == fast:
#             return True
#     return False
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Link them: 1 → 2 → 3 → None
node1.next = node2
node2.next = node3

# Check cycle
result = hasCycle(node1)
print(result)   # Output: False
