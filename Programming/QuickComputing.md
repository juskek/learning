- [1. Quick Computing](#1-quick-computing)
  - [1.1. Low-Level Concepts](#11-low-level-concepts)
    - [1.1.1. Parallel Computing](#111-parallel-computing)
    - [1.1.2. Concurrent Computing](#112-concurrent-computing)
  - [1.2. High-level Concepts](#12-high-level-concepts)
    - [1.2.1. Asynchronous Computing](#121-asynchronous-computing)
      - [1.2.1.1. Parallelism](#1211-parallelism)
      - [1.2.1.2. Concurrency](#1212-concurrency)
      - [Single Threading](#single-threading)
      - [1.2.1.3. Polling](#1213-polling)
      - [1.2.1.4. Interrupts](#1214-interrupts)
      - [Callback](#callback)
      - [Asynchronous Procedure Call](#asynchronous-procedure-call)
- [2. Problems](#2-problems)
  - [2.1. Shared Memory Access](#21-shared-memory-access)
  - [2.2. Race Condition/Hazard (RC)](#22-race-conditionhazard-rc)
  - [2.3. Deadlocks (DL)](#23-deadlocks-dl)
  - [2.4. Resource Starvation (RS)](#24-resource-starvation-rs)
  - [2.5. Solutions: Non-blocking algorithms](#25-solutions-non-blocking-algorithms)
    - [2.5.1. Mutual Exclusion/Locks (RC)](#251-mutual-exclusionlocks-rc)
      - [Characteristics](#characteristics)
        - [Access Attempt](#access-attempt)
        - [Access Mode](#access-mode)
        - [Blocked Access Reaction](#blocked-access-reaction)
      - [Algorithms](#algorithms)
        - [Dekker's](#dekkers)
        - [Peterson's](#petersons)
      - [Bakery](#bakery)
      - [Lamport](#lamport)
    - [2.5.2. Ostrich Algorithm (All)](#252-ostrich-algorithm-all)
    - [2.5.3. Breaking Symmetry (DL)](#253-breaking-symmetry-dl)
    - [2.5.4. Non-blocking Synchronisation (DL)](#254-non-blocking-synchronisation-dl)
    - [2.5.5. Serialising Tokens (DL)](#255-serialising-tokens-dl)
    - [2.5.6. Lock Freedom (DL)](#256-lock-freedom-dl)
    - [2.5.7. Wait Freedom (DL)](#257-wait-freedom-dl)
    - [2.5.8. Optimistic Concurrency Control (DL)](#258-optimistic-concurrency-control-dl)
    - [2.5.9. Interrupt Disabling (DL)](#259-interrupt-disabling-dl)
    - [2.5.10. Partial Ordering of Resources (DL)](#2510-partial-ordering-of-resources-dl)

# 1. Quick Computing
- How to get stuff done quicker
- Over same period of time, EXECUTE multiple
  - Computations/Operations
  - Processes 
    - Group of computations/operations

## 1.1. Low-Level Concepts
### 1.1.1. Parallel Computing
- Definition: Computations/operations EXECUTES at same physical instant
- Methods:
  - Parallel/Multi Processing/Tasking
    - Managing multiple processes on multiple cores

### 1.1.2. Concurrent Computing
- Definition: Computations/operations do not EXECUTE at same physical instant
  - Lifetime of their processes overlapping
- Multithreading
  - Managing multiple threads of execution on a single core
  - Task Queue: Processes in memory 
  - Thread Pool: Maintains state of multiple threads
    - Thread: Series of computations broken down into the smallest executable sequence

## 1.2. High-level Concepts
### 1.2.1. Asynchronous Computing
- Definition: EXECUTING other computations/operations while WAITING for some computation/operation to finish
  - EXECUTION may/may not happen at the same time
  - WAITING:
    - for data
    - for time delay
  - Async operation: one which allows other operations to execute before it completes

**Can be achieved through:**
#### 1.2.1.1. Parallelism
- Start other operations in next available core
#### 1.2.1.2. Concurrency
- Start other operations in next available thread
#### Single Threading
- Consider a data retrieval with operations 
  - A: async which retrieves data 
    - Execution time: 1s
    - Retrieval time varies
  - B: sync with input independent of A
    - Execution time: 1s
  - C: sync with input dependent on A
    - Execution time: 1s
- Sync:
  - Retrieval time: 2s
    A -> R -> R -> B -> C
    - Time: 5s
  - Retrieval time: 1s
    A -> R -> B -> C 
    - Time: 4s
- Async:
  - Retrieval time: 2s
    A -> B      |-> C   
     |-> R -> R |
    - Time: 4s
  - Retrieval time: 1s
    A -> B |-> C   
     |-> R |
    - Time: 3s
- Assumes retrieval of data does not require maintenance by thread

#### 1.2.1.3. Polling
- Start other operations in same thread, CHECK when async operation is done repeatedly after
  - each operation
  - an interval
- CPU needs to continuously monitor whether there is a change in the outcome
#### 1.2.1.4. Interrupts
- Start other operations in same thread, WAIT for async operation to finish
- CPU is signalled from by change in outcome

#### Callback
- Passing function into another function as an argument to invoke later/after some action
#### Asynchronous Procedure Call
- Storing async function as an object with some memory for input data
- Passing object to service which receives user inputs
- When a reply is received, the object is passed to the thread pool for execution
# 2. Problems
## 2.1. Shared Memory Access
- Threads may operate on the same memory resource
- e.g., 
```
    bool withdraw(int withdrawal)
    {
        if (balance >= withdrawal)
        {
            balance -= withdrawal;
            return true;
        } 
        return false;
    }
```

## 2.2. Race Condition/Hazard (RC)
- Behaviour dependent on sequence or timing of other events

## 2.3. Deadlocks (DL)
- Processes (P) preventing each other from continuing execution due to dependent resources (R)
- Coffman Conditions for Deadlocks to Occur:
  - Mutual Exclusion: 
    - Only one P can access one R at any time
  - Resource Holding: 
    - A P is holding >=1 R and is requesting additional R held by other Ps
  - No Premption: 
    - R can only be released voluntarily by the P holding it
  - Circular Wait:
    - For a set of waiting processes, P = {P1,...,Pn}
    - Pi is waiting for a resource held by Pi+1
- Types:
  - Multiple R:
    - e.g., 
    - P1 dependent on R1 and in possession of R2
    - P2 dependent on R2 and in possession of R1
  - Single R:
    - e.g, 
    - P1, P2, P3, P4 dependent on R




## 2.4. Resource Starvation (RS)
- Process perpetually denied access to necessary resources
- Causes:
  - Errors in scheduling or mutual exclusion algorithm
  - Resource leaks
  - Denial of Service attack

## 2.5. Solutions: Non-blocking algorithms
- Failure/suspension of any thread does not cause the same for other threads
### 2.5.1. Mutual Exclusion/Locks (RC)
- Prevents multiple threads from accessing a resource at the same time 
#### Characteristics
##### Access Attempt
- Advisory: Threads coordinate to acquire lock before accessing data
- Mandatory: Unauthorised access throws exception

- Binary semaphore
##### Access Mode
- Exclusive 
- Intend-to-exclude
- Intend-to-upgrade

##### Blocked Access Reaction
- Spinlock: Thread waits/spins until lock becomes available
  - Adv.: Avoids overhead of rescheduling for short blockages
  - Dis.: Hogs CPU for longer blockages

#### Algorithms
##### Dekker's 
- Each process uses a
  - flag: indicates whether it wants to enter the critical section
  - turn: indicates which process takes priority
##### Peterson's
- Same as Dekker's, but
  - 
#### Bakery 
- No hardware atomicity required
  - Atomicity: 
#### Lamport
- Synchronise N processors
  - in O(1) time when there is no contention
  - in O(N) time when there is contention
### 2.5.2. Ostrich Algorithm (All)
- Pretend it doesn't exist and deal with it if it happens
- Used when cost of detection/prevention is high and deadlock occurence is very rare
### 2.5.3. Breaking Symmetry (DL)
- Right Before Left: Granting access to
### 2.5.4. Non-blocking Synchronisation (DL)
- Avoid mutual exclusion

### 2.5.5. Serialising Tokens (DL)
- Avoid resource holding
- P request access to R before executing, or
- P only execute when R is not accessed 
  - Problems:
    - P may never execute if dependent on a popular R

### 2.5.6. Lock Freedom (DL)
- Grants preemption

### 2.5.7. Wait Freedom (DL)
- Grants preemption


### 2.5.8. Optimistic Concurrency Control (DL)
- Grants preemption

### 2.5.9. Interrupt Disabling (DL)
- Avoid circular wait

### 2.5.10. Partial Ordering of Resources (DL)
- Avoid circular wait