

# Syntax
## Immediately Invoked Function Expression (IIFE)
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
