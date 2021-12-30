- [1. Architecture](#1-architecture)
  - [1.1. main](#11-main)
  - [1.2. routes](#12-routes)
  - [1.3. styles](#13-styles)
  - [1.4. index](#14-index)
- [State, Widgets and Elements](#state-widgets-and-elements)
  - [State Definition](#state-definition)
  - [Stateless Widget](#stateless-widget)
  - [Stateful Widget](#stateful-widget)
  - [Lifecycles](#lifecycles)
- [Trees](#trees)
  - [Widget Tree (WT)](#widget-tree-wt)
  - [Element Tree (ET)](#element-tree-et)
- [2. Syntax](#2-syntax)
  - [2.1. Operators](#21-operators)
    - [2.1.1. Comparisons](#211-comparisons)
      - [2.1.1.1. Assignment (=)](#2111-assignment-)
      - [2.1.1.2. Equality (==)](#2112-equality-)
      - [2.1.1.3. Identity (===, or identical(a,b))](#2113-identity--or-identicalab)
  - [2.2. Conditional](#22-conditional)
    - [2.2.1. if null (??)](#221-if-null-)
  - [2.3. Cascade Notation](#23-cascade-notation)
  - [2.4. Initialiser List (:)](#24-initialiser-list-)
  - [2.5. Objects & Classes](#25-objects--classes)
    - [2.5.1. Object Constructors](#251-object-constructors)
- [3. Sound Null Safety](#3-sound-null-safety)
  - [3.1. Unsound null safety](#31-unsound-null-safety)
  - [3.2. Disable sound null safety](#32-disable-sound-null-safety)
- [4. Scoping](#4-scoping)
  - [4.1. Lexical Scoping](#41-lexical-scoping)
- [5. Syntax](#5-syntax)
  - [5.1. Arrow](#51-arrow)
  - [5.2. Closure/Inline Functions](#52-closureinline-functions)
  - [5.3. Anonymous Multiline Function](#53-anonymous-multiline-function)
  - [5.4. Conditional Rendering](#54-conditional-rendering)
    - [5.4.1. Binary if](#541-binary-if)
    - [5.4.2. Ternary Operator](#542-ternary-operator)
    - [5.4.3. Multiple if](#543-multiple-if)
    - [5.4.4. Spread Operator](#544-spread-operator)
- [6. Sizing](#6-sizing)
  - [Sizes, Constraints and Positions](#sizes-constraints-and-positions)
    - [Rules](#rules)
    - [Process](#process)
    - [Limitations](#limitations)
    - [Mechanisms](#mechanisms)
    - [Types of Constraints](#types-of-constraints)
      - [As Big As Possible](#as-big-as-possible)
      - [Same Size if Possible](#same-size-if-possible)
      - [Fixed Size if Possible](#fixed-size-if-possible)
  - [6.1. BoxConstraints](#61-boxconstraints)
  - [LayoutBuilder](#layoutbuilder)
  - [FractionallySizedBox](#fractionallysizedbox)
- [7. Layout](#7-layout)
  - [7.1. SafeArea](#71-safearea)
  - [7.2. Container](#72-container)
  - [7.3. Aligning](#73-aligning)
  - [7.4. SizedBox](#74-sizedbox)
  - [SliverGrid](#slivergrid)
  - [7.6. Performance](#76-performance)
    - [7.6.1. build() is costly](#761-build-is-costly)
    - [7.6.2. itemExtend for ListView](#762-itemextend-for-listview)
- [Weird Problems](#weird-problems)
  - [Vertical Dividers not showing](#vertical-dividers-not-showing)
- [8. Scrolling](#8-scrolling)
  - [8.1. ListView](#81-listview)
  - [8.2. ListView.builder()](#82-listviewbuilder)
  - [8.3. ListView.custom()](#83-listviewcustom)
- [9. Animations](#9-animations)
  - [9.1. Drawing-based](#91-drawing-based)
  - [9.2. Code-based](#92-code-based)
    - [9.2.1. Implicit (AnimatedFoo)](#921-implicit-animatedfoo)
      - [9.2.1.1. BuiltIn](#9211-builtin)
      - [9.2.1.2. Custom: TweenAnimationBuilder](#9212-custom-tweenanimationbuilder)
    - [9.2.2. Explicit (FooTransition)](#922-explicit-footransition)
      - [9.2.2.1. Built In](#9221-built-in)
      - [9.2.2.2. Custom](#9222-custom)
        - [9.2.2.2.1. AnimatedWidget](#92221-animatedwidget)
        - [9.2.2.2.2. CustomPainter](#92222-custompainter)
        - [9.2.2.2.3. AnimatedBuilder](#92223-animatedbuilder)
- [10. Asynchronous Programming](#10-asynchronous-programming)
  - [10.1. Terminology](#101-terminology)
  - [10.2. futures](#102-futures)
  - [10.3. async](#103-async)
  - [10.4. await](#104-await)
- [11. Generators (*)](#11-generators-)
- [12. Inheritance](#12-inheritance)
  - [12.1. extends](#121-extends)
  - [12.2. implements](#122-implements)
  - [12.3. with (mixin)](#123-with-mixin)
- [13. Variable Types](#13-variable-types)
  - [13.1. Lists](#131-lists)
    - [13.1.1. Constructors](#1311-constructors)
      - [13.1.1.1. .empty()](#13111-empty)
      - [13.1.1.2. .filled()](#13112-filled)
      - [13.1.1.3. .from()](#13113-from)
      - [13.1.1.4. .generate()](#13114-generate)
      - [13.1.1.5. .of()](#13115-of)
      - [13.1.1.6. .unmodifiable()](#13116-unmodifiable)
  - [13.2. Modifiers](#132-modifiers)
    - [13.2.1. static](#1321-static)
    - [13.2.2. final](#1322-final)
    - [13.2.3. const](#1323-const)

# 1. Architecture
## 1.1. main
## 1.2. routes
## 1.3. styles
## 1.4. index

# State, Widgets and Elements
## State Definition
- Info within a widget which is read for building

## Stateless Widget
- State in widget immutable once built
- Explanation:
  - Once widget builds element,
  - Data and functions which exist in widget cannot change what is on the screen
- Components:
  - Widget Tree
    - Stateless Widget
      - Builds stateless element and mounts it
  - Element Tree
    - Stateless Element
- Lifecycle Events
  - build() called when
    - Widget created for first time
    - Parent changes/updates
    - InheritedWidget changes
## Stateful Widget
- State in widget mutable after build
- Explanation:
  - Once widget builds element, 
  - Data and functions which exist in widget can change
- Components:
  - Widget Tree
    - Stateful Widget
      1 Creates stateful element and mounts it 
      3 Creates state object
    - State Widget
      4 Holds state and used as reference for stateful element 
      5 Builds stateless element and mounts it 
      6 Change in state triggers rebuild
  - Element Tree
    - Stateful Element
      2 Requests state object from stateful widget
    - Stateless Element
- Lifecycle Events
  - build() called when
    - Stateful changes but State persists
    - State changes
  - initState() called when
    - object inserted into WT
  - dispose() called when
    - object removed from WT permanently
  - didChangeDependencies() called when
    - State changes
  - didUpdateWidget() called when
    - Stateful config changes
  - deactivate() called when
    - object removed from WT temp
  - setState() triggers
    - State change
## Lifecycles

# Trees
## Widget Tree (WT)
- How, what and when to show on screen
- Creates elements to mount in element tree
## Element Tree (ET)
- What is currently shown on screen


# 2. Syntax
## 2.1. Operators
### 2.1.1. Comparisons
#### 2.1.1.1. Assignment (=)
- Assign value to variable
#### 2.1.1.2. Equality (==)
- Check if two variables/objects are equal
#### 2.1.1.3. Identity (===, or identical(a,b))
- Check if two variables/objects refer to the same instance/object
## 2.2. Conditional
### 2.2.1. if null (??)
## 2.3. Cascade Notation
Prevents repeating target for several call methods on same object.
```
List list = [];
list.add(color1);
list.add(color2);

list
  ..add(color1)
  ..add(color2);
```
## 2.4. Initialiser List (:)
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

## 2.5. Objects & Classes
### 2.5.1. Object Constructors
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

## 5.3. Anonymous Multiline Function
```
  () {expression}
  // is equivalent to
  function () {
      return expression
  }
```

## 5.4. Conditional Rendering
### 5.4.1. Binary if
`if (Responsive.isDesktop()) Text('Desktop)`
### 5.4.2. Ternary Operator
`Responsive.isDesktop() ? Text('Desktop') : null`

### 5.4.3. Multiple if
```
  (() {
    // your code here
  }())
```
### 5.4.4. Spread Operator
- Can be used to return multiple widgets
`if (Responsive.isDesktop()) ...[
    Text('Desktop')
    Text('Mode')
  ]
`

# 6. Sizing
## Sizes, Constraints and Positions
### Rules
  - Constraints go down
  - Sizes go up
  - Parent sets position
### Process 
For an arbitrary widget X, its parent Y, and its children Z
1. Y passes its constraints down to X
   - min/max height/width
2. X passes its constraints down to Z
3. X asks Z what size they are
   - width/height
4. X sets positions of Z
5. X tells Y its final size 

### Limitations
- Size defined in widget only within constraints of parent
- Widget does not know/decide its position
- Defining alignment must be specific or child size may be ignored

### Mechanisms
- RenderBox
  - Underlying object used to render widgets

### Types of Constraints
#### As Big As Possible
- e.g.,
  - Center
  - ListView
  - Container (null width and height)
#### Same Size if Possible
- e.g.,
  - Transform
  - Opacity
  - Container (non null width or height)
#### Fixed Size if Possible
- e.g., 
  - Image
  - Text
## 6.1. BoxConstraints
- Passed to Container.constraints
- Can specify max/min width/height

## LayoutBuilder 
- Provides parent constraints to child
- Builds at layout time

## FractionallySizedBox
- Provides percentage of parent size to child

```
ParentWidget(
  child: FractionallySizedBox(
        widthFactor: 0.5,
        heightFactor: 0.5,
        child: Container(
          // this container won't be larger than
          // half of its parent size
        ),
  )
)
```

# 7. Layout
## 7.1. SafeArea
- Should exist at top level
  - for iPhone notches etc
## 7.2. Container
- Expands to fit parent 

## 7.3. Aligning
- Align
- Center

## 7.4. SizedBox
- Fixed size or
- unconstrained in height or width if it is null

## SliverGrid
- Need parent to specify layout
- Does not depend on size of children

## 7.6. Performance
### 7.6.1. build() is costly
- avoid repetitive build in complex layouts
- PROBLEM: top level stateless widget has a build method
  - within build method there are a bunch of widgets
  - whenever build method is called again all widgets are rebuilt
- SOLUTIONS:
  - when calling widget which doesnt change, declare as constant
  - extend widget as stateless widget, which has its own build method
    - widget will only be built once

### 7.6.2. itemExtend for ListView 
- when action triggers jumping to other end of the list
# Weird Problems
## Vertical Dividers not showing

# 8. Scrolling
## 8.1. ListView

## 8.2. ListView.builder()

## 8.3. ListView.custom()
# 9. Animations
Animation Types:
## 9.1. Drawing-based
- Use external framework and export to flutter (e..g, Flare, Lottie)
## 9.2. Code-based
### 9.2.1. Implicit (AnimatedFoo)
#### 9.2.1.1. BuiltIn
#### 9.2.1.2. Custom: TweenAnimationBuilder
### 9.2.2. Explicit (FooTransition)
- Requires AnimationController, and managing life cycle inside stateful widget
Used if any of the following is true:
- Repeats forever
- Discontinuous animation
- Multiple widgets animating together
#### 9.2.2.1. Built In
#### 9.2.2.2. Custom
##### 9.2.2.2.1. AnimatedWidget
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
##### 9.2.2.2.2. CustomPainter
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
##### 9.2.2.2.3. AnimatedBuilder
- Part of parent widget




# 10. Asynchronous Programming
Completion of other work while waiting for a complex operation to finish.
The complex operation is usually set to be the asynchronous function.

## 10.1. Terminology
- Synchronous operation: Blocks other operations from executing till it completes
- Synchronous function: Only syncOp
- Asynchronous operation: Allows other operations to execute before it completes
- Asynchronous function: >=1 asyncOp


## 10.2. futures
- `future`: instance of Future class
  - Represents result of asyncOp:
    - Uncompleted, waiting for asyncOp to finish or throw an error
    - Completed, returns value for successful asyncOp, or throw error
    - 
- `Future<ReturnValueType>`: class returning future value of ReturnValueType
  -  

## 10.3. async
## 10.4. await

# 11. Generators (*)
- Function which returns multiple values
- e.g., sync function returns `int`, async function returns `Future<int>`, sync generator returns `Iterable<int>`, async generator returns `Stream<int>`
- Uses `yield` instead of `return`


# 12. Inheritance
## 12.1. extends
- making all properties, variables, functions of superclass  available to subclass
## 12.2. implements
- making type of superclass available to subclass
- all functions must be implemented/overridden 
## 12.3. with (mixin)
- making properties, variables, functions of a different class available to a subclass 


# 13. Variable Types
## 13.1. Lists
### 13.1.1. Constructors
#### 13.1.1.1. .empty()
- 
#### 13.1.1.2. .filled()
- List of given length with fixed value at each position
#### 13.1.1.3. .from()
- List containing all elements
#### 13.1.1.4. .generate()
- List of given length with values from a generator
#### 13.1.1.5. .of()
- List from elements
#### 13.1.1.6. .unmodifiable()
- Unmodifiable list containing all elements

## 13.2. Modifiers
### 13.2.1. static
- modifies members of a class (variables, functions)
  - only affects the class, not on instances of the class 
### 13.2.2. final
- modifies variables (`var, int, double`)
  - must be assigned on init
  - shallow immutability: e.g., final collection members can be mutable, collection itself is immutable
### 13.2.3. const
- modifies values and objects (`[1,2,3], Point(2,3)`)
  - compile time constant: state can be determined at compile time and is then frozen (e.g., `1+2` is compile time const, `DateTime.now()` is not)
  - deep (transitive) immutability: e.g., const collection members are immutable, recursively
  - canonicalised values and objects: all assignments of the const value/object will refer to the same instance