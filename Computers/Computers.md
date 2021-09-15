## Random Access Memory
### Stack Memory
- Temporary data storage
- Static allocation
- First In Last Out
- Stack pointer: indicates where current stack memory location is

### Heap Memory
- Dynamic allocation
- Variables which are no longer used are marked for garbage collection
- e.g., Classes, Objects, Arrays, Indexers, Interfaces

### Address Binding
- Association of data/instructions to physical memory location
- Compile Time: Before program is loaded 
- Load Time: When program is loading
- Execution Time: During runtime
## Central Processing Unit
- Retrieves and executes instructions
- Made from logic gates
- Clock generator:
  - Syncs state of CPU
  - Speed: number of instructions per second
- Components:
  - Control Unit (CU)
    - (Current) Instruction Register (CIR/IR)
      - Stores instruction 
    - Memory Address Register (MAR)
      - Stores address where instruction was copied from/result will be copied to
    - Program Counter/Instruction Pointer (PC/IP)
      - Starts at 0 and increments after instruction execution to point to address of next instruction
  - Arithmetic Logic Unit (ALU)
## Machine/Instruction Cycle
1. Fetch
   - Software is a set of instructions in RAM
   - PC starts at zero and points to first MAR
   - CU copies instruction in MAR to IR
2. Decode
   - CU parses bits into 
     - Optcode: Bits containing instruction (add, subtract etc.)
     - Operand: Data/memory location to execute instruction on
3. Execute
   - CU sends electrical signals to relevant components (e.g., ALU)
   - ALU stores result in MAR of RAM
- Cycle repeated from startup to shutdown
- Multiple cores = multiple cycles

## Volume (Logical Drive)
- Single accessible storage 
- Single file system
- 
## File System
- How data is stored and retrieved
- If not data would be on large body with no way to tell where each starts and ends
- Each group of data is a file

# Operating Systems
## Multitasking
### Daemon (Dump & Examine Monitor)  
- Continuously running background process 
- Convention: end process with letter d, e.g. `syslogd`