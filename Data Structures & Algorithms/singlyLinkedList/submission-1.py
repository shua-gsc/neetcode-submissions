# for the memes

class LinkedList:
    def __init__(self):
        self.list = []
        
    def get(self, index: int) -> int:
        if 0 <= index < len(self.list):
            return self.list[index]
        else:
            return -1
        
    def insertHead(self, val: int) -> None:
        self.list.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.list.append(val)

    def remove(self, index: int) -> bool:
        if 0 <= index < len(self.list):
            del self.list[index]
            return True
        return False
    
    def getValues(self) -> list[int]:
        return self.list