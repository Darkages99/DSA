length = 5

# pointer list acts like "next" pointers
pointer = [(i + 1) for i in range(length)]

# link stores actual values
link = [None] * length

# last free node points to -1 (end of free list)
pointer[-1] = -1

# start = head of active sorted list
start = -1

# heap = head of free list (free memory list)
heap = 0


def add(item):
    global start, heap

    # If no free space available
    if heap == -1:
        print("list full")
        return False

    # Case 1: List is empty
    if start == -1:
        temp = heap

        link[heap] = item              # store item in free node
        heap = pointer[heap]           # move heap to next free location

        pointer[temp] = start          # point new node to old start (-1)
        start = temp                  # new node becomes start

    # Case 2: Insert at head (larger than current head)
    elif item > link[start]:
        temp = heap

        link[heap] = item
        heap = pointer[heap]

        pointer[temp] = start
        start = temp

    # Case 3: Insert in middle or end
    else:
        temp_start = start
        placed = False
        prev_temp = None

        while not placed and temp_start != -1:

            # Move forward while current value is greater than item
            if link[temp_start] > item:
                prev_temp = temp_start
                temp_start = pointer[temp_start]

            # Insert before first smaller/equal element
            else:
                link[heap] = item
                temp_heap = heap
                heap = pointer[heap]

                pointer[temp_heap] = pointer[prev_temp]
                pointer[prev_temp] = temp_heap

                placed = True

        # If reached end, insert at tail
        if not placed:
            link[heap] = item
            temp_heap = heap
            heap = pointer[heap]

            pointer[temp_heap] = pointer[prev_temp]
            pointer[prev_temp] = temp_heap

            placed = True


def delete(item):
    global start, heap

    index = search(item)

    # If item not found
    if index == -1:
        print("cannot delete element not present in list")

    else:

        # Case 1: Deleting head
        if index == start:
            temp_start = start
            ret_val = link[index]

            start = pointer[temp_start]   # move start forward

            pointer[temp_start] = heap    # return node to free list
            heap = temp_start

            link[temp_start] = None

            return ret_val

        # Case 2: Deleting middle or tail
        else:
            prev_pointer = None
            ret_val = link[index]
            temp_start = start

            # Find node just before index
            while temp_start != -1 and pointer[temp_start] != index:
                prev_pointer = temp_start
                temp_start = pointer[temp_start]

                if pointer[temp_start] == index:
                    break

            prev_pointer = temp_start

            # Bypass the node being deleted
            pointer[prev_pointer] = pointer[index]

            # Return node to free list
            link[index] = None
            pointer[index] = heap
            heap = index

            return ret_val


def search(item):
    temp = start

    while temp != -1:
        if link[temp] == item:
            return temp
        temp = pointer[temp]

    return -1


def display():
    temp = start

    while temp != -1:
        print(link[temp])
        temp = pointer[temp]

#TESTS

print("TEST 1: Basic Inserts")

add(5)
add(9)
add(7)
add(8)
add(6)

display()
print("start =", start)
print("heap =", heap)
print("link =", link)
print("pointer =", pointer)

print("\nTEST 2: Delete Head (9)")
delete(9)
display()
print("heap =", heap)

print("\nTEST 3: Delete Middle (7)")
delete(7)
display()
print("heap =", heap)

print("\nTEST 4: Delete Tail (5)")
delete(5)
display()
print("heap =", heap)

print("\nTEST 5: Delete Non-Existent (100)")
delete(100)
display()

print("\nTEST 6: Reinsert Freed Values")

add(10)
add(4)
add(7)

display()
print("heap =", heap)

print("\nTEST 7: Insert When Full")
add(99)
                         
                         
               
