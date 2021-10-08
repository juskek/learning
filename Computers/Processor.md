
# 1. Central Processing Unit
- Retrieves and executes instructions
- Made from logic gates
- Clock generator:
  - Syncs state of CPU
  - Speed: number of instructions per second
- Components:
## Clock
- Sends regular electrical pulse which syncs all components
## 1.1. Control Unit (CU)
## 1.2. Cache
- Small RAM built into processor
- Temporarily holds resused data and instructions 
## Buses
- Internal connection
- Sends signals and data 

### Address 
- Carries memory addresses from processor to
  - RAM
  - I/O devices
### Data
- Carries data between processor and other components
### Control
- Carries control signals and clock pulses from processor and other components

## 1.3. Registers
- Tiny high-speed memory
- Stores addresses, instructions, results
### 1.3.1. (Current) Instruction Register (CIR/IR)
- Stores instruction 
### 1.3.2. Memory Address Register (MAR)
- Stores address 
  - where instruction was copied from
  - result will be copied to
### 1.3.3. Program Counter/Instruction Pointer (PC/IP)
- Starts at 0 and increments after instruction execution to point to address of next instruction

### 1.3.4. Memory Data Register (MDR)
- Stores data 
  - which was copied from RAM
  - which is to be copied into memory
### 1.3.5. Accumulator (ACC)
- Stores intermediate results from ALU
  - faster access than RAM

## 1.4. Arithmetic Logic Unit (ALU)
- Arithmetic and logical operations
  - i.e., calculations and decisions


# 2. Graphics Processing Unit
