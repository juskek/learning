- [1. Architectures](#1-architectures)
  - [1.1. REST: Representational State Transfer](#11-rest-representational-state-transfer)
- [2. Protocols](#2-protocols)
  - [2.1. Email Protocols](#21-email-protocols)
    - [2.1.1. POP3: Post Office Protocol v3](#211-pop3-post-office-protocol-v3)
    - [2.1.2. IMAP: Internet Message Access Protocol](#212-imap-internet-message-access-protocol)
    - [2.1.3. SMTP](#213-smtp)
  - [2.2. HTTP: HyperText Transfer Protocol](#22-http-hypertext-transfer-protocol)
  - [2.3. HTTPS: HTTP with TLS](#23-https-http-with-tls)
  - [2.4. SOAP: Simple Object Access Protocol](#24-soap-simple-object-access-protocol)
    - [2.4.1. WSS: Web Services Security](#241-wss-web-services-security)
    - [2.4.2. RPC: Remote Procedural Call](#242-rpc-remote-procedural-call)
  - [2.5. Transport Layer Security (TLS) Protocol](#25-transport-layer-security-tls-protocol)
    - [2.5.1. TLS Certificate](#251-tls-certificate)
  - [2.6. Secure Sockets Layer (SSL) Protocol](#26-secure-sockets-layer-ssl-protocol)
    - [2.6.1. Proxy Server](#261-proxy-server)
- [3. Internet Protocol Suite (TCP/IP) - Practical Implementation](#3-internet-protocol-suite-tcpip---practical-implementation)
  - [3.1. Application](#31-application)
  - [3.2. Transport](#32-transport)
  - [3.3. Internet](#33-internet)
  - [3.4. Link](#34-link)
- [4. Open Systems Interconnection Model (OSI) - Theoretical Model](#4-open-systems-interconnection-model-osi---theoretical-model)
  - [4.1. Host Layers](#41-host-layers)
    - [4.1.1. Application](#411-application)
    - [4.1.2. Presentation](#412-presentation)
    - [4.1.3. Session](#413-session)
    - [4.1.4. Transport](#414-transport)
  - [4.2. Media Layers](#42-media-layers)
    - [4.2.1. Network](#421-network)
    - [4.2.2. Data Link](#422-data-link)
    - [4.2.3. Physical](#423-physical)

Protocols/architectures used to design APIs for information exchange.


# 1. Architectures
- What to do with a message received (receive, translate with protocol, execute actions, translate with protocol, send)

## 1.1. REST: Representational State Transfer
- Languages: plain text, HTML, JSON, XML
- Adv: Scalability (low bandwidth), flexible
- Disadv:
- Mainly exchange data (based on resources)

# 2. Protocols
- How to send a message

## 2.1. Email Protocols
Email message consists of:
- headers
  - RFC5322/RFC6532 field names and values
- payload/content
  - text, binary object, or
  - structured sequence of sub-messages, each with their own header and content.

### 2.1.1. POP3: Post Office Protocol v3
- Mainly to retrieve emails from remote server to local client
- Adv.:
  - Fast
- Disadv.:
  - 
- Ports:
  - 110: default non-encrypted
  - 995: secure

### 2.1.2. IMAP: Internet Message Access Protocol
- Like POP3 but with simultaneous access from multiple clients
- Adv.:
  - Syncing between multiple clients and server
- Disadv.:
  - Slow
- Ports:
  - 143: default non-encrypted
  - 993: secure
### 2.1.3. SMTP
- Mainly to send emails
- Ports:
  - 25: default non-encrypted
  - 2525: for SiteGround servers
  - 465: secure

## 2.2. HTTP: HyperText Transfer Protocol
- Languages: Text
- Stack: TCP, IP
- Adv:
- Disadv.:
  - No security for sensitive data (naked motorcycle ride), can be intercepted by any pseudoserver
- Use cases:
  - Document centric

## 2.3. HTTPS: HTTP with TLS
- Adv.:
  - Transport level security (naked motorcycle ride through concrete tunnel), can only be read by the right server


## 2.4. SOAP: Simple Object Access Protocol
- Languages: XML
- Adv: 
  - Message level security with WSS (clothed motorcycle ride), can only be read by the right process on the right server
  - Web-socket/WS-addressing
  - SwA
  - Automatic processing of MTOM
  - Runtime checking aginst WSDL
  - complex data, 
  - strict and defined rules
- Disadv: High bandwidth, 
- Stack: HTTP, HTML, SMTP
- Use cases:
  - Executable actions (based on RPC)
  - Data centric

### 2.4.1. WSS: Web Services Security
How to:
- Sign messages
- Encrypt messages
- Verify sender's identity
### 2.4.2. RPC: Remote Procedural Call
- Languages: JSON, XML
- Mainly invoke executable actions

## 2.5. Transport Layer Security (TLS) Protocol
Establishes encrypted session between two computers by:
1. Server sends user valid and signed certificate
2. User sends one time public encryption key
3. Server decrypts with private encryption key
### 2.5.1. TLS Certificate

## 2.6. Secure Sockets Layer (SSL) Protocol




### 2.6.1. Proxy Server
- Computer/router that relays between client and server
- Proxy: act on behalf on another


# 3. Internet Protocol Suite (TCP/IP) - Practical Implementation
- In effect
## 3.1. Application 
- Logical components used for server-to-client communications?
  - e.g., HTTP, SMTP, FTP
## 3.2. Transport 
- Logical components used for communication between two nodes
  - e.g., TCP, UDP
- Functions:
  - Connection-oriented communication
  - Reliability
  - Flow control
  - Multiplexing
- OSI Analogy: 4
## 3.3. Internet 
- Logical components used to transport network packets across network boundaries
  - e.g., IPv4, IPv6
- Functions:
  - Internetworking (connecting multiple networks through gateways)
- OSI Analogy: 3
## 3.4. Link 
- Physical and logical components (specs, protocols) used to connect nodes in a network
  - e.g., MAC, WiFi, Ethernet (LAN)
- Functions: 
  - Maintaining link states between local nodes
- OSI Analogy: 1, 2
  


# 4. Open Systems Interconnection Model (OSI) - Theoretical Model
- Flow of data in a communication system
- Each layer 
  - serves class of functionality to the layer above it
  - is served by the layer below it
- Classes of functionality are realised by communication protocols
## 4.1. Host Layers
### 4.1.1. Application
- Functionality: high-level API
  - e.g., resource sharing, remote file access???
- Data Unit: Data 
### 4.1.2. Presentation
- Functionality: Translation of data between a networking service and an application
  - e.g., character encoding, data compression, encryption/decryption
- Data Unit: Data 
### 4.1.3. Session
- Functionality: Managing sessions
  - Continuous exchange of information between two nodes
- Data Unit: Data 
### 4.1.4. Transport
- Functionality: Reliable transmission between network nodes 
  - e.g., segmentation, achnowledgement, multiplexing (superpositioning signals to share scarce resource)
- Data Unit: 
  - Segment, or 
    - Subportion of data packet, e.g., when packet size > max transmission unit or unreliable network
  - Datagram
    - basically a packet, but used on a different layer
    - protocol may specify differently
## 4.2. Media Layers
### 4.2.1. Network
- Functionality: Structuring and managing multi-node network 
  - e.g., addressing, routing, traffic control
- Data Unit: 
  - Packet
    - Control info 
      - e.g., source/dest address, error detection code, sequencing info
    - User data/payload
### 4.2.2. Data Link
- Functionality: Reliable physical transmission between two nodes
- Data Unit: 
  - Frame: Unit of transmission
    - Link layer header 
      - e.g., serial comms start/stop bit, header/footer
    - Packet 
      - e.g., byte, packet
### 4.2.3. Physical
- Functionality: Transmission/receiption over physical medium
- Data Unit: 
  - Bit, or 
    - 1,0
  - Symbol 
    - state or waveform which persists over some time, e.g., am/fm