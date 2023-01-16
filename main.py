class Bin:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None

  def insert(self,item):
     # insert item at root if tree is empty
    if self.data is None:
      self.data=item
    else:
      # if item is less than current node, 
        # insert item into left subtree
      if item < self.data:
        if self.left is None:
          self.left=Bin(item)
        else:
          self.left.insert(item)
      elif item > self.data:
         # else, insert item into right subtree
        if self.right is None:
          self.right=Bin(item)
        else:
          self.right.insert(item)

  def inorder(self):
    if self.left:
      self.left.inorder()
    print(self.data)
    if self.right:
      self.right.inorder()

  def search(self,element):
    if element < self.data:
      if self.left is None:
        return False
      else:
        return self.left.search(element)
    elif element > self.data:
      if self.right is None:
        return False
      else:
        return self.right.search(element)
    else:
      return True

T = Bin(15)
T.insert(12)
T.insert(8)
T.insert(6)
T.insert(2)
T.insert(7)
T.insert(9)
T.insert(10)

T.inorder()

print(T.search(8))
