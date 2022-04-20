
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
    