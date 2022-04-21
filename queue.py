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
        
        
