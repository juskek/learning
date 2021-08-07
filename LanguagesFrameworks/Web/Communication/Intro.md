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
- 
- Use cases:
  - Document centric


## RPC: Remote Procedural Call
- Languages: JSON, XML
- Mainly invoke executable actions

## SOAP: Simple Object Access Protocol
- Languages: XML
- Adv: 
  - Security
  - Web-socket/WS-addressing
  - WS-security
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