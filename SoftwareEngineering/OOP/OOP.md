
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
      - [1.4.3.2. Method Dispatch](#1432-method-dispatch)
        - [1.4.3.2.1. Static vs Dynamic Dispatch](#14321-static-vs-dynamic-dispatch)
        - [1.4.3.2.2. Single vs Multiple Dispatch](#14322-single-vs-multiple-dispatch)
        - [1.4.3.2.3. Multiple Dispatch](#14323-multiple-dispatch)

# 1. Core Concepts
## 1.1. Encapsulation
- Compartmentalising objects with classes to prevent unwanted interaction (hiding state details)
- e.g., Pig.weight, Cow.weight
- Abstraction starts when associating data types with the same behaviour together 

## 1.2. Abstraction
- Extracting behaviour from data types and associating them together to simplify design  
- e.g., Pig extends Animal, Cow extends Animal
  - Pig and Cow is an abstraction of Animal, they all eat, sleep and move
  - Further abstraction can be performed, e.g., DairyAnimal extends Animal, MeatAnimal extends Animal
    - Cow, Goat extends DairyAnimal
    - Pig, Chicken extends MeatAnimal
      - Abstraction makes code design easier, e.g., defining ideal food for a MeatAnimal removes the need to define it twice in Pig and Chicken 
- Inheritance starts when defining members for simplifying code
- Polymorphism starts when defining members for various types

## 1.3. Inheritance
- Passing of properties of a parent class to a child class
  - Parent: Super/Base
  - Child: Sub/Derived
- e.g., Pig extends MeatAnimal, gets ideal food as well as properties from Animal...

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
- e.g., List<Type t>

### 1.4.3. Subtype/Inclusion Polymorphism
- morphing for subclasses
#### 1.4.3.1. Virtual Function
- member function which is expected to be redefined in subclasses
- e.g., 
  - render() and update() when extending a Game class
#### 1.4.3.2. Method Dispatch
- Algorithm used to decide which method to invoke in response to a message
- e.g., System.print(integer)
  - message: print()
  - receiver: System
  - argument: integer
  - System receives the message print, what happens next?
##### 1.4.3.2.1. Static vs Dynamic Dispatch
- Static: Decision made at compile time
- Dynamic: Decision made at runtime
  - e.g., 
  ```
  class Cat:
    def speak(self):
        print("Meow")

  class Dog:
      def speak(self):
          print("Woof")

  def speak(pet):
      cat.speak() # static
      pet.speak() # dynamic

  ```
##### 1.4.3.2.2. Single vs Multiple Dispatch
- Single: Decision based on a single type
  - e.g., player.touch(hazard)
    - Method invoked based on type of player only
    - Player gets damaged when touching hazard 
- Multiple: Decision based on multiple types
  - e.g., player.touch(hazard), fire, cactus extends hazard
    - Method invoked based on both type of player and hazard
    - Player gets burnt when touching fire
    - Player get pricked when touching cactus
##### 1.4.3.2.3. Multiple Dispatch
- Dispatch based on multiple types
- e.g., (animal1 and animal2).method()



