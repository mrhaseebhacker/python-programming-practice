class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = 0
        self.next = next

def merged_list(list1 : ListNode, list2 : ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1 < list2:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next       