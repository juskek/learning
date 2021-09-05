- [1. Services](#1-services)
  - [1.1. Compute](#11-compute)
    - [1.1.1. Server (IaaS)](#111-server-iaas)
    - [1.1.2. Serverless](#112-serverless)
      - [1.1.2.1. App Platform](#1121-app-platform)
      - [1.1.2.2. Quantum](#1122-quantum)
      - [1.1.2.3. Functions](#1123-functions)
      - [1.1.2.4. Containers](#1124-containers)
      - [1.1.2.5. Virtual Machines](#1125-virtual-machines)
      - [1.1.2.6. High Performance Computing](#1126-high-performance-computing)
  - [1.2. Storage](#12-storage)
    - [1.2.1. File Storage](#121-file-storage)
    - [1.2.2. Relational DBs](#122-relational-dbs)
    - [1.2.3. NoSQL DBs](#123-nosql-dbs)
    - [1.2.4. Distributed DBs](#124-distributed-dbs)
    - [1.2.5. Blockchain DBs](#125-blockchain-dbs)
  - [1.3. Networking](#13-networking)
- [Hybrid cloud storage.](#hybrid-cloud-storage)
- [2. Azure](#2-azure)
  - [2.1. Adv:](#21-adv)
  - [2.2. Disadv:](#22-disadv)
- [3. AWS](#3-aws)
  - [3.1. Adv:](#31-adv)
  - [3.2. Disadv:](#32-disadv)
- [4. Google Cloud](#4-google-cloud)
  - [4.1. Adv:](#41-adv)
  - [4.2. Disadv:](#42-disadv)

# 1. Services

## 1.1. Compute
Processing data

### 1.1.1. Server (IaaS)

- MA Dedicated Host:
Dedicated physical server to host VMs
- GCP Compute Engine
### 1.1.2. Serverless
#### 1.1.2.1. App Platform
- MA App Service:
Upload Web/Mobile/Linux Apps
- MA Cloud Services:
Like MA App Service but with remote access and software installation control.

- GCP App Engine (PaaS):
Upload Web/Mobile/Linux Apps

#### 1.1.2.2. Quantum
- MA Quantum
  
#### 1.1.2.3. Functions
- GCP Cloud Functions:
Process events
- MA Functions:
Process events. Fast, small chunks of code on shared backend, usually microservice. Runtime limit approx. 10 mins. 
- MA Automation Runbooks: 
Run scripts. Slow, large chunks of code on individual worker. Good for admin on infrastructure.

#### 1.1.2.4. Containers
- MA Container Instances:
Run containers
- GCP Cloud Run (PaaS):
Upload containers 

- MA Container Registry:
Store and manage container images

- MA Kubernetes Engine
- MA Red Hat OpenShift
- MA Service Fabric


- GCP Kubernetes Engine:
Orchestrate multi-container apps

#### 1.1.2.5. Virtual Machines
- MA VMWare Solution
- MA Virtual Desktop
- MA Virtual Machines
- MA VM Scale Sets
- MA Batch:
Job scheduling and compute management with VMs.

#### 1.1.2.6. High Performance Computing
- MA CycleCloud:
Manage HPC and big compute clusters of any scale




## 1.2. Storage

### 1.2.1. File Storage
Storing unstructured data
- GCP Cloud Storage:
- GCP Cloud Filestore:
- 

### 1.2.2. Relational DBs
Storing structured data
- GCP Cloud SQL
- MA Database for PostgreSQL
- MA Database for MySQL
- MA Database for MariaDB
- MA SQL Database
- MA SQL Server Stretch DB:
Expand on-premises SQL DB to cloud.


### 1.2.3. NoSQL DBs
- MA Apache Cassandra MI 
- MA Cosmos DB
- MA Redis Cache
- GCP Bigtable
- GCP Firestore
- GCP Firebase Realtime
- GCP Memorystore
- 

### 1.2.4. Distributed DBs
- GCP Cloud Spanner

### 1.2.5. Blockchain DBs
- MA Blockchain Service


## 1.3. Networking
- Moving 



==========
?
- MA Avere vFXTL:
Manages on-premise expansion to cloud to optimise resources.
- MA NetApp Files:
Migration and running of file-based applications. 
- MA Storage:
For blobs, files, queues, tables (NoSQL) and disks (VMs). 
- MA Data Lake Storage

- MA Data Share:
For sharing any type of data securely.
- MA Managed Disks:
Storage for VMs
- MA StorSimple:
Hybrid cloud storage.
==========

# 2. Azure
## 2.1. Adv:
- Safe bet
## 2.2. Disadv:
- 
# 3. AWS
## 3.1. Adv:
- Breadth and depth of services
## 3.2. Disadv:
- Can get complicated and expensive when designed poorly
# 4. Google Cloud
## 4.1. Adv: 
- ML frameworks (TensorFlow, Keras)
## 4.2. Disadv:
- 

Azure cheaper for simple projects

AWS can get complicated




=============

To Blob or not to Blob (Gray, 2006):
- <= 256 KB: Blob in DB
- >= 1MB: Blob in file system
- In between, depends on read:write ratio and rate of object overwrite


Data-
- Base: structured data, usually for transactions
- Warehouse: structured data, exists on top of database specifically for analytics
- Lake: un-/semi-/structured data  