- [1. Dependency Inversion of Control (IOC)](#1-dependency-inversion-of-control-ioc)
  - [1.1. Dependency Injection](#11-dependency-injection)
    - [1.1.1. Injection Types](#111-injection-types)
      - [1.1.1.1. Constructor Injection](#1111-constructor-injection)
      - [1.1.1.2. Setter Injection](#1112-setter-injection)
      - [1.1.1.3. Field Injection](#1113-field-injection)
  - [1.2. Producer Graphs](#12-producer-graphs)
  - [1.3. Service Locator](#13-service-locator)

# 1. Dependency Inversion of Control (IOC)
- Traditional Control Flow:
  - Code calls libs
- Inversion of Control
  - Framework calls into code


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
