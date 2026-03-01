length=5
pointer=[(i+1) for i in range(length)]            #pointer array
link=[None]*length                                #items array
pointer[-1]=-1

heap=0    #heap pointer
start=-1  #start pointer

def push(item):
     global start,heap
     if heap!=-1:
          temp = heap

          link[heap] = item              # store item in free node
          heap = pointer[heap]           # move heap to next free location

          pointer[temp] = start          # point new node to old start 
          start = temp                  # new node becomes start
     else:
          print("Stack Full")

def pop():
     global start,heap
     if start!=-1:
          
          temp_start = start
          ret_val = link[temp_start]

          start = pointer[temp_start]   # move start forward

          pointer[temp_start] = heap    # return node to free list
          heap = temp_start

          link[temp_start] = None

          return ret_val
     else:
          print("Stack Empty")


def display():
     temp=start
     while temp!=-1:
          print(link[temp])
          temp=pointer[temp]

def search(item):
     temp=start
     found=False
     while temp !=-1 and not found:
          if link[temp]==item:
               print(f"found at index {temp}")
               found=True
               return True
          temp=pointer[temp]
     print("not found")
     return False

#TESTS

print("INITIAL STATE")
display()
print("heap:", heap, "start:", start)
print()

print("PUSHING 5")
push(5)
display()
print("heap:", heap, "start:", start)
print()

print("PUSHING 9")
push(9)
display()
print("heap:", heap, "start:", start)
print()

print("PUSHING 7")
push(7)
display()
print("heap:", heap, "start:", start)
print()

print("SEARCH TESTS")
search(9)      # should find
search(100)    # should not find
print()

print("POP TEST")
print("popped:", pop())
display()
print("heap:", heap, "start:", start)
print()

print("FILLING STACK COMPLETELY")
push(1)
push(2)
push(3)   # should fill memory
display()
print("heap:", heap, "start:", start)
print()

print("TRYING TO PUSH WHEN FULL")
push(99)  # should print stack full
print()

print("EMPTYING STACK")
print("popped:", pop())
print("popped:", pop())
print("popped:", pop())
print("popped:", pop())
print("popped:", pop())   # eventually empty
display()
print("heap:", heap, "start:", start)
print()

print("TRYING TO POP WHEN EMPTY")
print("popped:", pop())   # should print stack empty





