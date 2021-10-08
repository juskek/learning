- [1. Dependency Inversion of Control (IOC)](#1-dependency-inversion-of-control-ioc)
  - [1.1. Dependency Injection](#11-dependency-injection)
    - [1.1.1. Injection Types](#111-injection-types)
      - [1.1.1.1. Constructor Injection](#1111-constructor-injection)
      - [1.1.1.2. Setter Injection](#1112-setter-injection)
      - [1.1.1.3. Field Injection](#1113-field-injection)
  - [1.2. Producer Graphs](#12-producer-graphs)
  - [1.3. Service Locator](#13-service-locator)
- [Evolution](#evolution)
  - [Manual DI](#manual-di)
  - [Spring 1 & 2 (XML)](#spring-1--2-xml)
  - [Guice (Java)](#guice-java)
  - [Dagger 1](#dagger-1)
  - [Dagger 2](#dagger-2)

# 1. Dependency Inversion of Control (IOC)
- Traditional Control Flow:
  - Code calls libs
- Inversion of Control
  - Framework calls into code
  - aka Hollywood Principle; don't call us, we'll call you


## 1.1. Dependency Injection
- Process by which an object (client) receives other objects it depends on (service) through an injector
  - Injector: Code that passes service to client
- Characteristics
  - Injector tells client what service to use
  - Client cannot find or build service 
- Adv.:
  - IOC
    - Service creation and maintenance passed to injector (framework)
  - Loose Coupling
    - Easy testing/swapping of code
- Disadv.:
  - Decreased readability/ increased complexity
  - Reliance on framework, even if buggy
### 1.1.1. Injection Types
- e.g., client (foo) is given dependency (bar)
```
    //Foo Needs an IBar
    public class Foo {
        Bar bar;

        // constructor inj
        Foo(Bar bar) {
            this.bar = bar;
        }
        // setter inj
        setDep(Bar bar) {
            this.bar = bar;
        }
        main() {
            // Dep Inj: foo is given bar
            foo = new Foo(bar); // constructor inj
            foo.setDep(bar); // setter inj
            foo.bar = bar; // field inj
        }
    }
```
#### 1.1.1.1. Constructor Injection 
- Used when
  - deps are obligatory
    - when this obj is constructed, it NEEDS this dep
  - deps are not gonna change
#### 1.1.1.2. Setter Injection
- Used when
  - dependencies are replaceable

#### 1.1.1.3. Field Injection
- Convenient to write and implement


## 1.2. Producer Graphs 
## 1.3. Service Locator
- Client (foo) responsible for creating service (bar)
```
    //Foo Needs an Bar
    public class Foo {
        private Bar bar;
        public Foo()
        {
            // Service Locator: foo builds bar
            this.bar = Container.Get<IBar>();
        }
        public void main() {
            foo = new Foo(); // client
        }
    }
```


# Evolution
## Manual DI
- Manually injecting deps into new objects
- Problem: 
  - Objects have to be manually ordered to ensure trickle down deps are satisfied

## Spring 1 & 2 (XML)
- Solved initialisation ordering
- Automated code generation for DI
- Problem:
  - XML was too verbose and hard to read
  - Validation of configuration only at runtime
  - Untraceable application flow

## Guice (Java)
- Used annotations and generics to achieve
  - e.g., @Inject, @Provides
- Decentralised, decreased configurations instead of a massive central config file
- Dynamic and conditional configuration
- Problem
  - Runtime stack trace had too much noise
  - Bindings were untraceable
    - e.g., which dep implementation was used?

## Dagger 1
- Introduced compile time error reporting
- Shows generated DI code for debugging
- Reduced stack frames
- Problems:
  - Generated code ugly

## Dagger 2
- Compile time validation for entire graph
- Improved traceability
- Generated code like handwritten code
- Increased speed