"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # 원본 노드 -> 복사 노드 매핑
        old_to_new = {}
        
        # 1차 순회: 노드(값)만 먼저 전부 복사
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        
        # 2차 순회: next, random 포인터 연결
        cur = head
        while cur:
            copy_node = old_to_new[cur]
            copy_node.next = old_to_new.get(cur.next)
            copy_node.random = old_to_new.get(cur.random)
            cur = cur.next
        
        return old_to_new[head]