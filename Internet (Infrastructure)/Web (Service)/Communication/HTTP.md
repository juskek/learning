

# Client-Server Request Proces
Client sends request to server in form of message with format:
## Request Line
### Method
- GET: Retrieve all info
- HEAD: Retrieve status and header info only
- POST: Add info
- PUT: Add info/replace existing info
- DELETE: Rmove all info
- CONNECT: Establish tunnel
- OPTIONS: Decribe communication options for URI
- TRACE: Test loop message along with path
### URI
Which resource to apply method to, absolute URI used
- Server: *
- Proxy: https://<>.com/<>.<>
- Gateway: /<>.<>
  - Need to add host after, e.g.,
`
METHOD /<>.<> HTTPS/1.1

Host: <>.com
`
### HTTPS Version
## >=0 Header Fields
## Message Body


**Example**
GET https://www.example.com/test.pdf HTTPS/1.1
