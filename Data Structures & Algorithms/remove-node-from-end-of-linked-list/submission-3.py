# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # go through once, determine length
        # subtract len - 2 + 1, run a for loop, then reassign pointers
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        node_del = length - n
        
        curr = head
        prev = None
        for i in range(node_del):
            if (i == node_del - 1):
                prev = curr
            curr=curr.next

        if (length == 1):
            return head.next
        elif (curr == head):
            return curr.next
        else:
            prev.next = curr.next
            return head
        # now at the node to delete
        
