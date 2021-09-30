
- [1. Core Concepts](#1-core-concepts)
  - [1.1. Encapsulation](#11-encapsulation)
  - [1.2. Abstraction](#12-abstraction)
  - [1.3. Inheritance](#13-inheritance)
  - [1.4. Polymorphism](#14-polymorphism)
    - [1.4.1. Ad Hoc Polymorphism](#141-ad-hoc-polymorphism)
      - [1.4.1.1. Function Overloading](#1411-function-overloading)
      - [1.4.1.2. Operator Overloading](#1412-operator-overloading)
    - [1.4.2. Parametric Polymorphism](#142-parametric-polymorphism)
      - [1.4.2.1. Generic Function](#1421-generic-function)
      - [1.4.2.2. Generic Datatypes](#1422-generic-datatypes)
    - [1.4.3. Subtype/Inclusion Polymorphism](#143-subtypeinclusion-polymorphism)
      - [1.4.3.1. Virtual Function](#1431-virtual-function)
      - [Single and Dynamic Dispatch](#single-and-dynamic-dispatch)
      - [Double Dispatch](#double-dispatch)
      - [Multiple Dispatch](#multiple-dispatch)
      - [Predicate Dispatch](#predicate-dispatch)

# 1. Core Concepts
## 1.1. Encapsulation
- Compartmentalising objects with classes to prevent unwanted interaction

## 1.2. Abstraction
- Extracting only the important bits of the code and hiding everything else to reduce complexity 

## 1.3. Inheritance
- Passing of properties of a parent class to a child class
- Parent: Super/Base
- Child: Sub/Derived

## 1.4. Polymorphism
- Altering an object into various forms by changing parts of it
- Classes of polymorphism: ad hoc, parametric, subtype

### 1.4.1. Ad Hoc Polymorphism
- morphing when necessary
#### 1.4.1.1. Function Overloading
- >1 definition for same function name
- e.g., print(int i), print(double f)
#### 1.4.1.2. Operator Overloading
- Giving new meaning to an operator (+=-* etc) 
- e.g.,
  ```
  class Position {
      x = 1;
      y = 1;
      // OPERATOR OVERLOADING
      Position operator + (Position pos) {
          Position newPos;
          newPos.x = this.x + pos.x;
          newPos.y = this.y + pos.y;
          return newPos;
      }
  }
  main() {
      Position pos1, pos2;
      Position pos3 = pos1 + pos2;
      print(pos3);
      // OUT: Position with x=2,y=2
  }
  ```
  - Similar to defining a method (return operator args)

### 1.4.2. Parametric Polymorphism
- morphing for parameter types
#### 1.4.2.1. Generic Function
- Function which can accept various types and return various types
- e.g., print(Type t)
#### 1.4.2.2. Generic Datatypes
- Data type which can store various subtypes
- e.g., 
  - List<Type t>

### 1.4.3. Subtype/Inclusion Polymorphism
- morphing for subclasses
#### 1.4.3.1. Virtual Function
- member function which is expected to be redefined in subclasses
- e.g., 
  - render() and update() when extending a Game class
#### Single and Dynamic Dispatch
#### Double Dispatch
#### Multiple Dispatch
#### Predicate Dispatch