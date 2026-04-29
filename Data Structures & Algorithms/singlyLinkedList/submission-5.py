class Node:
    def __init__(self, val: int = 0, next: Node | None = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self._dummy = Node()
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self._dummy.next
        for _ in range(index):
            node = node.next
        return node.val
    
    def insertHead(self, val: int) -> None:
        node = Node(val, self._dummy.next)
        self._dummy.next = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val, None)
        if self.size == 0:
            self._dummy.next = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        prev = self._dummy
        for _ in range(index):
            prev = prev.next # move to the node before the node we are removing

        prev.next = prev.next.next # skip the node we are removing

        if index == self.size - 1:
            self.tail = prev if prev is not self._dummy else None

        self.size -= 1
        if self.size == 0:
            self.tail = None
        
        return True
    
    def getValues(self) -> list[int]:
        out: list[int] = []
        node = self._dummy.next
        while node is not None:
            out.append(node.val)
            node = node.next
        return out