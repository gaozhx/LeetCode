# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 is None):
            return l2
        if(l2 is None):
            return l1
        ln1=l1
        ln2=l2
        while(ln1.next is not None or ln2.next is not None):
            if(ln1.next is None):
                ln1.next=ListNode()
            if(ln2.next is None):
                ln2.next=ListNode()
            ln1=ln1.next
            ln2=ln2.next
        ln1=l1
        ln2=l2
        c=0
        while(ln1.next is not None):
            if(ln1.val+ln2.val+c<10):
                ln2.val=ln1.val+ln2.val+c
                c=0
            else:
                ln2.val=(ln1.val+ln2.val+c)%10
                c=1
            ln1=ln1.next
            ln2=ln2.next
        if (ln1.val + ln2.val + c < 10):
            ln2.val = ln1.val + ln2.val + c
            c = 0
        else:
            ln2.val = (ln1.val + ln2.val + c) % 10
            c = 1
        if(c==1):
            ln2.next=ListNode()
            ln2.next.val=c
        return l2