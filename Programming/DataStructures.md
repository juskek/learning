





# 1. Primitive Variables
- contains value 
- stored in stack
## Boolean
## Character
## Floating-point
## Fixed-point
## Integer
## Reference
## Enumerated
## Date-Time
##

# 2. Pointer Variables
- holds memory address of another variable
- can be reassigned
- 

# 3. Reference Variables
- holds memory address of another variable
- cannot be reassigned 
- stored in heap

# 4. Data Structures
- Storage, organisation and management of primitive variables for efficient access
## Linear Structure
- Elements form a sequence
### 4.1.1. Arrays
- Sequence of values
- Ordered
- Indexed (Random Access)
- Unique Index/Key
- Non-unique values
- Fixed Size
- Operations:
  - Traverse
  - Search
  - Update
  - Insertion/Deletion
    - Requires recreating entire array
- Building block for:
  - Array Lists
  - Heaps
  - Hash Tables
  - Vectors
  - Matrices
- Applications:
  - Insertion sort
  - Quick sort
  - Bubble sort
  - Merge sort

### Linked List
- Sequence of nodes
  - Head: Points to first node
  - Node: Key + Next Pointer
  - Tail: Last node, pointer to null
- Ordered
- Unindexed Sequential Access
- Non-unique 
- Operations:
  - Search
  - Insert 
  - Delete
- Types
  - Singly: Forward traversal
  - Doubly: Forward and reverse traversal
    - Prev + Key + Next Pointer
  - Circular:
    - Head and tail joined 
- Applications:
  - Alt+Tab
  - Symbol table management in compiler design

### Stack
- LIFO
- Applications:
  - Shunting-yard algorithm
  - Recursive function calls
- Operations:
  - Push
  - Pop
  - Peek
### Queue
- FIFO
- Operations:
  - Enqueue
  - Dequeue
- Applications
  - Multithreading
  - Priority Queues

## Random Structures
- Elements are randomly stored
### 4.1.2. Set
- Unordered/unindexed
- Elements immutable?
- 
### 4.1.3. Dictionary/Hash Tables
- Array of key-value pairs
- Unordered
- Process:
  1. Key is passed to hash function
     - h(k) = k % m
       - Hash function, h()
       - Key, k
       - Size of hash table, m 
       - Hash code/value, h(k): Array index at which the value will be stored
     - OUT: Hash code
  2. Store/Retrieve value in array at hash code index
     - Direct Addressing: No duplicate hash codes
  3. Resolve collisions
     - Chaining: Array of linked lists with original key 
     - Open Addressing: Probing of alternative unoccupied indexes with a specific sequence
- Built off arrays
- O(1) retrieval 
- Applications:
  - Database Keys
  - Associate Arrays
  - Used to implement sets
### 4.1.4. Tuple
- Ordered/indexed
- Duplicates allowed
- Sets of elements immutable

## Hierarchical
### Trees
- Each node has a key (value) and three pointers (parent, left, right)
- Applications:
  - Binary Search Tree
  - B Tree
  - Treap
  - Red-Black 
  - Splay 
  - AVL
  - N-ary

### Heaps
- Tree with sorting based on parent