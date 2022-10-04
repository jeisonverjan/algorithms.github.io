class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))

start=node=head
node=head.next

while start and node:
    if start.val == node.val:
        start.next = node.next
        node = start.next
    else:
        start = start.next
        node = node.next

#while head:
    #print(head.val)
    #head = head.next

head = ListNode()
for i in range(6):
    node = ListNode(i, head)
    head = node

while head.next:
    print(head.val)
    head = head.next
