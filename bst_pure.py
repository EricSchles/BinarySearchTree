class Node:
    def __init__(self,item,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return repr(self.item)


class BinarySearchTree:
    def __init__(self,root=None,left=None,right=None):
        self.root = Node(root)
        self.root.left = left
        self.root.right = right

    def insert(self,val):
        if self.root.item == None:
            self.root = Node(root)
        else:
            self._insert(self.root,val)

    def _insert(self,curr,val):
        if curr.item > val and curr.left == None:
            node = Node(val)
            curr.left = node
        elif curr.item < val and curr.right == None:
            node = Node(val)
            curr.right = node
        else:
            if curr.item < val:
                self._insert(curr.right,val)
            else:
                self._insert(curr.left,val)

    def contains(self,val):
        if self.root.item == val:
            return True
        else:
            return self._contains(self.root,val)
    
    def _contains(self,curr,val):
        if curr.item == val:
            return True
        if val < curr.item:
            if curr.left != None:
                return self._contains(curr.left,val)
            else:
                return False
        elif val > curr.item:
            if curr.right != None:
                return self._contains(curr.right,val)
            else:
                return False
        else:
            return False

    def pretty_print(self):
        if self.root.item == None:
            print None
        else:
            self._pretty_print(self.root)
    
    def _pretty_print(self,curr):
        if curr.item == None:
            print None
        else:
            if curr.left != None:
                self._pretty_print(curr.left)
            print str(curr.item)
            if curr.right != None:
                self._pretty_print(curr.right)

    # def remove(self,val):
    #     if self.contains(val):
    #         if self.root.item == val:
    #             return True
    #         else:
    #             return self._remove(self.root,val)
    #     else:
    #         raise Exception("Value you not in tree")
    
    # def _remove(self,curr,val):
    #     if curr.item == val:
    #think about how to do this...        
                
            
