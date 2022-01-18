- [1. Architecture](#1-architecture)
  - [State Management](#state-management)
    - [UI Approach](#ui-approach)
      - [Declarative](#declarative)
      - [Imperative](#imperative)
    - [State Types](#state-types)
      - [Ephemeral State](#ephemeral-state)
      - [App State](#app-state)
    - [State Management Approaches](#state-management-approaches)
      - [Provider](#provider)
      - [Redux](#redux)
      - [Rx](#rx)
      - [Hooks](#hooks)
- [2. State, Widgets and Elements](#2-state-widgets-and-elements)
  - [2.1. State Definition](#21-state-definition)
  - [2.2. StatelessWidget](#22-statelesswidget)
  - [2.3. StatefulWidget](#23-statefulwidget)
  - [2.4. InheritedWidget](#24-inheritedwidget)
  - [2.5. Lifecycles](#25-lifecycles)
- [3. Trees](#3-trees)
  - [3.1. Widget Tree (WT)](#31-widget-tree-wt)
  - [3.2. Element Tree (ET)](#32-element-tree-et)
- [4. Keys](#4-keys)
  - [4.1. When to use](#41-when-to-use)
  - [4.2. Where to use](#42-where-to-use)
  - [4.3. Which to use](#43-which-to-use)
  - [4.4. Mechanism](#44-mechanism)
- [5. Syntax](#5-syntax)
  - [5.1. Operators](#51-operators)
    - [5.1.1. Comparisons](#511-comparisons)
      - [5.1.1.1. Assignment (=)](#5111-assignment-)
      - [5.1.1.2. Equality (==)](#5112-equality-)
      - [5.1.1.3. Identity (===, or identical(a,b))](#5113-identity--or-identicalab)
  - [5.2. Conditional](#52-conditional)
    - [5.2.1. if null (??)](#521-if-null-)
  - [5.3. Cascade Notation](#53-cascade-notation)
  - [5.4. Initialiser List (:)](#54-initialiser-list-)
  - [5.5. Objects & Classes](#55-objects--classes)
    - [5.5.1. Object Constructors](#551-object-constructors)
- [6. Sound Null Safety](#6-sound-null-safety)
  - [6.1. Unsound null safety](#61-unsound-null-safety)
  - [6.2. Disable sound null safety](#62-disable-sound-null-safety)
- [7. Scoping](#7-scoping)
  - [7.1. Lexical Scoping](#71-lexical-scoping)
- [8. Syntax](#8-syntax)
  - [8.1. Arrow](#81-arrow)
  - [8.2. Closure/Inline Functions](#82-closureinline-functions)
  - [8.3. Anonymous Multiline Function](#83-anonymous-multiline-function)
  - [8.4. Conditional Rendering](#84-conditional-rendering)
    - [8.4.1. Binary if](#841-binary-if)
    - [8.4.2. Ternary Operator](#842-ternary-operator)
    - [8.4.3. Multiple if](#843-multiple-if)
    - [8.4.4. Spread Operator](#844-spread-operator)
- [9. Sizing](#9-sizing)
  - [9.1. Sizes, Constraints and Positions](#91-sizes-constraints-and-positions)
    - [9.1.1. Rules](#911-rules)
    - [9.1.2. Process](#912-process)
    - [9.1.3. Limitations](#913-limitations)
    - [9.1.4. Mechanisms](#914-mechanisms)
    - [9.1.5. Types of Constraints](#915-types-of-constraints)
      - [9.1.5.1. As Big As Possible](#9151-as-big-as-possible)
      - [9.1.5.2. Same Size if Possible](#9152-same-size-if-possible)
      - [9.1.5.3. Fixed Size if Possible](#9153-fixed-size-if-possible)
  - [9.2. BoxConstraints](#92-boxconstraints)
  - [9.3. LayoutBuilder](#93-layoutbuilder)
  - [9.4. FractionallySizedBox](#94-fractionallysizedbox)
- [10. Layout](#10-layout)
  - [10.1. SafeArea](#101-safearea)
  - [10.2. Container](#102-container)
  - [10.3. Aligning](#103-aligning)
  - [10.4. SizedBox](#104-sizedbox)
  - [10.5. SliverGrid](#105-slivergrid)
  - [10.6. Performance](#106-performance)
    - [10.6.1. build() is costly](#1061-build-is-costly)
    - [10.6.2. itemExtend for ListView](#1062-itemextend-for-listview)
- [11. Weird Problems](#11-weird-problems)
  - [11.1. Vertical Dividers not showing](#111-vertical-dividers-not-showing)
- [12. Scrolling](#12-scrolling)
  - [12.1. ListView](#121-listview)
  - [12.2. ListView.builder()](#122-listviewbuilder)
  - [12.3. ListView.custom()](#123-listviewcustom)
- [13. Animations](#13-animations)
  - [13.1. Drawing-based](#131-drawing-based)
  - [13.2. Code-based](#132-code-based)
    - [13.2.1. Implicit (AnimatedFoo)](#1321-implicit-animatedfoo)
      - [13.2.1.1. BuiltIn](#13211-builtin)
      - [13.2.1.2. Custom: TweenAnimationBuilder](#13212-custom-tweenanimationbuilder)
    - [13.2.2. Explicit (FooTransition)](#1322-explicit-footransition)
      - [13.2.2.1. Built In](#13221-built-in)
      - [13.2.2.2. Custom](#13222-custom)
        - [13.2.2.2.1. AnimatedWidget](#132221-animatedwidget)
        - [13.2.2.2.2. CustomPainter](#132222-custompainter)
        - [13.2.2.2.3. AnimatedBuilder](#132223-animatedbuilder)
- [14. Asynchronous Programming](#14-asynchronous-programming)
  - [14.1. Terminology](#141-terminology)
  - [14.2. futures](#142-futures)
  - [14.3. async](#143-async)
  - [14.4. await](#144-await)
- [15. Generators (*)](#15-generators-)
- [16. Inheritance](#16-inheritance)
  - [16.1. extends](#161-extends)
  - [16.2. implements](#162-implements)
  - [16.3. with (mixin)](#163-with-mixin)
- [17. Variable Types](#17-variable-types)
  - [17.1. Lists](#171-lists)
    - [17.1.1. Constructors](#1711-constructors)
      - [17.1.1.1. .empty()](#17111-empty)
      - [17.1.1.2. .filled()](#17112-filled)
      - [17.1.1.3. .from()](#17113-from)
      - [17.1.1.4. .generate()](#17114-generate)
      - [17.1.1.5. .of()](#17115-of)
      - [17.1.1.6. .unmodifiable()](#17116-unmodifiable)
  - [17.2. Modifiers](#172-modifiers)
    - [17.2.1. static](#1721-static)
    - [17.2.2. final](#1722-final)
    - [17.2.3. const](#1723-const)

# 1. Architecture
## State Management
### UI Approach
#### Declarative
- what to show from state
  - e.g., in Dart/Flutter:
```
return Center(Text('Hello World'))
```
#### Imperative
- how to show from state
  - e.g., in Java/Android Ice Cream Sandwich:
```
setContentView

return  <TextView
       android:layout_width="wrap_content"
       android:layout_height="wrap_content"
       android:text="Hello World!"
       app:layout_constraintBottom_toBottomOf="parent"
       app:layout_constraintLeft_toLeftOf="parent"
       app:layout_constraintRight_toRightOf="parent"
       app:layout_constraintTop_toTopOf="parent" />
```
### State Types
#### Ephemeral State
- Definition
  - UI or local state
  - Contained in single widget
  - e.g., animation progress, current page in pageview
- Use cases
  - Does not change in complex ways
  - Other parts of widget tree seldom require access 
- Methods
  - Stateful widget
#### App State
- Definition
  - Shared across many widgets
  - e.g., user prefs, login info, notifications, shopping cart, read/unread articles
- Use cases
  - Required by many widgets
  - Preserve some state between session, e.g., current page in page view
### State Management Approaches

#### Provider
- Recommended if no strong reason to choose another approach
#### Redux
#### Rx
#### Hooks
# 2. State, Widgets and Elements
## 2.1. State Definition
- Info within a widget which is read for building

## 2.2. StatelessWidget
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
## 2.3. StatefulWidget
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
## 2.4. InheritedWidget
- Allows sub widgets to access InheritedWidget state from anywhere in the tree without passing state down through multiple widgets

## 2.5. Lifecycles

# 3. Trees
## 3.1. Widget Tree (WT)
- How, what and when to show on screen
- Creates elements to mount in element tree
## 3.2. Element Tree (ET)
- What is currently shown on screen

# 4. Keys
## 4.1. When to use
- When state needs to be preserved in widget tree
  - e.g., Rearranging items in a list
## 4.2. Where to use
- Top of widget subtree which is being rearranged
  - e.g., if items in list have padding, key should be assigned to padding

## 4.3. Which to use
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
## 4.4. Mechanism
- Flutter's element-widget matching mechanism checks for same type 
- Rearranging Stateless Widgets
  1. Stateless
- Rearranging Stateful Widgets
# 5. Syntax
## 5.1. Operators
### 5.1.1. Comparisons
#### 5.1.1.1. Assignment (=)
- Assign value to variable
#### 5.1.1.2. Equality (==)
- Check if two variables/objects are equal
#### 5.1.1.3. Identity (===, or identical(a,b))
- Check if two variables/objects refer to the same instance/object
## 5.2. Conditional
### 5.2.1. if null (??)
## 5.3. Cascade Notation
Prevents repeating target for several call methods on same object.
```
List list = [];
list.add(color1);
list.add(color2);

list
  ..add(color1)
  ..add(color2);
```
## 5.4. Initialiser List (:)
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

## 5.5. Objects & Classes
### 5.5.1. Object Constructors
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
# 6. Sound Null Safety
- Types are non-nullable by default
- Variables cannot contain `null` unless allowed to:
  - To allow null values, add `?` after type declaration
```
    int nonNullableInt = 1; // cannot be null
    int? aNullableInt = null; 
```
- Non-null assertion operator variable!.method tells the compiler that the value of the variable will not be null during runtime, and hence methods can be called on the variable.
## 6.1. Unsound null safety
- Mixed-version programme
- Some files with sound NS and some with unsound NS
- Runtime null only occurs from leakage of unsound to sound code

## 6.2. Disable sound null safety
`flutter run --no-sound-null-safety`


# 7. Scoping
## 7.1. Lexical Scoping
Inner function has access to parent variables



# 8. Syntax
## 8.1. Arrow 
```
    => expression,
    // is equivalent to 
    {return expression;},
```

## 8.2. Closure/Inline Functions
```
    () => expression
    
    // is equivalent to
    function () {
        return expression
    }
```

## 8.3. Anonymous Multiline Function
```
  () {expression}
  // is equivalent to
  function () {
      return expression
  }
```

## 8.4. Conditional Rendering
### 8.4.1. Binary if
`if (Responsive.isDesktop()) Text('Desktop)`
### 8.4.2. Ternary Operator
`Responsive.isDesktop() ? Text('Desktop') : null`

### 8.4.3. Multiple if
```
  (() {
    // your code here
  }())
```
### 8.4.4. Spread Operator
- Can be used to return multiple widgets
`if (Responsive.isDesktop()) ...[
    Text('Desktop')
    Text('Mode')
  ]
`

# 9. Sizing
## 9.1. Sizes, Constraints and Positions
### 9.1.1. Rules
  - Constraints go down
  - Sizes go up
  - Parent sets position
### 9.1.2. Process 
For an arbitrary widget X, its parent Y, and its children Z
1. Y passes its constraints down to X
   - min/max height/width
2. X passes its constraints down to Z
3. X asks Z what size they are
   - width/height
4. X sets positions of Z
5. X tells Y its final size 

### 9.1.3. Limitations
- Size defined in widget only within constraints of parent
- Widget does not know/decide its position
- Defining alignment must be specific or child size may be ignored

### 9.1.4. Mechanisms
- RenderBox
  - Underlying object used to render widgets

### 9.1.5. Types of Constraints
#### 9.1.5.1. As Big As Possible
- e.g.,
  - Center
  - ListView
  - Container (null width and height)
#### 9.1.5.2. Same Size if Possible
- e.g.,
  - Transform
  - Opacity
  - Container (non null width or height)
#### 9.1.5.3. Fixed Size if Possible
- e.g., 
  - Image
  - Text
## 9.2. BoxConstraints
- Passed to Container.constraints
- Can specify max/min width/height

## 9.3. LayoutBuilder 
- Provides parent constraints to child
- Builds at layout time

## 9.4. FractionallySizedBox
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

# 10. Layout
## 10.1. SafeArea
- Should exist at top level
  - for iPhone notches etc
## 10.2. Container
- Expands to fit parent 

## 10.3. Aligning
- Align
- Center

## 10.4. SizedBox
- Fixed size or
- unconstrained in height or width if it is null

## 10.5. SliverGrid
- Need parent to specify layout
- Does not depend on size of children

## 10.6. Performance
### 10.6.1. build() is costly
- avoid repetitive build in complex layouts
- PROBLEM: top level stateless widget has a build method
  - within build method there are a bunch of widgets
  - whenever build method is called again all widgets are rebuilt
- SOLUTIONS:
  - when calling widget which doesnt change, declare as constant
  - extend widget as stateless widget, which has its own build method
    - widget will only be built once

### 10.6.2. itemExtend for ListView 
- when action triggers jumping to other end of the list
# 11. Weird Problems
## 11.1. Vertical Dividers not showing

# 12. Scrolling
## 12.1. ListView

## 12.2. ListView.builder()

## 12.3. ListView.custom()
# 13. Animations
Animation Types:
## 13.1. Drawing-based
- Use external framework and export to flutter (e..g, Flare, Lottie)
## 13.2. Code-based
### 13.2.1. Implicit (AnimatedFoo)
#### 13.2.1.1. BuiltIn
#### 13.2.1.2. Custom: TweenAnimationBuilder
### 13.2.2. Explicit (FooTransition)
- Requires AnimationController, and managing life cycle inside stateful widget
Used if any of the following is true:
- Repeats forever
- Discontinuous animation
- Multiple widgets animating together
#### 13.2.2.1. Built In
#### 13.2.2.2. Custom
##### 13.2.2.2.1. AnimatedWidget
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
##### 13.2.2.2.2. CustomPainter
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
##### 13.2.2.2.3. AnimatedBuilder
- Part of parent widget




# 14. Asynchronous Programming
Completion of other work while waiting for a complex operation to finish.
The complex operation is usually set to be the asynchronous function.

## 14.1. Terminology
- Synchronous operation: Blocks other operations from executing till it completes
- Synchronous function: Only syncOp
- Asynchronous operation: Allows other operations to execute before it completes
- Asynchronous function: >=1 asyncOp


## 14.2. futures
- `future`: instance of Future class
  - Represents result of asyncOp:
    - Uncompleted, waiting for asyncOp to finish or throw an error
    - Completed, returns value for successful asyncOp, or throw error
    - 
- `Future<ReturnValueType>`: class returning future value of ReturnValueType
  -  

## 14.3. async
## 14.4. await

# 15. Generators (*)
- Function which returns multiple values
- e.g., sync function returns `int`, async function returns `Future<int>`, sync generator returns `Iterable<int>`, async generator returns `Stream<int>`
- Uses `yield` instead of `return`


# 16. Inheritance
## 16.1. extends
- making all properties, variables, functions of superclass  available to subclass
## 16.2. implements
- making type of superclass available to subclass
- all functions must be implemented/overridden 
## 16.3. with (mixin)
- making properties, variables, functions of a different class available to a subclass 


# 17. Variable Types
## 17.1. Lists
### 17.1.1. Constructors
#### 17.1.1.1. .empty()
- 
#### 17.1.1.2. .filled()
- List of given length with fixed value at each position
#### 17.1.1.3. .from()
- List containing all elements
#### 17.1.1.4. .generate()
- List of given length with values from a generator
#### 17.1.1.5. .of()
- List from elements
#### 17.1.1.6. .unmodifiable()
- Unmodifiable list containing all elements

## 17.2. Modifiers
### 17.2.1. static
- modifies members of a class (variables, functions)
  - only affects the class, not on instances of the class 
### 17.2.2. final
- modifies variables (`var, int, double`)
  - must be assigned on init
  - shallow immutability: e.g., final collection members can be mutable, collection itself is immutable
### 17.2.3. const
- modifies values and objects (`[1,2,3], Point(2,3)`)
  - compile time constant: state can be determined at compile time and is then frozen (e.g., `1+2` is compile time const, `DateTime.now()` is not)
  - deep (transitive) immutability: e.g., const collection members are immutable, recursively
  - canonicalised values and objects: all assignments of the const value/object will refer to the same instance