

# 1. Architecture
## 1.1. main
## 1.2. routes
## 1.3. styles
## 1.4. index
# Syntax
## Cascade Notation
Prevents repeating target for several call methods on same object.
```
List list = [];
list.add(color1);
list.add(color2);

list
  ..add(color1)
  ..add(color2);
```
## Initialiser List (:)
Used to:
- Initialise list of expressions that can:
  - access constructor parameters
  - assign to instance fields (even final instance fields!)
- Call other constructors
  - e.g., superclass
- Assert constructor parameters
NOTE:
- Initialiser list is exeuted before constructor body

## Objects & Classes
### Object Constructors
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
# 2. Sound Null Safety
- Types are non-nullable by default
- Variables cannot contain `null` unless allowed to:
  - To allow null values, add `?` after type declaration
```
    int nonNullableInt = 1; // cannot be null
    int? aNullableInt = null; 
```
## 2.1. Unsound null safety
- Mixed-version programme
- Some files with sound NS and some with unsound NS
- Runtime null only occurs from leakage of unsound to sound code

## 2.2. Disable sound null safety
`flutter run --no-sound-null-safety`


# 3. Scoping
## 3.1. Lexical Scoping
Inner function has access to parent variables



# 4. Syntax
## 4.1. Arrow 
```
    => expression,
    // is equivalent to 
    {return expression;},
```

## 4.2. Closure/Inline Functions
```
    () => expression
    // is equivalent to
    function () {
        return expression
    }
```

# 5. Animations
Animation Types:
## 5.1. Drawing-based
- Use external framework and export to flutter (e..g, Flare, Lottie)
## 5.2. Code-based
### 5.2.1. Implicit (AnimatedFoo)
#### 5.2.1.1. BuiltIn
#### 5.2.1.2. Custom: TweenAnimationBuilder
### 5.2.2. Explicit (FooTransition)
- Requires AnimationController, and managing life cycle inside stateful widget
Used if any of the following is true:
- Repeats forever
- Discontinuous animation
- Multiple widgets animating together
#### 5.2.2.1. Built In
#### 5.2.2.2. Custom
##### 5.2.2.2.1. AnimatedWidget
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
##### CustomPainter
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
##### 5.2.2.2.2. AnimatedBuilder
- Part of parent widget




# 6. Asynchronous Programming
Completion of other work while waiting for a complex operation to finish.
The complex operation is usually set to be the asynchronous function.

## 6.1. Terminology
- Synchronous operation: Blocks other operations from executing till it completes
- Synchronous function: Only syncOp
- Asynchronous operation: Allows other operations to execute before it completes
- Asynchronous function: >=1 asyncOp


## 6.2. futures
- `future`: instance of Future class
  - Represents result of asyncOp:
    - Uncompleted, waiting for asyncOp to finish or throw an error
    - Completed, returns value for successful asyncOp, or throw error
    - 
- `Future<ReturnValueType>`: class returning future value of ReturnValueType
  -  

## 6.3. async
## 6.4. await
