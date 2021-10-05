# Dependency Inversion of Control (IOC)
- Traditional Control Flow:
  - Code calls libs
- Inversion of Control
  - Framework calls into code


## Dependency Injection
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
### Injection Types
- Client is given dependency (bar)
```
    //Foo Needs an IBar
    public class Foo {
        Bar bar;

        Foo(Bar bar) {
            this.bar = bar;
        }
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
### Constructor Injection 
- Used when
  - dependencies are obligatory
    - when this obj is constructed, it NEEDS this dep
  - goal is permanency
    - dep is not gonna change
### Setter Injection
- Used when
  - dependencies are replaceable
    - 
### Field Injection
## Service Locator
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

## Producer Graphs 