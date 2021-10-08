- [1. Random Access Memory](#1-random-access-memory)
  - [1.1. Stack Memory](#11-stack-memory)
  - [1.2. Heap Memory](#12-heap-memory)
  - [1.3. Address Binding](#13-address-binding)
  - [1.4. Memory Leak](#14-memory-leak)
- [2. Central Processing Unit](#2-central-processing-unit)
  - [2.1. Control Unit (CU)](#21-control-unit-cu)
    - [2.1.1. (Current) Instruction Register (CIR/IR)](#211-current-instruction-register-cirir)
    - [2.1.2. Memory Address Register (MAR)](#212-memory-address-register-mar)
    - [2.1.3. Program Counter/Instruction Pointer (PC/IP)](#213-program-counterinstruction-pointer-pcip)
  - [2.2. Arithmetic Logic Unit (ALU)](#22-arithmetic-logic-unit-alu)
- [3. Machine/Instruction Cycle](#3-machineinstruction-cycle)
- [4. Drive](#4-drive)
  - [4.1. Volume (Logical Drive)](#41-volume-logical-drive)
  - [4.2. File System](#42-file-system)
- [5. Operating Systems](#5-operating-systems)
  - [5.1. Multitasking](#51-multitasking)
    - [5.1.1. Daemon (Dump & Examine Monitor)](#511-daemon-dump--examine-monitor)


# Computers
- There are _ critical components
- Processor 
- Memory
- Network Card
- 



# 3. Machine/Instruction Cycle
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


# 5. Operating Systems
## 5.1. Multitasking
### 5.1.1. Daemon (Dump & Examine Monitor)  
- Continuously running background process 
- Convention: end process with letter d, e.g. `syslogd`