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

#To Do: Finish BST remove method

    def highest(self,node):
        return self._highest(node)
        
    def _highest(self,curr):
        if curr.right != None:
            return self.right.highest(curr.right)
        else:
            return curr.item
    
    def lowest(self,node):
        return self._lowest(node)

    def _lowest(self,curr):
        if curr.left != None:
            return self._lowest(curr.left)
        else:
            return curr.item

    def delete(self,value):
        return self._delete(self.root,value)

    def _delete(self,curr,value):
        if value == curr.item:
            if curr.left != None:
                curr.item = self.highest(curr.left)
                self._delete(curr.left)
            elif curr.right != None:
                curr.item = self.lowest(curr.right)
                self._delete(curr.right,value)
            else:
                return None
        else:
            if value < curr.item and curr.left != None:
                curr.left = self._delete(curr.left,value)
            if value > curr.item and curr.right != None:
                curr.right = self._delete(curr.right,value)
            return curr.item

