
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        new_head = None
        if not list1 and not list2:
            return new_head
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        if list1.val<list2.val:
            new_head = list1
            list1 = list1.next
        else:
            new_head = list2
            list2 = list2.next
        cond = True
        curr = new_head
        while cond:
            if list1==None and list2!=None:
                curr.next=list2
                return new_head
            elif list2==None and list1!=None:
                curr.next= list1
                
                return new_head
            if list1.val<list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

sol = Solution()
n1 = ListNode(val=1) 
n2 = ListNode(val=3) 
n3 = ListNode(val=4) 
n4 = ListNode(val=1) 
n5 = ListNode(val=2) 
n6 = ListNode(val=4) 
# n1.next= n2; n2.next=n3; n4.next=n5; n5.next= n6
sol.mergeTwoLists(n1, n5)