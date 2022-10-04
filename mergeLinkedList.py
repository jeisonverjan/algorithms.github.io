class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))
list2 = ListNode(1, ListNode(2, ListNode(4, ListNode(5, ListNode(6, None)))))

star = curr = ListNode()
while list1 and list2:
    if list1.val <= list2.val:
        curr.next = list1
        list1 = list1.next
    else:
        curr.next = list2
        list2 = list2.next
    curr = curr.next
    curr.next = list1 or list2

while star:
    print(star.val)
    star = star.next

