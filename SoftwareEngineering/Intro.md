- [1. Development Process](#1-development-process)
  - [1.1. Pen & Paper](#11-pen--paper)
    - [1.1.1. Listen](#111-listen)
    - [1.1.2. Example](#112-example)
    - [1.1.3. Brute Force](#113-brute-force)
    - [1.1.4. Optimise](#114-optimise)
    - [1.1.5. Walk Through](#115-walk-through)
  - [1.2. Keyboard & Computer](#12-keyboard--computer)
    - [1.2.1. Code](#121-code)
    - [1.2.2. Test](#122-test)
- [2. Development Tips](#2-development-tips)
  - [2.1. Do-It-Yourself](#21-do-it-yourself)
  - [2.2. Space/Time Tradeoff](#22-spacetime-tradeoff)
  - [Just use a hash table](#just-use-a-hash-table)

## 1. Development Process
### 1.1. Pen & Paper
#### 1.1.1. Listen
- So the objective is to...
#### 1.1.2. Example
- For example, if I have...
#### 1.1.3. Brute Force
- So first I need to...
#### 1.1.4. Optimise
- I can see that... has the largest time complexity because...
- I could...
- BUD:
  - Bottlenecks: operations which take more time
  - Unnecessary work: e.g., break loop if iterations after invalid
  - Duplicated work: e.g., instead of computing value repeatedly, use hash table (recursive fib)
#### 1.1.5. Walk Through
- So when the function is called, it takes in... 
- then...
- and returns...
### 1.2. Keyboard & Computer
#### 1.2.1. Code
- Comment before coding
#### 1.2.2. Test
- Test multiple scenarios


## 2. Development Tips

### 2.1. Do-It-Yourself
Identifying specific cases which can be programmed for O(1) time complexity.

### 2.2. Space/Time Tradeoff
Higher memory usage, faster run time and vice versa (e.g. hashtables).

### Just use a hash table
- Fast:
  - Searching
  - Storing
  - Deleting
- Note:
  - Ineffective for small no. of entries