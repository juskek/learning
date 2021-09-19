- [1. Overview](#1-overview)
- [2. Main Structure](#2-main-structure)
  - [2.1. Workspace](#21-workspace)
  - [2.2. Packages](#22-packages)
  - [2.3. Targets](#23-targets)
    - [2.3.1. Labels](#231-labels)
    - [2.3.2. Rules](#232-rules)
  - [2.4. BUILD programs](#24-build-programs)
    - [2.4.1. Syntax](#241-syntax)
    - [2.4.2. Rule Types](#242-rule-types)
    - [2.4.3. Dependencies](#243-dependencies)
  - [2.5. WORKSPACE](#25-workspace)
    - [2.5.1. Rule Types](#251-rule-types)
  - [2.6. TERMINAL](#26-terminal)
    - [2.6.1. Double Forward Slash `//`](#261-double-forward-slash-)
- [3. Test Structure](#3-test-structure)
  - [3.1. Good Test Design](#31-good-test-design)
    - [3.1.1. Hermetic](#311-hermetic)
    - [3.1.2. Deterministic](#312-deterministic)
    - [3.1.3. Reentrant](#313-reentrant)
  - [3.2. Testing Roles](#32-testing-roles)
    - [3.2.1. Build System](#321-build-system)
    - [3.2.2. Test Runner](#322-test-runner)
      - [3.2.2.1. Initial Conditions](#3221-initial-conditions)
      - [3.2.2.2. Test Sharding](#3222-test-sharding)
    - [3.2.3. Host System](#323-host-system)
- [Terminal Commands](#terminal-commands)

# 1. Overview
- Used to build binaries from source code 

# 2. Main Structure
- Three main components:
1. Workspace
2. Packages
3. Targets
```
// root of main repo, aka @
project_name/
|- projectName/
|   |- BUILD
|   |- package/
|   |- BUILD
|       |- module/
|           |- BUILD
|           |- script.extension
|- external_repository/
|   |- WORKSPACE
|- WORKSPACE
|- BUILD
```
## 2.1. Workspace
- **Workspace** is a directory with a WORKSPACE file
  - Workspace contains nested packages/other repositories

- WORKSPACE file
  - Contains references to external deps for build
  
## 2.2. Packages
- **Package** is a 
  - collection of related files
  - directory with a BUILD file
    - residing beneath top level dir in workspace
  - container, which contains
    - elements/targets, 

## 2.3. Targets
- An element of a package, which can be a 
  - **file**, which can be 
    - source
    - generated
  - **rule**, which specifies r/s between
      - input files
        - e.g., source, generated
      - output files
        - i.e., generated
  - **package group**
    - is a set of packages
    - limits accessibility of certain rules
- The name of a target is its **label**

### 2.3.1. Labels
- Name of a target
  - Uniquely identifies target
- Canonical form:
`@myrepo//app/package:target`
  1. Repository: `@myrepo//`
     - when label used in same repo, abbrev: `//app/package:target`
  2. Unqualified Package: `app/package`
     - qualified when appended to 1. 
     - when label used in same package, abbrev: `:target` (rules) or `target` (files)
  3. Unqualified Target: `:target`
     - qualified when appended to 1. and 2.
     - when target and last component of package has same name, e.g. `//app/name:name`, abbrev: `//app/name`
- Relative labels
  - Refer to targets in other packages
  - 1. and 2. must be specified
- Labels are not package names
  - Labels always start with `//`, package names never do

### 2.3.2. Rules
- Specifies
  - Relationship between inputs and outputs
  - Steps to build outputs
```
rule_name(
    attribute_name = attribute_val,

)
```
## 2.4. BUILD programs
- Language: Starlark
- Sequential execution
- Contains *rules* and *targets* to specify
    - interdependencies
    - what software outputs can be built
### 2.4.1. Syntax
- `.bzl`: Bazel extensions
- `load("extension_label","symbol_name")`:
  - load symbol from extension into environment
  - must be top-level
### 2.4.2. Rule Types
- `*_binary`: builds executables in a given language
  - `name`: symbol of the program which can be called in `build //folder:name`
- `*_test`: special case of `*_binary`, for automated testing
  - programs `return 0` on success
- `*_library`: separately compled modules
  - libs can depend on libs
  - bins and tests can depend on libs
### 2.4.3. Dependencies
- Dependency Management
  - *Actual*: X has actual dependency on Y IFF Y must be built before X can
  - *Declared*: X has declared dependency on Y IFF X has a dependency declaration on Y in its package
- Correct Build: A = subgraph(D)
    - Actual dep graph = subgraph of declare dep graph
    - i.e., directly connected nodes in A must also be directly connected in D
    - aka, D is an overapproximation of A
- Implications
  - E.g.,
      1. At first, dependencies are declared correctly: 
      - A: `X -> Y -> Z`
      - D: `X -> Y -> Z`
      - Overapprox, all good
      2. Then, someone accidentally adds code in X which is dependent on Z
      - A: `X -> Y -> Z`, `X -> Z`
      - D: `X -> Y -> Z`
      - A no longer subgraph of D, but build may be ok because transitive closure of A and D are equal
        - Transitive Closure: 
          - Matrix representing the reachability of node j from node i
          - 1: at least one path, 0: no path
          - e.g., in 2.
            ```
            A:  1 1 1   D:  1 1 1
                0 1 1       0 1 1
                0 0 1       0 0 1
            ```
      3. Someone refactors Y so that it no longer depends on Z
      - A: `X -> Y`, `X -> Z`
      - D: `X -> Y`
      - Build fails as there is no longer a path from X to Z
        - Underapproximation
- Dependency Types:
  - `srcs`: Files consumed directly by rule
  - `deps`: Points to separately-compiled modules providing header files, symbols, libs, data etc.
  - `data`: Files not containing source code.
    - e.g., compare unit test output to file data
      - tests run in isolated dir hence data files must be specified
      - use `glob()` and `**` to force iterate over files as rebuild only performed when dir is changed
    - not needed during build but required during execution
## 2.5. WORKSPACE
### 2.5.1. Rule Types
- `bind`
  - Gives a target an alias in the `//external` package
- `local_repository`
  - Allows targets from a local dir to be bound
    - Current repo can use targets defined in this dir
- `new_local_repository`
  - Turns local dir into Bazel repo
    - Current repo can define and use targets anywhere on filesystem
- `git_repository`
  - Clones git repo, checks out specified tag/commit, makes targets available for binding
- `maven_jar`
  - Downloads jar from Maven repo and makes it available for use as Java dependency
- `maven_server`
  - How to access a Maven repo

- `xcode_config`
  - 
- `xcode_version`
## 2.6. TERMINAL
### 2.6.1. Double Forward Slash `//`
- Indicates project root and starting a build

# 3. Test Structure
- Tests are run with `bazel test`
- File structure:
```
project_name/
|- projectName/
|   |- main/
|   |- test/
```
## 3.1. Good Test Design
- Outcome of test must depend only on
  - source files on which test has declared dependency
  - products of build system on which test has declared dependency
  - resources whose behavoiur is guaranteed by test runner to remain constant
### 3.1.1. Hermetic
- Airtight
  - Only access resources on which they have a declared dependency
### 3.1.2. Deterministic
- Given a certain input will always produce same output
### 3.1.3. Reentrant
- Multiple invocations of test can
  - run concurrently on a multiprocessor
  - be interrupted and "reentered" before completely executing on a single processor

## 3.2. Testing Roles
### 3.2.1. Build System
- Uses runfiles to deliver code and data
### 3.2.2. Test Runner
- Program which executes tests
  - If program runs to completion with exit code 0, test passed 
- Needs manifest of runfiles and input files which should be avail at runtime
- Failure may occur when
  - method fails
  - runner takes too long to execute (based on `timeout` or implied from `size`)
  - runner exceeds some resource limit (based on `size`)
#### 3.2.2.1. Initial Conditions
- Environment which is set before executing the test
  - env variables
    - e.g., size, timeout
  - resource limits
    - e.g., cpu, core
#### 3.2.2.2. Test Sharding
- Parralel testing with shards 
### 3.2.3. Host System


# Terminal Commands
- Unconditionally fetch all external deps: `bazel sync`
- Prefetch deps for specific targets: `bazel fetch`
- Show external dependencies in output_base/external: `ls $(bazel info output_base)/external`
- 