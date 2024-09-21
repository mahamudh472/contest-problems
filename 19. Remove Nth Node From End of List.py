# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head , n: int) :
        '''
        Two pointer approch. time complexity(O(len))
        '''
        left = head
        right = head
        while n!=0:
            right = right.next
            n-=1
        if right == None:
            head = head.next
            return head
        while right.next:
            left= left.next
            right = right.next
        if left.next == None:
            del left
        else:
            left.next = left.next.next

        return head
        
        '''
        Brute Force approch. Time complexity(O(2*len))
        '''
        # count = 0
        # temp = head
         
        # while temp:
        #     count+=1
        #     temp = temp.next
        # if count == 1:
        #     del head
        #     return
        # count = count - n
        # if count == 0:
        #     head = head.next
        #     return head
        # temp2 = head
        # for i in range(count-1):
        #     temp2 = temp2.next
        # if temp2.next == None:
        #     del temp2
        # else:
        #     temp2.next = temp2.next.next

        # return head
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next=n2; n2.next=n3; n3.next=n4; n4.next=n5
# n1 = ListNode(1)
sol = Solution()
m = sol.removeNthFromEnd(n1, 2)
while m:
    print(m.val)
    m = m.next