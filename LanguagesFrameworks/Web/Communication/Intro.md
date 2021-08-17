Protocols/architectures used to design APIs for information exchange.
# Architectures
- What to do with a message received (receive, translate with protocol, execute actions, translate with protocol, send)

## REST: Representational State Transfer
- Languages: plain text, HTML, JSON, XML
- Adv: Scalability (low bandwidth), flexible
- Disadv:
- Mainly exchange data (based on resources)

# Protocols
- How to send a message

## HTTP: HyperText Transfer Protocol
- Languages: Text
- Stack: TCP, IP
- Adv:
- Disadv.:
  - No security for sensitive data (naked motorcycle ride), can be intercepted by any pseudoserver
- Use cases:
  - Document centric

## HTTPS: HTTP with TLS
- Adv.:
  - Transport level security (naked motorcycle ride through concrete tunnel), can only be read by the right server


## SOAP: Simple Object Access Protocol
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

### WSS: Web Services Security
How to:
- Sign messages
- Encrypt messages
- Verify sender's identity
### RPC: Remote Procedural Call
- Languages: JSON, XML
- Mainly invoke executable actions

## Transport Layer Security (TLS) Protocol
Establishes encrypted session between two computers by:
1. Server sends user valid and signed certificate
2. User sends one time public encryption key
3. Server decrypts with private encryption key
### TLS Certificate

## Secure Sockets Layer (SSL) Protocol