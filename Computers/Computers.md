- [1. Random Access Memory](#1-random-access-memory)
  - [1.1. Stack Memory](#11-stack-memory)
  - [1.2. Heap Memory](#12-heap-memory)
  - [1.3. Address Binding](#13-address-binding)
  - [1.4. Memory Leak](#14-memory-leak)
- [2. Central Processing Unit](#2-central-processing-unit)
  - [2.1. Control Unit (CU)](#21-control-unit-cu)
    - [2.1.1. (Current) Instruction Register (CIR/IR)](#211-current-instruction-register-cirir)
    - [2.1.2. Memory Address Register (MAR)](#212-memory-address-register-mar)
    - [2.1.3. Program Counter/Instruction Pointer (PC/IP)](#213-program-counterinstruction-pointer-pcip)
  - [2.2. Arithmetic Logic Unit (ALU)](#22-arithmetic-logic-unit-alu)
- [3. Machine/Instruction Cycle](#3-machineinstruction-cycle)
- [4. Drive](#4-drive)
  - [4.1. Volume (Logical Drive)](#41-volume-logical-drive)
  - [4.2. File System](#42-file-system)
- [5. Operating Systems](#5-operating-systems)
  - [5.1. Multitasking](#51-multitasking)
    - [5.1.1. Daemon (Dump & Examine Monitor)](#511-daemon-dump--examine-monitor)

# 1. Random Access Memory
- Short term storage
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
## 1.3. Address Binding
- Association of data/instructions to physical memory location
- Compile Time: Before program is loaded 
- Load Time: When program is loading
- Execution Time: During runtime
## 1.4. Memory Leak
- Failure to release unused memory


# 2. Central Processing Unit
- Retrieves and executes instructions
- Made from logic gates
- Clock generator:
  - Syncs state of CPU
  - Speed: number of instructions per second
- Components:
## 2.1. Control Unit (CU)
### 2.1.1. (Current) Instruction Register (CIR/IR)
- Stores instruction 
### 2.1.2. Memory Address Register (MAR)
- Stores address where instruction was copied from/result will be copied to
### 2.1.3. Program Counter/Instruction Pointer (PC/IP)
- Starts at 0 and increments after instruction execution to point to address of next instruction
## 2.2. Arithmetic Logic Unit (ALU)

# 3. Machine/Instruction Cycle
1. Fetch
   - Software is a set of instructions in RAM
   - PC starts at zero and points to first MAR
   - CU copies instruction in MAR to IR
2. Decode
   - CU parses bits into 
     - Optcode: Bits containing instruction (add, subtract etc.)
     - Operand: Data/memory location to execute instruction on
3. Execute
   - CU sends electrical signals to relevant components (e.g., ALU)
   - ALU stores result in MAR of RAM
- Cycle repeated from startup to shutdown
- Multiple cores = multiple cycles

# 4. Drive
- Long Term Storage
## 4.1. Volume (Logical Drive)
- Single accessible storage 
- Single file system
- 
## 4.2. File System
- How data is stored and retrieved
- If not data would be on large body with no way to tell where each starts and ends
- Each group of data is a file

# 5. Operating Systems
## 5.1. Multitasking
### 5.1.1. Daemon (Dump & Examine Monitor)  
- Continuously running background process 
- Convention: end process with letter d, e.g. `syslogd`