- [1. Overview](#1-overview)
- [2. Structure](#2-structure)
  - [2.1. Workspace](#21-workspace)
  - [2.2. Packages](#22-packages)
  - [2.3. Targets](#23-targets)
    - [2.3.1. Labels](#231-labels)
    - [2.3.2. Rules](#232-rules)
  - [2.4. BUILD programs](#24-build-programs)
    - [2.4.1. Syntax](#241-syntax)
    - [2.4.2. Rule Types](#242-rule-types)
    - [Dependencies](#dependencies)
  - [2.5. WORKSPACE](#25-workspace)
  - [2.6. TERMINAL](#26-terminal)
    - [2.6.1. Double Forward Slash `//`](#261-double-forward-slash-)

# 1. Overview
- Used to build binaries from source code 

# 2. Structure
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
  - directory with a BUILD file to specify
    - interdependencies
    - what software outputs can be built
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
### 2.4.1. Syntax
- `.bzl`: Bazel extensions
- `load("extension_label","symbol_name")`:
  - load symbol from extension into environment
  - must be top-level
### 2.4.2. Rule Types
- `*_binary`: builds executables in a given language
- `*_test`: special case of `*_binary`, for automated testing
  - programs `return 0` on success
### Dependencies
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

## 2.6. TERMINAL
### 2.6.1. Double Forward Slash `//`
- Indicates project root and starting a build