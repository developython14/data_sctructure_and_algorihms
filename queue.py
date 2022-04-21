""".implemenation of queue using python and linkedlist concept:"""


class queue : 
    """public class represent a queue structure"""

    class node : 
        """_a base node to use it to implement a linkedlist and queue_
        """
        def __init__(self):
            """_a public constructor to design a Node_
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


        return
    
    def push(self,e):
        """_public function that append new element in the stack_

        Args:
            e (_object_): _element that we will put it in the stack_
        """


    def pop(self):
        """_public function that return the top element of the stack and remove it_
        """

        
