- [1. Architecture](#1-architecture)
  - [1.1. main](#11-main)
  - [1.2. routes](#12-routes)
  - [1.3. styles](#13-styles)
  - [1.4. index](#14-index)
- [2. Syntax](#2-syntax)
  - [2.1. Operators](#21-operators)
    - [2.1.1. Comparisons](#211-comparisons)
      - [2.1.1.1. Assignment (=)](#2111-assignment-)
      - [2.1.1.2. Equality (==)](#2112-equality-)
      - [2.1.1.3. Identity (===, or identical(a,b))](#2113-identity--or-identicalab)
  - [Conditional](#conditional)
    - [if null (??)](#if-null-)
  - [2.2. Cascade Notation](#22-cascade-notation)
  - [2.3. Initialiser List (:)](#23-initialiser-list-)
  - [2.4. Objects & Classes](#24-objects--classes)
    - [2.4.1. Object Constructors](#241-object-constructors)
- [3. Sound Null Safety](#3-sound-null-safety)
  - [3.1. Unsound null safety](#31-unsound-null-safety)
  - [3.2. Disable sound null safety](#32-disable-sound-null-safety)
- [4. Scoping](#4-scoping)
  - [4.1. Lexical Scoping](#41-lexical-scoping)
- [5. Syntax](#5-syntax)
  - [5.1. Arrow](#51-arrow)
  - [5.2. Closure/Inline Functions](#52-closureinline-functions)
  - [Anonymous Multiline Function](#anonymous-multiline-function)
  - [Conditional Rendering](#conditional-rendering)
    - [Binary if](#binary-if)
    - [Ternary Operator](#ternary-operator)
    - [Spread Operator](#spread-operator)
    - [](#)
- [Layout](#layout)
  - [SafeArea](#safearea)
  - [Container](#container)
  - [SizedBox](#sizedbox)
  - [Constraints](#constraints)
  - [Performance](#performance)
    - [build() is costly](#build-is-costly)
    - [itemExtend for ListView](#itemextend-for-listview)
- [6. Animations](#6-animations)
  - [6.1. Drawing-based](#61-drawing-based)
  - [6.2. Code-based](#62-code-based)
    - [6.2.1. Implicit (AnimatedFoo)](#621-implicit-animatedfoo)
      - [6.2.1.1. BuiltIn](#6211-builtin)
      - [6.2.1.2. Custom: TweenAnimationBuilder](#6212-custom-tweenanimationbuilder)
    - [6.2.2. Explicit (FooTransition)](#622-explicit-footransition)
      - [6.2.2.1. Built In](#6221-built-in)
      - [6.2.2.2. Custom](#6222-custom)
        - [6.2.2.2.1. AnimatedWidget](#62221-animatedwidget)
        - [6.2.2.2.2. CustomPainter](#62222-custompainter)
        - [6.2.2.2.3. AnimatedBuilder](#62223-animatedbuilder)
- [7. Asynchronous Programming](#7-asynchronous-programming)
  - [7.1. Terminology](#71-terminology)
  - [7.2. futures](#72-futures)
  - [7.3. async](#73-async)
  - [7.4. await](#74-await)
- [8. Generators (*)](#8-generators-)
- [9. Inheritance](#9-inheritance)
  - [9.1. extends](#91-extends)
  - [9.2. implements](#92-implements)
  - [9.3. with (mixin)](#93-with-mixin)
- [10. Variable Types](#10-variable-types)
  - [10.1. Lists](#101-lists)
    - [10.1.1. Constructors](#1011-constructors)
      - [10.1.1.1. .empty()](#10111-empty)
      - [10.1.1.2. .filled()](#10112-filled)
      - [10.1.1.3. .from()](#10113-from)
      - [10.1.1.4. .generate()](#10114-generate)
      - [10.1.1.5. .of()](#10115-of)
      - [10.1.1.6. .unmodifiable()](#10116-unmodifiable)
  - [10.2. Modifiers](#102-modifiers)
    - [10.2.1. static](#1021-static)
    - [10.2.2. final](#1022-final)
    - [10.2.3. const](#1023-const)

# 1. Architecture
## 1.1. main
## 1.2. routes
## 1.3. styles
## 1.4. index
# 2. Syntax
## 2.1. Operators
### 2.1.1. Comparisons
#### 2.1.1.1. Assignment (=)
- Assign value to variable
#### 2.1.1.2. Equality (==)
- Check if two variables/objects are equal
#### 2.1.1.3. Identity (===, or identical(a,b))
- Check if two variables/objects refer to the same instance/object
## Conditional
### if null (??)
## 2.2. Cascade Notation
Prevents repeating target for several call methods on same object.
```
List list = [];
list.add(color1);
list.add(color2);

list
  ..add(color1)
  ..add(color2);
```
## 2.3. Initialiser List (:)
Used to:
- Initialise list of expressions that can:
  - access constructor parameters
  - assign to instance fields (even final instance fields!)
- Call other constructors
  - e.g., superclass
- Assert constructor parameters
NOTE:
- Initialiser list is executed before constructor body
- Use `this.instanceVariable` when there is a name conflict, else omit

## 2.4. Objects & Classes
### 2.4.1. Object Constructors
Construct/initialise an object of that class.
Initialisation:
```
// init class
class FooClass {
  FooClass(); // init object
  FooClass(arg); // init object with mandatory argument
  FooClass({arg1, arg2}); // init object with named optional arguments
  FooClass([arg1, arg2]); // init object with positional optional arguments
}
```
- Named and positional optional arguments cannot be used concurrently
- Values must be provided for all positional arguments if one argument wants to be used, e.g., `FooClass(1,2)`
- This does not apply for named optional arguments, e.g., `FooClass(arg2=2)`
# 3. Sound Null Safety
- Types are non-nullable by default
- Variables cannot contain `null` unless allowed to:
  - To allow null values, add `?` after type declaration
```
    int nonNullableInt = 1; // cannot be null
    int? aNullableInt = null; 
```
- Non-null assertion operator variable!.method tells the compiler that the value of the variable will not be null during runtime, and hence methods can be called on the variable.
## 3.1. Unsound null safety
- Mixed-version programme
- Some files with sound NS and some with unsound NS
- Runtime null only occurs from leakage of unsound to sound code

## 3.2. Disable sound null safety
`flutter run --no-sound-null-safety`


# 4. Scoping
## 4.1. Lexical Scoping
Inner function has access to parent variables



# 5. Syntax
## 5.1. Arrow 
```
    => expression,
    // is equivalent to 
    {return expression;},
```

## 5.2. Closure/Inline Functions
```
    () => expression
    
    // is equivalent to
    function () {
        return expression
    }
```

## Anonymous Multiline Function
```
  () {expression}
  // is equivalent to
  function () {
      return expression
  }
```

## Conditional Rendering
### Binary if
`if (Responsive.isDesktop()) Text('Desktop)`
### Ternary Operator
`Responsive.isDesktop() ? Text('Desktop') : null`
### Spread Operator
- Can be used to return multiple widgets
`if (Responsive.isDesktop()) ...[
    Text('Desktop')
    Text('Mode')
  ]
`

###  
# Layout
## SafeArea
- Should exist at top level
  - for iPhone notches etc
## Container
- Expands to fit parent 

## SizedBox
- Fixed size or
- unconstrained in height or width if it is null
## Constraints
- Constraints go down
- Sizes go up
- Parents set position

- A widget
  - gets constrained by its parent
  - tells its parent what its size is within the constraints 
  - tells its children what their constraints are
  - positions its children
## Performance
### build() is costly
- avoid repetitive build in complex layouts
- PROBLEM: top level stateless widget has a build method
  - within build method there are a bunch of widgets
  - whenever build method is called again all widgets are rebuilt
- SOLUTIONS:
  - when calling widget which doesnt change, declare as constant
  - extend widget as stateless widget, which has its own build method
    - widget will only be built once

### itemExtend for ListView 
- when action triggers jumping to other end of the list
- 
# 6. Animations
Animation Types:
## 6.1. Drawing-based
- Use external framework and export to flutter (e..g, Flare, Lottie)
## 6.2. Code-based
### 6.2.1. Implicit (AnimatedFoo)
#### 6.2.1.1. BuiltIn
#### 6.2.1.2. Custom: TweenAnimationBuilder
### 6.2.2. Explicit (FooTransition)
- Requires AnimationController, and managing life cycle inside stateful widget
Used if any of the following is true:
- Repeats forever
- Discontinuous animation
- Multiple widgets animating together
#### 6.2.2.1. Built In
#### 6.2.2.2. Custom
##### 6.2.2.2.1. AnimatedWidget
- Standalone widget
- Use Process:
1. Define class to extend `AnimatedWidget`
2. Override `build` to return desired widget which will be animated
3. Add listenable argument to constructor and pass it up to Animated widget as well. This tells the widget what to look out for.
4. Add getter to make listenable argument usable. 
5. Add listenable argument to build method to affect widget properties.
6. Create `AnimationController` within `StateWidget` where animation will be used. Ensure `AnimationController` is initialised in `init` and disposed in `dispose`.
7. Extend `StatefulWidget` with `TickerProviderStateMixin` to get a ticker listener. The ticker listens to frameCallback and determines the duration between the current and last frame, and passes it to the controller to control the animation. Implement it in the controller with vsync.
8. Add methods to direct the controller.
EXAMPLE:
```
// 1.
class FooTransition extends AnimatedWidget {
  // 3.
  const FooTransition(Type listenableArg)
    : super(listenable: listenableArg);
  
  // 4.
  Animation<type> get listenableArg => listenable


  // 2.
  @override
  Widget build(BuildContext context) {
    // 5. 
    return ...
  }

class ExampleStateful extends StatefulWidget {
  
}

class _ExampleStatefulState extends State<ExampleStateful> 
  with TickerProviderStateMixin {
    late final AnimationController _controller = AnimationController(vsync: this, ...)
      ..method1()
      ..method2();

    @override
    void dispose() {
      _controller.dispose();
      super.dispose();
    }
    @override
    Widget build(BuildContext context) {
      return FooTransition(controller: _controller);
    }

}

}

```
##### 6.2.2.2.2. CustomPainter
- Similar to AnimatedWidget but paints directly to canvas without Widget build paradigm, for complex animations or higher performance. Could cause more performance problems if misused.
- CustomPaint is a widget which provides a canvas and takes a CustomPainter to execute paint commands.
- Implementation:
1. Define `CustomPaint` widget with painter and child/size in `StateWidget`
2. Define `myPainter` class as extension of `CustomPainter`, override `paint` and `shouldRepaint`.
3. Define paint commands within `paint` function with `canvas.method()`.
4. Define repaint scenarios within `shouldRepaint` if necessary.
5. For animations, pass the controller into the painter and change parameters with progress value.

```
// 1.
class ExampleStateful extends StatefulWidget {
  
}

class _ExampleStatefulState extends State<ExampleStateful> 
with TickerProviderStateMixin {
  
  late final AnimationController _controller = AnimationController(vsync: this, ...)
      ..method1()
      ..method2();

  final customPaint = CustomPaint(
  painter: MyPainter(_controller),
  child: myWidget(),
  )

  @override
  Widget build(BuildContext context) {
    return customPaint;
}


class MyPainter extends CustomPainter {
  @override
  void paint(ui.Canvas canvas, ui.Size size) {
    // paint commands
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) {
    // hook called when CustomPainter is rebuilt
    // when to repaint, set to true if necessary
    return false;
  }


}
```
##### 6.2.2.2.3. AnimatedBuilder
- Part of parent widget




# 7. Asynchronous Programming
Completion of other work while waiting for a complex operation to finish.
The complex operation is usually set to be the asynchronous function.

## 7.1. Terminology
- Synchronous operation: Blocks other operations from executing till it completes
- Synchronous function: Only syncOp
- Asynchronous operation: Allows other operations to execute before it completes
- Asynchronous function: >=1 asyncOp


## 7.2. futures
- `future`: instance of Future class
  - Represents result of asyncOp:
    - Uncompleted, waiting for asyncOp to finish or throw an error
    - Completed, returns value for successful asyncOp, or throw error
    - 
- `Future<ReturnValueType>`: class returning future value of ReturnValueType
  -  

## 7.3. async
## 7.4. await

# 8. Generators (*)
- Function which returns multiple values
- e.g., sync function returns `int`, async function returns `Future<int>`, sync generator returns `Iterable<int>`, async generator returns `Stream<int>`
- Uses `yield` instead of `return`


# 9. Inheritance
## 9.1. extends
- making all properties, variables, functions of superclass  available to subclass
## 9.2. implements
- making type of superclass available to subclass
- all functions must be implemented/overridden 
## 9.3. with (mixin)
- making properties, variables, functions of a different class available to a subclass 


# 10. Variable Types
## 10.1. Lists
### 10.1.1. Constructors
#### 10.1.1.1. .empty()
- 
#### 10.1.1.2. .filled()
- List of given length with fixed value at each position
#### 10.1.1.3. .from()
- List containing all elements
#### 10.1.1.4. .generate()
- List of given length with values from a generator
#### 10.1.1.5. .of()
- List from elements
#### 10.1.1.6. .unmodifiable()
- Unmodifiable list containing all elements

## 10.2. Modifiers
### 10.2.1. static
- modifies members of a class (variables, functions)
  - only affects the class, not on instances of the class 
### 10.2.2. final
- modifies variables (`var, int, double`)
  - must be assigned on init
  - shallow immutability: e.g., final collection members can be mutable, collection itself is immutable
### 10.2.3. const
- modifies values and objects (`[1,2,3], Point(2,3)`)
  - compile time constant: state can be determined at compile time and is then frozen (e.g., `1+2` is compile time const, `DateTime.now()` is not)
  - deep (transitive) immutability: e.g., const collection members are immutable, recursively
  - canonicalised values and objects: all assignments of the const value/object will refer to the same instance