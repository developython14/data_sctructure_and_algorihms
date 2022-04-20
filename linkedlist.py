
from queue import Empty


class linkedlist :
    """_linked list implemenation lIFO STACK_
    """
    class _node:
        """_non public class to store nodes_
        """
        slots = '_element' , '_next' # streamline memory usage

        def __init__(self,element,next):
            """_initialite the node elemement_

            Args:
                element (_type_): _description_
                next (function): _description_
            """
            self._element = element # reference to user’s element
            self._next = next
    def __init__(self ):
        """_initilaite the stack_
        """
        self.head = None
        self._size = 0

    def __len__(self):
        """_return the lenght of the stack_
        """
        return self._size
    
    def is_empty(self):
        """_test if the stack is empty_

        Returns:
            _type_: boolean
        """
        return self._size == 0
    
    def push(self,e):
        """_push an element to the list_

        Args:
            e (_type_): _a new element to the stack _
        """
        self.head = self._node(e,self.head)
        self._size += 1
    def top(self):
        """return the top of the stack """
        if self.is_empty():
            raise Empty('stack is empty')
        return self.head._element

    def pop(self):
        """return the top of the element and remove it from the stack"""
        if self.is_empty():
            raise Empty('stack is empty')
        toreturn = self.head._element
        self.head = self.head._next
        self._size-=1
        return toreturn 
    

#test some functionalities

new = linkedlist()

new.push(2)  #push 2 in the stack
new.push(5) #push 5 in the stack
new.push(-3) #push 5 in the stack
print(new.is_empty()) # test if the stack is empty
print(new.top())  # get the top element of the stack
print(len(new)) #should return 3
print(new.pop()) #should return -3
print(new.pop()) #should return 5
print(new.pop()) #should return 2
print(len(new)) #should return 3
