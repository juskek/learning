# Blockchain
- Growing list of blocks that are chained together using cryptography
- Used as ledger to record events, e.g., transactions

# Components
## Chained Blocks
- Blocks are records of 
### Cryptographic hash
- Generated from hash, timestamp and data of previous block
### Human-Readable Addresses
- Hash are referred to as addresses
- Blockchain Name Service (BNS) analogous to DNS

###  Timestamp
- Proof of existence of data
###  Transaction data
- Altering previous blocks requires altering all subsequent blocks
### Block Time
- Time taken for network to confirm new block

### Transactions Per Second
- Transactions per block/block time

## Smart Contracts
- Immutable, self-executed program stored in blockchain
### Secret Contracts
- For privacy protection, personal information is not written to blockchain

## Decentralised Ledger
- Records
  - Keeps everyone else in check
- Timestamping 
  - Distributed to prevent malicious user from tampering with data before addition of a new block

## Consensus Mechanism
- Used to select most reliable version history

### Proof-of-Work/Waste (PoW)
- Probability of success in appending new block proportional to computational effort expended 
- Deterrence of manipulation through large energy and hardware requirements
- e.g., Bitcoin
  - Issuance of 21 million Bitcoins in the genesis block
  - Distribution given to worker who successfully appends new block



### Proof-of-Stake
- Probability of success in appending new block proportional to amount of holdings in the associated cryptocurrency
- Deterrence of manipulation through detrimental effect on majority holder of cryptocurrency when attacking the network
- Terminology
  - Delegator: Trusts validator for due diligence
  - Validator: Creates new blocks 
  - Slashing: Losing portion of stake for malicious behaviour
#### Delegated
- Voting Rights:
  - Validators only
- Slashing:
  - Depends on chain protocol

#### Hybrid
- Voting Rights:
  - Depends on chain protocol
- Slashing:
  - Depends on chain protocol

#### Liquid
- Voting Rights:
  - Vote for protocol changes
- Slashing:
  - Paid by validator
#### Bonded
- Voting Rights:
  - Vote for protocol changes
- Slashing:
  - Paid by validator and delegator


# Features
## Segmentation/Zoning
- Offloading resource intensive services into separate chain
## Sharding
- Splitting blockchain into shards for storage on different nodes 
## Cross Chain Communication
- Communicating with other networks