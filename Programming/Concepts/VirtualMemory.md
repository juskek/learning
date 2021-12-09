## 1.1. Stack Memory
- Purpose:
- Fast, temporary data storage for primitives
- e.g., int, bool
- Characteristics:
  - FILO
  - Static allocation (stack size fixed after allocation)
  - Data created on the stack can be used without pointers
  - Maximum size determined when program starts
  - Automatic deallocation after variables go out of scope
- Application:
  - Each function/thread has its own stack
  - Stores local data, return addresses, used for parameter passing.
  - You would use the stack if you know exactly how much data you need to allocate before compile time and it is not too big.
- Overheads:
  - Stack pointer: indicates where current stack memory location is
    - Allocation/deallocation by incrementing/decremeting pointer
- Problems:
  - Can have a stack overflow when too much of the stack is used (mostly from infinite or too deep recursion, very large allocations).

## 1.2. Heap Memory
- Purpose:
  - Slow, persisting data storage for complex data
  - e.g., Classes, Objects, Arrays, Indexers, Interfaces
- Characteristics:
  - Dynamic allocation (heap size can change after allocation)
  - Variables which are no longer used are marked for garbage collection
- Applications:
  - Each program has its own heap
  - Used on demand to allocate a block of data for use by program
  - You would use the heap if you don't know exactly how much data you will need at run time or if you need to allocate a lot of data
- Overheads:
  - Record Table
    - Tracks allocated/deallocated memory
  - Defragmentation
    - Moving allocated memory around
    - Finding sufficiently big contiguous memory segments
  - Garbage collection
- Problems:
  - Can have fragmentation when there are a lot of allocations and deallocations.
  - Can have allocation failures if too big of a buffer is requested to be allocated.
  - Responsible for memory leaks.



#### 1.3. Address Binding
- Association of data/instructions to physical memory location
- Compile Time: Before program is loaded 
- Load Time: When program is loading
- Execution Time: During runtime
#### 1.4. Memory Leak
- Failure to release unused memory
