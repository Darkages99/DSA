class Link:
     def __init__(self, value, pointer=-1):
          self.pointer = pointer   # stores index of next node
          self.value = value       # stores actual data

     def __str__(self):
          return f"pointer:{self.pointer}, value:{self.value}"


class List:
     def __init__(self):
          self.list = []           # physical storage (array of Link objects)
          self.heap = []           # stores free indexes for reuse
          self.start = -1          # index of first node


     def add(self, value):
          new_link = Link(value)

          # Adding first item
          if self.start == -1:
               self.list.append(new_link)
               self.start = 0

          # Adding new greatest item (becomes new head)
          elif value > self.list[self.start].value:
               new_link.pointer = self.start

               if len(self.heap) == 0:
                    index = len(self.list)
                    self.list.append(new_link)
                    self.start = index
               else:
                    index = self.heap[0]
                    self.list[index] = new_link
                    self.start = index
                    self.heap.pop(0)

          # Insert somewhere in middle or end
          else:
               temp = self.start
               prev_ptr = None

               # Traverse until correct position found
               while temp != -1 and value < self.list[temp].value:
                    prev_ptr = temp
                    temp = self.list[temp].pointer

               if len(self.heap) == 0:
                    index = len(self.list)
                    new_link.pointer = self.list[prev_ptr].pointer
                    self.list[prev_ptr].pointer = index
                    self.list.append(new_link)

               else:
                    index = self.heap[0]
                    new_link.pointer = self.list[prev_ptr].pointer
                    self.list[prev_ptr].pointer = index
                    self.list[index] = new_link
                    self.heap.pop(0)


     def delete(self, value):
          temp_ptr = self.start
          prev_ptr = None

          # If deleting head
          if self.list[self.start].value == value:

               # Only one element
               if self.list[self.start].pointer == -1:
                    self.list = []
                    self.start = -1
                    return True

               # More than one element
               else:
                    self.heap.append(self.start)
                    self.list[self.start].value = None
                    self.start = self.list[self.start].pointer
                    return True

          # Deleting non-head node
          else:
               while temp_ptr != -1 and value != self.list[temp_ptr].value:
                    prev_ptr = temp_ptr
                    temp_ptr = self.list[temp_ptr].pointer

               if temp_ptr == -1:
                    print("value not found")
                    return False

               self.list[prev_ptr].pointer = self.list[temp_ptr].pointer
               self.list[temp_ptr].value = None
               self.heap.append(temp_ptr)
               return True


     def display(self):
          # Empty list check
          if self.start == -1:
               print("list empty")
               return False

          # Traverse and print values
          else:
               temp = self.start
               while temp != -1:
                    if self.list[temp].value != None:
                         print(self.list[temp].value)
                    temp = self.list[temp].pointer
               return True