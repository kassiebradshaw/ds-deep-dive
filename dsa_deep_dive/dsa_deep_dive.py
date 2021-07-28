# Problem domain
# Given a Binary Tree where the value of each node is a LL,  the value of each LL is a list.
# Write a function that will return some information in a tuple format.
# Return: sum of all values, largest value, smallest value, and furthest removed from zero

# algorithm return_junk(BT):

# val_list = [] <-- empty list to hold all inner-list values
# max_val = 
# min_val =


# BT

# current = BT.root <-- node is a LL <-- LL has multiple is a list

# current.value --> LinkedList = head -> [list1] -> [list2] -> [list3] -> None

#list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]

#first_list = current.value.head.value --> list1

# print(max(first_list)) <-- returns largest value
# print(min(first_list)) <-- returns smallest value

# --------------------------------------------------------------

def function(BinaryTree):
  max_val = BT.root.value.head.value[0]
  min_val = BT.root.value.head.value[0]
  sum = 0
  abs_val = 0

  queue = Queue()
  queue.enqueue(BinaryTree.root)
  while queue.peek():
    front = queue.dequeue()
    if front.left:
      queue.enqueue(front.left)
    if front.right:
      queue.enqueue(front.right)
    # now start looking at the value of the front
    # start looking at the linked list portion of our value
    # iterate through the linked list and grab every list value
    # then iterate through the list
    # --------Algorithm for linked list -----
    # front.value points to a linked list

    current = front.value.head

    while current: #current.value <-- an array
      for number in current.value:
        if number > max_val:
          max_val = number
        if number < min_val:
          min_val = number
        if abs(number) > abs_val:
          abs_val = number
        sum += number
      current = current.next

  return (max_val, min_val, sum, abs_val)
