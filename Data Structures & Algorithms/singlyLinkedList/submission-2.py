class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def get(self, index: int) -> int:
        if index == 0:
            if self.head is None:
                return -1
            else:
                return self.head.data
        else:
            idx = 0
            current = self.head
            while current.next is not None:
                current = current.next
                idx += 1

                if idx == index:
                    return current.data
            
            return -1

    def insertHead(self, val: int) -> None: # O(1)
        new_node = Node(data=val)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None: # O(1)
        new_node = Node(data=val)

        if self.tail is None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        if self.head is None:
            self.head = new_node

    def remove(self, index: int) -> bool: # O(n)
        if index == 0:
            if self.head is None:
                return False
            else:
                self.head = self.head.next
                return True
        else:
            idx = 0
            current = self.head
            while current.next is not None:
                if idx == index - 1:
                    if current.next.next is None:
                        self.tail = current
                    current.next = current.next.next
                    return True

                current = current.next
                idx += 1

            return False

    def getValues(self) -> List[int]: # O(n)
        linked_list = []
        current = self.head
        if self.head is None:
            return []
        else:
            while current.next is not None:
                linked_list.append(current.data)
                current = current.next

            linked_list.append(current.data)

            return linked_list
        
