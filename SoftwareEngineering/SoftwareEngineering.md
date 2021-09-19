- [1. Prototyping Process](#1-prototyping-process)
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

## 1. Prototyping Process
### 1.1. Write before you 
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
### 1.2. Type
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


# Versioning
## Major.Minor.Revision+Build
- MAJOR is a major release (usually many new features or changes to the UI or underlying OS)
- MINOR is a minor release (perhaps some new features) on a previous major release
- REVISION is usually a fix for a previous minor release (no new functionality)
- BUILDNUMBER is incremented for each latest build of a revision.

# DevOps


# Testing
## Tenets
1. Understanding big picture and priorities
2. Understanding interactions of components within big picture
3. Structured approach (mindmap)
4. Practicality (reasonable testing plans)

## Process
1. Who will use it and why?
2. What are the use cases?
3. What are the bounds of use?
4. What are the stress/failure conditions?
5. How will testing be performed?
   - Manual vs Automated
   - Black Box vs WhiteBox

## Testing Types
### Manual
### Automated
#### Smoke Testing
#### Integration
#### Unit 
- Isolate
  - Test one class at a time
  - Test results should not depend on other classes or tests
    - Use `Setup` and `TearDown` features
  - Tests should be able to run offline
- AAA Rule
  - Arrange: Set up variables to enable test 
  - Act: Call method
  - Assert: Verify result
- Simplicity before complexity
  - Simplest functionalities first
  - Edge and boundary cases after
- Test across boundaries
  - e.g., one second before and after midnight, one point before and after a line
- Test entire spectrum (if possible)
  - e.g., enum tests
- Cover every code path (if possible)
- Write tests for bugs before fixing them
  - If bug is found, write tests that reveals it so that it can be quickly fixed in the future 
- Name tests clearly
- Test raised exceptions
- Avoid checking boolean conditions
  - Using `Assert.AreEqual(x,y)` will provide more information than `Assert.IsTrue(x==y)`
- Run tests while writing code
  - Better as part of build process