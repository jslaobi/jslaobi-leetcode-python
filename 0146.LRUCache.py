class Node:
    def __init__(self, key=0, val=0):
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # 需要一个double linked list来帮助记忆元素的顺序,在链表中考前的就是最近使用的元素. 当达到capacity时,再插入元素就需要从链表最后面删除不常用的元素
        # 这里的head和tail都是dummy节点,用来获取真正的第一个节点(head.next)和最后一个节点(tail.prev)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.next = self.head

    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 因为元素最近使用过, 所以移动到链表的开头
            self._remove_node(node)
            self._add_to_head(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        # 如果存在于缓存, 从缓存中删除以便更新
        if key in self.cache:
            self._remove_node(self.cache[key])
        
        new_node = Node(key, value)
        self._add_to_head(new_node)
        self.cache[key] = new_node


        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            del self.cache[lru_node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)