# Javascript
## Compilers
- V8

## Environments
- Node.js
  - Server side
  - Manual implementation
- Cloudflare worker
  - Server side
  - Existing network
- Chrome V8
  - Client side
## Syntax
### Variable Declaration
#### var
- global/function scoped
- can be redeclared and updated 
- hoisted and init as undefined
#### let
- block scoped {}
- can be updated but not redeclared
- hoisted but not init
#### const
- block scoped {}
- cannot be redeclared or updated
### Immediately Invoked Function Expression (IIFE)
- Running the function as soon as it is 
- Returns `undefined` by default, use `!` to return `true`
- 

```
    // function declaration
    function foo() {}
    foo(); // invocation to run declared function
   
    // IIFE
    // function expression (self invoking, runs as soon as declared)
    (function foo() {})();
    !function foo() {}();

    // Anonymous IIFE
    (function (){})();
    !function (){}();

 


```
