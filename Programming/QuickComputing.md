- Multiple processes executing over same period of time
- Each process has multiple computations
# Parallel Computing
- Computation occurs at same physical instant
## Parallel Processing

## Multiprocessing


# Concurrent Computing
- Computation does not occur at same physical instant
- Lifetime of processes overlapping
## Multithreading

## Shared Memory Access
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
## Problems
### Race Condition/Hazard (RC)
- Behaviour dependent on sequence or timing of other events

### Deadlocks (DL)
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




### Resource Starvation (RS)
- Process perpetually denied access to necessary resources
- Causes:
  - Errors in scheduling or mutual exclusion algorithm
  - Resource leaks
  - Denial of Service attack

### Solutions: Non-blocking algorithms
- Failure/suspension of any thread does not cause the same for other threads
#### Mutual Exclusion (RC)
- Prevents multiple threads from accessing a resource at the same time 
#### Ostrich Algorithm (All)
- Pretend it doesn't exist and deal with it if it happens
- Used when cost of detection/prevention is high and deadlock occurence is very rare
#### Breaking Symmetry (DL)
- Right Before Left: Granting access to
#### Non-blocking Synchronisation (DL)
- Avoid mutual exclusion

#### Serialising Tokens (DL)
- Avoid resource holding
- P request access to R before executing, or
- P only execute when R is not accessed 
  - Problems:
    - P may never execute if dependent on a popular R

#### Lock Freedom (DL)
- Grants preemption

#### Wait Freedom (DL)
- Grants preemption


#### Optimistic Concurrency Control (DL)
- Grants preemption

#### Interrupt Disabling (DL)
- Avoid circular wait

#### Partial Ordering of Resources (DL)
- Avoid circular wait