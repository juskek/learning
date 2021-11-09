# Blockchain
- Growing list of blocks that are chained together using cryptography
- Used as ledger to record events, e.g., transactions

## Chained Blocks
- Blocks are records of 
  1. Cryptographic hash
    - Generated from hash, timestamp and data of previous block
  2. Timestamp
    - Proof of existence of data
  3. Transaction data
- Altering previous blocks requires altering all subsequent blocks

## Decentralised Ledger
- Records
  - Keeps everyone else in check
- Timestamping 
  - Distributed to prevent malicious user from tampering with data before addition of a new block

## Version Scoring
- Used to select most reliable version history
- Methods
  - Proof-of-Work (PoW)
    - Probability of success in appending new block proportional to computational effort expended 
    - Deterrence of manipulation through large energy and hardware requirements
    - e.g., Bitcoin
      - Issuance of 21 million Bitcoins in the genesis block
      - Distribution given to worker who successfully appends new block
  - Proof-of-Stake
    - Probability of success in appending new block proportional to amount of holdings in the associated cryptocurrency
    - Deterrence of manipulation through detrimental effect on majority holder of cryptocurrency when attacking the network
