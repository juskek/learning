





# 1. Primitive Variables
- contains value 
- stored in stack
## 1.1. Boolean
## 1.2. Character
## 1.3. Floating-point
## 1.4. Fixed-point
## 1.5. Integer
## 1.6. Reference
## 1.7. Enumerated
## 1.8. Date-Time
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
## 4.1. Linear Structure
- Elements form a sequence
### 4.1.1. Arrays
#### 4.1.1.1. Overview
- Sequence of values
- Ordered
- Indexed (Random Access)
- Unique Index/Key
- Non-unique values
- Fixed Size

#### 4.1.1.2. Storage
- Contiguous
- Fixed size upon declaration
#### 4.1.1.3. Complexity
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

### 4.1.2. Linked List
- Sequence of nodes
  - Head: Points to first node
  - Node: Key + Next Pointer
  - Tail: Last node, pointer to null

#### 4.1.2.1. Overview
#### 4.1.2.2. Storage
- Non-contiguous
- Dynamic size 

#### 4.1.2.3. Complexity
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

### 4.1.3. Stack
- LIFO
- Applications:
  - Shunting-yard algorithm
  - Recursive function calls
- Operations:
  - Push
  - Pop
  - Peek
### 4.1.4. Queue
- FIFO
- Operations:
  - Enqueue
  - Dequeue
- Applications
  - Multithreading
  - Priority Queues

## 4.2. Random Structures
- Elements are randomly stored
### 4.2.1. Set
- Unordered/unindexed
- Elements immutable?
- 
### 4.2.2. Dictionaries/Hash Tables
#### 4.2.2.1. Overview
- Array of key-value pairs
- Unordered

#### 4.2.2.2. Types
- Hash Map: implemented with dicts,
- Hash Set: implemented with set, no duplicates allowed
#### 4.2.2.3. Complexity
##### Space
- O(n)
##### Time
- No collisions
  - Insert
    - Best: O(1)
  - Search/Remove
    - Best: O(1)

- Chaining
  - Insert
    - Best: O(1)
  - Search/Remove
    - Best: O(1)
    - Worst: O(n)
    - Expected: O(n/k)
- Linear Probing
  - Insert
    - Best: O(1)
    - Worst: O(n)
    - Expected:
  - Search/Remove
    - Best: O(1)
    - Worst: O(n)
    - Expected:
- Height-balanced BST
  - Insert
    - Best: O(1)
    - Worst: O(log n)
    - Expected:
  - Search/Remove
    - Best: O(1)
    - Worst: O(log n)
    - Expected:
#### 4.2.2.4. Working Principle
- Insertion
  1. Key passed to hash function
  2. Hash function generates bucket/hashcode
  3. No duplicate, key directly addressed to hashcode
- Search
  1. Key passed to hash function and hashcode generated
  2. Search for value at hashcode 

##### Generating Hash
- Distribution to buckets should be uniform
- Tradeoff between no. of buckets and capacity of a bucket
- No. of buckets, N
  - should be on same order as elements, n
  - Load factor: n/N < 0.8, else rehash with 2N
    - Open Addressing 
  - should be a prime number to reduce collisions 


##### 4.2.2.4.1. Resolving Collisions
- Chaining
  - Hashcode points to linked list 
- Linear Probing
- Open Addressing
  - Probing of alternative unoccupied indexes with a specific sequence
- Height-balanced Binary Search Tree
  - Preferred to chaining when too many keys in a bucket
- Applications:
  - Database Keys
  - Associate Arrays
  - Used to implement sets

#### 4.2.2.5. Memory Location
- Built off arrays
### 4.2.3. Tuple
- Ordered/indexed
- Duplicates allowed
- Sets of elements immutable

## 4.3. Hierarchical
### 4.3.1. Trees
- Each node has a key (value) and three pointers (parent, left, right)
- Applications:
  - Binary Search Tree
  - B Tree
  - Treap
  - Red-Black 
  - Splay 
  - AVL
  - N-ary

### 4.3.2. Heaps
- Tree with sorting based on parent