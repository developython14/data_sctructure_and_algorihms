""".implemenation of queue using python and linkedlist concept:"""


from pickle import NONE
from re import A


class queue : 
    """public class represent a queue structure"""

    class node : 
        """_a base node to use it to implement a linkedlist and queue_
        """
        def __init__(self,element,next):
            """_a public constructor to design a Node_
            """
            self.element = None
            self.next = None
    

    def __init__(self):
            """_a public constructor to design a queue_
            """
            self.head = None
            self.tail = None
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

    def top(self):
        """_public funtion that return the top of stack or the next elemenent in ordering_
        """
        if self.is_empty():
            raise Empty('stack is empty')
        return self.head.element



        return
    
    def push(self,e):
        """_public function that append new element in the stack_

        Args:
            e (_object_): _element that we will put it in the stack_
        """
        a =  self.node(e,None)
        if self.is_empty():
            print('rah tverisfiel')
            self.head = a
        else:
            self.tail.next = a
        self.tail = a
        self._size +=1


    def pop(self):
        """_public function that return the top element of the stack and remove it_
        """
        if self.is_empty():
            raise Empty('stack is empty')
        
        answer = self.head.element
        self.head = self.head.next
        self._size -=1
        if self.is_empty():
           self.tail = None
        return  answer






