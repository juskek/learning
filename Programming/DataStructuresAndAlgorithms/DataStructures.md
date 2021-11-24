





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
#### Overview
- Sequence of values
- Ordered
- Indexed (Random Access)
- Unique Index/Key
- Non-unique values
- Fixed Size

#### Storage
- Contiguous
- Fixed size upon declaration
#### Complexity
- Access: O(1)

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

#### Overview
#### Storage
- Non-contiguous
- Dynamic size 

#### Complexity
- Access: O(n)

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
### 4.1.3. Dictionaries/Hash Tables
#### Overview
- Array of key-value pairs
- Unordered

#### Types
- Hash Map: implemented with dicts,
- Hash Set: implemented with set, no duplicates allowed
#### Complexity
- O(1) retrieval (no collisions)
- O(n/k) retrieval (chaining) 
- O(n) retrieval (linear probing)

#### Principle
- Insertion
  1. Key passed to hash function
  2. Hash function generates bucket/hashcode
  3. Key assigned to hashcode
- Retrieval

##### Resolving Collisions
- Chaining
- Linear Probing
- Open Addressing
- Process:
  1. Key is passed to hash function
     - OUT: Hash code
  2. Store/Retrieve value in array at hash code index
     - Direct Addressing: No duplicate hash codes
  3. Resolve collisions
     - Chaining: Array of linked lists with original key 
     - Open Addressing: Probing of alternative unoccupied indexes with a specific sequence
- Built off arrays
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