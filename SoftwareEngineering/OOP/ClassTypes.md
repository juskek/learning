- [1. Class Types](#1-class-types)
  - [1.1. Static](#11-static)
  - [1.2. Final](#12-final)
  - [1.3. Abstract](#13-abstract)
  - [1.4. Concrete](#14-concrete)
  - [1.5. Singleton](#15-singleton)
  - [1.6. PO_O](#16-po_o)
  - [1.7. Inner/Nested](#17-innernested)
    - [1.7.1. Static Nested](#171-static-nested)
    - [1.7.2. Non-static Nested (Inner)](#172-non-static-nested-inner)
      - [1.7.2.1. Member Inner Class](#1721-member-inner-class)
      - [1.7.2.2. Anonymous Inner Class](#1722-anonymous-inner-class)
      - [1.7.2.3. Method Local Inner Class](#1723-method-local-inner-class)
      - [1.7.2.4. Anonymous Inner Class](#1724-anonymous-inner-class)
      - [1.7.2.5. Nested Interface](#1725-nested-interface)

# 1. Class Types

## 1.1. Static
- Cannot be instantiated or inherited
  - Members are static
- Java
  - Must be nested in non-static class
  - Only static members
  - Cannot access non-members of super

## 1.2. Final
- Immutable after declaration
- Java
  - Cannot be extended
## 1.3. Abstract
- Cannot be instantiated, can be inherited/extended
- Any abstract methods must be implemented after extending 


## 1.4. Concrete
- Regular class, all members implemented

## 1.5. Singleton
- Can only be instantiated once
- Applications
  - Socket programming
  - Database connectio
- Java
  - Process:
    1. Create concrete class
    2. Create private constructor
    3. Create static method that returns object
    ```
    public class Singleton {
        private static Singleton instance = null;
        private Singleton() {
            // Constructor
        }
        public static Singleton getInstance() {
            if (instance == null) {
                try {
                    instance = new Singleton();
                } catch (Exception e) {
                    e.printStackTrace
                }
            }
            return instance;
        }
    }
    ```
## 1.6. PO_O
- Plain Old ____ Object
- Only private variables, setter and getter
- Java
  - No pre-specified annotations
  - Cannot implement pre-defined implementations
  - No constructor required
  - Cannot extend predefined classes

## 1.7. Inner/Nested
- Class within a class

### 1.7.1. Static Nested
- Static class within class 
### 1.7.2. Non-static Nested (Inner)
- Non-static class within class
#### 1.7.2.1. Member Inner Class
- Class defined outside method

#### 1.7.2.2. Anonymous Inner Class
- Member inner class without name
- Used for implementing an interface or extending class

#### 1.7.2.3. Method Local Inner Class
- Class defined within a method
#### 1.7.2.4. Anonymous Inner Class
- Local inner class without name

#### 1.7.2.5. Nested Interface
- Interface within class