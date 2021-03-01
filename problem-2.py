#Add Two Numbers


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        mylistnode = ListNode(0)
        newnode = mylistnode
        carry = 0
        while l1 or l2 or carry:
            
            if l1:
                pass
            else: 
                l1 = ListNode(0)
            if l2:
                pass
            else: 
                l2 = ListNode(0)
                
            r = (l1.val+l2.val+carry)%10
            carry = (l1.val+l2.val+carry)//10
            
            newnode.next = ListNode(r)
            newnode = newnode.next

            
            if l1.next:
                l1 = l1.next 
            else:
                l1 = None
            if l2.next:
                l2 = l2.next
            else:
                l2 = None
                
        return mylistnode.next