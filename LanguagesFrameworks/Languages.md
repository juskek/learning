# Primitive Variables
- contains value 
- stored in stack
## int
## byte
## short
## long
## float
## double
## boolean
## char
## string

# Pointer Variables
- holds memory address of another variable
- can be reassigned
- 

# Reference Variables
- holds memory address of another variable
- cannot be reassigned 
- stored in heap

# Types of Data Structures

## Main Types
### List/Array
- Ordered/indexed
- Duplicates allowed
### Set
- Unordered/unindexed
- Elements immutable?
- 
### Dictionary
- Unordered/unindexed
- Key Value Pair
- Built off arrays
- O(1) retrieval 
### Tuple
- Ordered/indexed
- Duplicates allowed
- Sets of elements immutable

# Types of Languages

## Design Approach (How is the program designed?)
### Procedural
- Execute line by line
### Functional
- Functions encapsulate instructions
- Contains procedural design
### OOP
- Encapsulation, Abstraction, Inheritance/Delegation, Polymorphism
- Contains procedural and functional design too

## Time of Conversion (When is it converted?)
### Compile Type
- Converted directly into machine code on build 
- Processor runs machine code as a whole
- e.g., recipe in greek, translated to english before cooking
- Adv:
  - Faster
### Interpreted Type
- Slower (improved by JIT compilation)
- Converted into machine code line by line  
- e.g., recipe in greek, greek friend instructs you step by step in english
- Adv:
  - Slower

## Instruction Approach (How is the compiler instructed?)
- Can have both types
### Imperative
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

### Declarative
- Instruct compiler of final output
- e.g., getting odd numbers in LINQ
  ```
  List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
  
  var results = collection.Where( num => num % 2 != 0);
  ```
  - Instruction: Create result collection containing all numbers which are odd


## Memory Management

### Manual
### Automatic Garbage Collection

### Deterministic
### Automatic Reference Counting


## Statements vs Expressions
- Statements do something (e.g., `if, for, while, x=1, y=x+1, return`), they are complete units of execution. 
- Expressions evaluate TO a value (e.g., `x + 2, y`)


## Static Member/Method
- Belongs to class
- Uses less memory
- Compile time binding
## Non-static Member/Method
- Belongs to instance of class
- Uses more memory
- Runtime binding