import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        flat_list = []
        h = []
        for i in range(len(lists)):
            if lists[i] != None:
                heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        while len(h) > 0:
            val, i = heappop(h)
            flat_list.append(val)
            if lists[i] != None:
                heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        def to_ListNode(i, arr):
            if i < len(arr):
                return ListNode(arr[i], to_ListNode(i + 1, arr))
            else:
                return None

        return to_ListNode(0, flat_list)
