class listnode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverselist(head):
        prev = None
        curr = head 

        while curr :
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next_node

        return prev 

head = listnode(1)
head.next = listnode(2)
head.next.next = listnode(3)

print(head)

