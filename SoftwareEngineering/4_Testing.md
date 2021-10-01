
# Testing
## Tenets
1. Understanding big picture and priorities
2. Understanding interactions of components within big picture
3. Structured approach (mindmap)
4. Practicality (reasonable testing plans)

## Process
1. Who will use it and why?
2. What are the use cases?
3. What are the bounds of use?
4. What are the stress/failure conditions?
5. How will testing be performed?
   - Manual vs Automated
   - Black Box vs WhiteBox

## Testing Types
### Manual
### Automated
#### Smoke Testing
#### Integration
#### Unit 
- Isolate
  - Test one class at a time
  - Test results should not depend on other classes or tests
    - Use `Setup` and `TearDown` features
  - Tests should be able to run offline
- AAA Rule
  - Arrange: Set up variables to enable test 
  - Act: Call method
  - Assert: Verify result
- Simplicity before complexity
  - Simplest functionalities first
  - Edge and boundary cases after
- Test across boundaries
  - e.g., one second before and after midnight, one point before and after a line
- Test entire spectrum (if possible)
  - e.g., enum tests
- Cover every code path (if possible)
- Write tests for bugs before fixing them
  - If bug is found, write tests that reveals it so that it can be quickly fixed in the future 
- Name tests clearly
- Test raised exceptions
- Avoid checking boolean conditions
  - Using `Assert.AreEqual(x,y)` will provide more information than `Assert.IsTrue(x==y)`
- Run tests while writing code
  - Better as part of build process