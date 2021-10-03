- [1. Types of Languages](#1-types-of-languages)
  - [1.1. Design Approach (How is the program designed?)](#11-design-approach-how-is-the-program-designed)
    - [1.1.1. Procedural](#111-procedural)
    - [1.1.2. Functional](#112-functional)
    - [1.1.3. OOP](#113-oop)
  - [1.2. Time of Conversion (When is it converted?)](#12-time-of-conversion-when-is-it-converted)
    - [1.2.1. Compile Type](#121-compile-type)
    - [1.2.2. Interpreted Type](#122-interpreted-type)
  - [1.3. Instruction Approach (How is the compiler instructed?)](#13-instruction-approach-how-is-the-compiler-instructed)
    - [1.3.1. Imperative](#131-imperative)
    - [1.3.2. Declarative](#132-declarative)
  - [1.4. Type Checking (When are data types checked?)](#14-type-checking-when-are-data-types-checked)
    - [1.4.1. Static](#141-static)
    - [1.4.2. Dynamic](#142-dynamic)
  - [1.5. Memory Management](#15-memory-management)
    - [1.5.1. Manual](#151-manual)
    - [1.5.2. Automatic Garbage Collection](#152-automatic-garbage-collection)
    - [1.5.3. Deterministic](#153-deterministic)
    - [1.5.4. Automatic Reference Counting](#154-automatic-reference-counting)

# 1. Types of Languages

## 1.1. Design Approach (How is the program designed?)
### 1.1.1. Procedural
- Execute line by line
### 1.1.2. Functional
- Functions encapsulate instructions
- Contains procedural design
### 1.1.3. OOP
- Encapsulation, Abstraction, Inheritance/Delegation, Polymorphism
- Contains procedural and functional design too

## 1.2. Time of Conversion (When is it converted?)
### 1.2.1. Compile Type
- Converted directly into machine code on build 
- Processor runs machine code as a whole
- e.g., recipe in greek, translated to english before cooking
- Adv:
  - Faster
### 1.2.2. Interpreted Type
- Slower (improved by JIT compilation)
- Converted into machine code line by line  
- e.g., recipe in greek, greek friend instructs you step by step in english
- Adv:
  - Slower

## 1.3. Instruction Approach (How is the compiler instructed?)
- Can have both types
### 1.3.1. Imperative
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

### 1.3.2. Declarative
- Instruct compiler of final output
- e.g., getting odd numbers in LINQ
  ```
  List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
  
  var results = collection.Where( num => num % 2 != 0);
  ```
  - Instruction: Create result collection containing all numbers which are odd

## 1.4. Type Checking (When are data types checked?)
### 1.4.1. Static
- Compile time checking
### 1.4.2. Dynamic
- Runtime checking
## 1.5. Memory Management

### 1.5.1. Manual
- Explicit allocation and freeing of memory
- e.g,, C malloc, free
### 1.5.2. Automatic Garbage Collection

### 1.5.3. Deterministic
### 1.5.4. Automatic Reference Counting


Language Compilation Process
1. Translation: Translate compiled language to assembly language
2. Assemble: Convert assembly language to machine code 