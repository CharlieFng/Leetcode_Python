class Solution(object):
    def reverseList(self, head):
        
        prev = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev




     def reverseList2(self, head):
     	return self.doReverse(head,None)


     def doReverse(self, head, newHead):
     	if head is None:
     		return newHead

     	next = head.next
     	head.next = newHead
     	return self.doReverse(next, head)