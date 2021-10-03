# 1. Primitive Variables
- contains value 
- stored in stack
## 1.1. int
## 1.2. byte
## 1.3. short
## 1.4. long
## 1.5. float
## 1.6. double
## 1.7. boolean
## 1.8. char
## 1.9. string

# 2. Pointer Variables
- holds memory address of another variable
- can be reassigned
- 

# 3. Reference Variables
- holds memory address of another variable
- cannot be reassigned 
- stored in heap

# 4. Types of Data Structures

## 4.1. Main Types
### 4.1.1. List/Array
- Ordered/indexed
- Duplicates allowed
### 4.1.2. Set
- Unordered/unindexed
- Elements immutable?
- 
### 4.1.3. Dictionary
- Unordered/unindexed
- Key Value Pair
- Built off arrays
- O(1) retrieval 
### 4.1.4. Tuple
- Ordered/indexed
- Duplicates allowed
- Sets of elements immutable

# 5. Types of Languages

## 5.1. Design Approach (How is the program designed?)
### 5.1.1. Procedural
- Execute line by line
### 5.1.2. Functional
- Functions encapsulate instructions
- Contains procedural design
### 5.1.3. OOP
- Encapsulation, Abstraction, Inheritance/Delegation, Polymorphism
- Contains procedural and functional design too

## 5.2. Time of Conversion (When is it converted?)
### 5.2.1. Compile Type
- Converted directly into machine code on build 
- Processor runs machine code as a whole
- e.g., recipe in greek, translated to english before cooking
- Adv:
  - Faster
### 5.2.2. Interpreted Type
- Slower (improved by JIT compilation)
- Converted into machine code line by line  
- e.g., recipe in greek, greek friend instructs you step by step in english
- Adv:
  - Slower

## 5.3. Instruction Approach (How is the compiler instructed?)
- Can have both types
### 5.3.1. Imperative
- Instruct compiler step by step
- e.g., getting odd numbers in C#
  ```
  List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
  
  List<int> results = new List<int>();
  foreach(var num in numbers)
  {
      if (num % 2 != 0)
            results.Add(num);
  }
  ```
  - Instruction:
    1. Create result collection 
    2. Step through each num in numbers
    3. If odd, add to result

### 5.3.2. Declarative
- Instruct compiler of final output
- e.g., getting odd numbers in LINQ
  ```
  List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
  
  var results = collection.Where( num => num % 2 != 0);
  ```
  - Instruction: Create result collection containing all numbers which are odd

## 5.4. Type Checking (When are data types checked?)
### 5.4.1. Static
- Compile time checking
### 5.4.2. Dynamic
- Runtime checking
## 5.5. Memory Management

### 5.5.1. Manual
- Explicit allocation and freeing of memory
- e.g,, C malloc, free
### 5.5.2. Automatic Garbage Collection

### 5.5.3. Deterministic
### 5.5.4. Automatic Reference Counting

## 

# 6. ???
## 6.1. Statements vs Expressions
- Statements do something (e.g., `if, for, while, x=1, y=x+1, return`), they are complete units of execution. 
- Expressions evaluate TO a value (e.g., `x + 2, y`)


## 6.2. Static Member/Method
- Belongs to class
- Uses less memory
- Compile time binding
## 6.3. Non-static Member/Method
- Belongs to instance of class
- Uses more memory
- Runtime binding


Language Compilation Process
1. Translation: Translate compiled language to assembly language
2. Assemble: Convert assembly language to machine code 