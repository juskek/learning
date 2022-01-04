- [1. Architecture](#1-architecture)
  - [1.1. main](#11-main)
  - [1.2. routes](#12-routes)
  - [1.3. styles](#13-styles)
  - [1.4. index](#14-index)
- [2. State, Widgets and Elements](#2-state-widgets-and-elements)
  - [2.1. State Definition](#21-state-definition)
  - [2.2. Stateless Widget](#22-stateless-widget)
  - [2.3. Stateful Widget](#23-stateful-widget)
  - [2.4. Lifecycles](#24-lifecycles)
- [3. Trees](#3-trees)
  - [3.1. Widget Tree (WT)](#31-widget-tree-wt)
  - [3.2. Element Tree (ET)](#32-element-tree-et)
- [Keys](#keys)
  - [When to use](#when-to-use)
  - [Where to use](#where-to-use)
  - [Which to use](#which-to-use)
  - [Mechanism](#mechanism)
- [4. Syntax](#4-syntax)
  - [4.1. Operators](#41-operators)
    - [4.1.1. Comparisons](#411-comparisons)
      - [4.1.1.1. Assignment (=)](#4111-assignment-)
      - [4.1.1.2. Equality (==)](#4112-equality-)
      - [4.1.1.3. Identity (===, or identical(a,b))](#4113-identity--or-identicalab)
  - [4.2. Conditional](#42-conditional)
    - [4.2.1. if null (??)](#421-if-null-)
  - [4.3. Cascade Notation](#43-cascade-notation)
  - [4.4. Initialiser List (:)](#44-initialiser-list-)
  - [4.5. Objects & Classes](#45-objects--classes)
    - [4.5.1. Object Constructors](#451-object-constructors)
- [5. Sound Null Safety](#5-sound-null-safety)
  - [5.1. Unsound null safety](#51-unsound-null-safety)
  - [5.2. Disable sound null safety](#52-disable-sound-null-safety)
- [6. Scoping](#6-scoping)
  - [6.1. Lexical Scoping](#61-lexical-scoping)
- [7. Syntax](#7-syntax)
  - [7.1. Arrow](#71-arrow)
  - [7.2. Closure/Inline Functions](#72-closureinline-functions)
  - [7.3. Anonymous Multiline Function](#73-anonymous-multiline-function)
  - [7.4. Conditional Rendering](#74-conditional-rendering)
    - [7.4.1. Binary if](#741-binary-if)
    - [7.4.2. Ternary Operator](#742-ternary-operator)
    - [7.4.3. Multiple if](#743-multiple-if)
    - [7.4.4. Spread Operator](#744-spread-operator)
- [8. Sizing](#8-sizing)
  - [8.1. Sizes, Constraints and Positions](#81-sizes-constraints-and-positions)
    - [8.1.1. Rules](#811-rules)
    - [8.1.2. Process](#812-process)
    - [8.1.3. Limitations](#813-limitations)
    - [8.1.4. Mechanisms](#814-mechanisms)
    - [8.1.5. Types of Constraints](#815-types-of-constraints)
      - [8.1.5.1. As Big As Possible](#8151-as-big-as-possible)
      - [8.1.5.2. Same Size if Possible](#8152-same-size-if-possible)
      - [8.1.5.3. Fixed Size if Possible](#8153-fixed-size-if-possible)
  - [8.2. BoxConstraints](#82-boxconstraints)
  - [8.3. LayoutBuilder](#83-layoutbuilder)
  - [8.4. FractionallySizedBox](#84-fractionallysizedbox)
- [9. Layout](#9-layout)
  - [9.1. SafeArea](#91-safearea)
  - [9.2. Container](#92-container)
  - [9.3. Aligning](#93-aligning)
  - [9.4. SizedBox](#94-sizedbox)
  - [9.5. SliverGrid](#95-slivergrid)
  - [9.6. Performance](#96-performance)
    - [9.6.1. build() is costly](#961-build-is-costly)
    - [9.6.2. itemExtend for ListView](#962-itemextend-for-listview)
- [10. Weird Problems](#10-weird-problems)
  - [10.1. Vertical Dividers not showing](#101-vertical-dividers-not-showing)
- [11. Scrolling](#11-scrolling)
  - [11.1. ListView](#111-listview)
  - [11.2. ListView.builder()](#112-listviewbuilder)
  - [11.3. ListView.custom()](#113-listviewcustom)
- [12. Animations](#12-animations)
  - [12.1. Drawing-based](#121-drawing-based)
  - [12.2. Code-based](#122-code-based)
    - [12.2.1. Implicit (AnimatedFoo)](#1221-implicit-animatedfoo)
      - [12.2.1.1. BuiltIn](#12211-builtin)
      - [12.2.1.2. Custom: TweenAnimationBuilder](#12212-custom-tweenanimationbuilder)
    - [12.2.2. Explicit (FooTransition)](#1222-explicit-footransition)
      - [12.2.2.1. Built In](#12221-built-in)
      - [12.2.2.2. Custom](#12222-custom)
        - [12.2.2.2.1. AnimatedWidget](#122221-animatedwidget)
        - [12.2.2.2.2. CustomPainter](#122222-custompainter)
        - [12.2.2.2.3. AnimatedBuilder](#122223-animatedbuilder)
- [13. Asynchronous Programming](#13-asynchronous-programming)
  - [13.1. Terminology](#131-terminology)
  - [13.2. futures](#132-futures)
  - [13.3. async](#133-async)
  - [13.4. await](#134-await)
- [14. Generators (*)](#14-generators-)
- [15. Inheritance](#15-inheritance)
  - [15.1. extends](#151-extends)
  - [15.2. implements](#152-implements)
  - [15.3. with (mixin)](#153-with-mixin)
- [16. Variable Types](#16-variable-types)
  - [16.1. Lists](#161-lists)
    - [16.1.1. Constructors](#1611-constructors)
      - [16.1.1.1. .empty()](#16111-empty)
      - [16.1.1.2. .filled()](#16112-filled)
      - [16.1.1.3. .from()](#16113-from)
      - [16.1.1.4. .generate()](#16114-generate)
      - [16.1.1.5. .of()](#16115-of)
      - [16.1.1.6. .unmodifiable()](#16116-unmodifiable)
  - [16.2. Modifiers](#162-modifiers)
    - [16.2.1. static](#1621-static)
    - [16.2.2. final](#1622-final)
    - [16.2.3. const](#1623-const)

# 1. Architecture
## 1.1. main
## 1.2. routes
## 1.3. styles
## 1.4. index

# 2. State, Widgets and Elements
## 2.1. State Definition
- Info within a widget which is read for building

## 2.2. Stateless Widget
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
## 2.3. Stateful Widget
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
## 2.4. Lifecycles

# 3. Trees
## 3.1. Widget Tree (WT)
- How, what and when to show on screen
- Creates elements to mount in element tree
## 3.2. Element Tree (ET)
- What is currently shown on screen

# Keys
## When to use
- When state needs to be preserved in widget tree
  - e.g., Rearranging items in a list
## Where to use
- Top of widget subtree which is being rearranged
  - e.g., if items in list have padding, key should be assigned to padding

## Which to use
- Depends on state to be preserved
- ValueKey
  - When state of each widget being rearranged is unique
- UniqueKey
  - When state of widgets may not be unique
- ObjectKey
  - When state attributes may be common amongst widgets, but combination of them is unique
- PageStorageKey
  - Stores scroll location
- GlobalKey
  - When widget needs to change parents without losing state
    - e.g., same widget on two different pages
  - When need to access info about widget in different part of the tree
    - e.g., do not want other widgets to be able to access password widget
  - NOTE: usually better way to avoid GlobalKey
    - e.g., InheritedWidget, redux/block pattern
- DO NOT
  - Set random number in key as everytime widget is rebuilt, a number different from element key is generated, making it redundant
## Mechanism
- Flutter's element-widget matching mechanism checks for same type 
- Rearranging Stateless Widgets
  1. Stateles
- Rearranging Stateful Widgets
# 4. Syntax
## 4.1. Operators
### 4.1.1. Comparisons
#### 4.1.1.1. Assignment (=)
- Assign value to variable
#### 4.1.1.2. Equality (==)
- Check if two variables/objects are equal
#### 4.1.1.3. Identity (===, or identical(a,b))
- Check if two variables/objects refer to the same instance/object
## 4.2. Conditional
### 4.2.1. if null (??)
## 4.3. Cascade Notation
Prevents repeating target for several call methods on same object.
```
List list = [];
list.add(color1);
list.add(color2);

list
  ..add(color1)
  ..add(color2);
```
## 4.4. Initialiser List (:)
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

## 4.5. Objects & Classes
### 4.5.1. Object Constructors
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
# 5. Sound Null Safety
- Types are non-nullable by default
- Variables cannot contain `null` unless allowed to:
  - To allow null values, add `?` after type declaration
```
    int nonNullableInt = 1; // cannot be null
    int? aNullableInt = null; 
```
- Non-null assertion operator variable!.method tells the compiler that the value of the variable will not be null during runtime, and hence methods can be called on the variable.
## 5.1. Unsound null safety
- Mixed-version programme
- Some files with sound NS and some with unsound NS
- Runtime null only occurs from leakage of unsound to sound code

## 5.2. Disable sound null safety
`flutter run --no-sound-null-safety`


# 6. Scoping
## 6.1. Lexical Scoping
Inner function has access to parent variables



# 7. Syntax
## 7.1. Arrow 
```
    => expression,
    // is equivalent to 
    {return expression;},
```

## 7.2. Closure/Inline Functions
```
    () => expression
    
    // is equivalent to
    function () {
        return expression
    }
```

## 7.3. Anonymous Multiline Function
```
  () {expression}
  // is equivalent to
  function () {
      return expression
  }
```

## 7.4. Conditional Rendering
### 7.4.1. Binary if
`if (Responsive.isDesktop()) Text('Desktop)`
### 7.4.2. Ternary Operator
`Responsive.isDesktop() ? Text('Desktop') : null`

### 7.4.3. Multiple if
```
  (() {
    // your code here
  }())
```
### 7.4.4. Spread Operator
- Can be used to return multiple widgets
`if (Responsive.isDesktop()) ...[
    Text('Desktop')
    Text('Mode')
  ]
`

# 8. Sizing
## 8.1. Sizes, Constraints and Positions
### 8.1.1. Rules
  - Constraints go down
  - Sizes go up
  - Parent sets position
### 8.1.2. Process 
For an arbitrary widget X, its parent Y, and its children Z
1. Y passes its constraints down to X
   - min/max height/width
2. X passes its constraints down to Z
3. X asks Z what size they are
   - width/height
4. X sets positions of Z
5. X tells Y its final size 

### 8.1.3. Limitations
- Size defined in widget only within constraints of parent
- Widget does not know/decide its position
- Defining alignment must be specific or child size may be ignored

### 8.1.4. Mechanisms
- RenderBox
  - Underlying object used to render widgets

### 8.1.5. Types of Constraints
#### 8.1.5.1. As Big As Possible
- e.g.,
  - Center
  - ListView
  - Container (null width and height)
#### 8.1.5.2. Same Size if Possible
- e.g.,
  - Transform
  - Opacity
  - Container (non null width or height)
#### 8.1.5.3. Fixed Size if Possible
- e.g., 
  - Image
  - Text
## 8.2. BoxConstraints
- Passed to Container.constraints
- Can specify max/min width/height

## 8.3. LayoutBuilder 
- Provides parent constraints to child
- Builds at layout time

## 8.4. FractionallySizedBox
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

# 9. Layout
## 9.1. SafeArea
- Should exist at top level
  - for iPhone notches etc
## 9.2. Container
- Expands to fit parent 

## 9.3. Aligning
- Align
- Center

## 9.4. SizedBox
- Fixed size or
- unconstrained in height or width if it is null

## 9.5. SliverGrid
- Need parent to specify layout
- Does not depend on size of children

## 9.6. Performance
### 9.6.1. build() is costly
- avoid repetitive build in complex layouts
- PROBLEM: top level stateless widget has a build method
  - within build method there are a bunch of widgets
  - whenever build method is called again all widgets are rebuilt
- SOLUTIONS:
  - when calling widget which doesnt change, declare as constant
  - extend widget as stateless widget, which has its own build method
    - widget will only be built once

### 9.6.2. itemExtend for ListView 
- when action triggers jumping to other end of the list
# 10. Weird Problems
## 10.1. Vertical Dividers not showing

# 11. Scrolling
## 11.1. ListView

## 11.2. ListView.builder()

## 11.3. ListView.custom()
# 12. Animations
Animation Types:
## 12.1. Drawing-based
- Use external framework and export to flutter (e..g, Flare, Lottie)
## 12.2. Code-based
### 12.2.1. Implicit (AnimatedFoo)
#### 12.2.1.1. BuiltIn
#### 12.2.1.2. Custom: TweenAnimationBuilder
### 12.2.2. Explicit (FooTransition)
- Requires AnimationController, and managing life cycle inside stateful widget
Used if any of the following is true:
- Repeats forever
- Discontinuous animation
- Multiple widgets animating together
#### 12.2.2.1. Built In
#### 12.2.2.2. Custom
##### 12.2.2.2.1. AnimatedWidget
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
##### 12.2.2.2.2. CustomPainter
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
##### 12.2.2.2.3. AnimatedBuilder
- Part of parent widget




# 13. Asynchronous Programming
Completion of other work while waiting for a complex operation to finish.
The complex operation is usually set to be the asynchronous function.

## 13.1. Terminology
- Synchronous operation: Blocks other operations from executing till it completes
- Synchronous function: Only syncOp
- Asynchronous operation: Allows other operations to execute before it completes
- Asynchronous function: >=1 asyncOp


## 13.2. futures
- `future`: instance of Future class
  - Represents result of asyncOp:
    - Uncompleted, waiting for asyncOp to finish or throw an error
    - Completed, returns value for successful asyncOp, or throw error
    - 
- `Future<ReturnValueType>`: class returning future value of ReturnValueType
  -  

## 13.3. async
## 13.4. await

# 14. Generators (*)
- Function which returns multiple values
- e.g., sync function returns `int`, async function returns `Future<int>`, sync generator returns `Iterable<int>`, async generator returns `Stream<int>`
- Uses `yield` instead of `return`


# 15. Inheritance
## 15.1. extends
- making all properties, variables, functions of superclass  available to subclass
## 15.2. implements
- making type of superclass available to subclass
- all functions must be implemented/overridden 
## 15.3. with (mixin)
- making properties, variables, functions of a different class available to a subclass 


# 16. Variable Types
## 16.1. Lists
### 16.1.1. Constructors
#### 16.1.1.1. .empty()
- 
#### 16.1.1.2. .filled()
- List of given length with fixed value at each position
#### 16.1.1.3. .from()
- List containing all elements
#### 16.1.1.4. .generate()
- List of given length with values from a generator
#### 16.1.1.5. .of()
- List from elements
#### 16.1.1.6. .unmodifiable()
- Unmodifiable list containing all elements

## 16.2. Modifiers
### 16.2.1. static
- modifies members of a class (variables, functions)
  - only affects the class, not on instances of the class 
### 16.2.2. final
- modifies variables (`var, int, double`)
  - must be assigned on init
  - shallow immutability: e.g., final collection members can be mutable, collection itself is immutable
### 16.2.3. const
- modifies values and objects (`[1,2,3], Point(2,3)`)
  - compile time constant: state can be determined at compile time and is then frozen (e.g., `1+2` is compile time const, `DateTime.now()` is not)
  - deep (transitive) immutability: e.g., const collection members are immutable, recursively
  - canonicalised values and objects: all assignments of the const value/object will refer to the same instance