#create node
class Node:
      
      def __init__(self,isi):
            self._isi = isi
            self._next = None
       
# create head
class ll:
      def __init__(self):
            self._head = None
            
            
      def add1(self,isi):
            a = Node(isi)
            if self._head == None:
                  self._head = a
                  
            else:
                  a._next = self._head 
                  self._head = a
                  
                  
      def isinya(self):
            a = self._head
            
            while a != None:
                  print(a._isi)
                  a = a._next
                  
                  
myll = ll()
myll.add1("a")
myll.add1("b")
myll.add1("c")
myll.isinya()