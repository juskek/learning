- [1. Client-Server Request Process](#1-client-server-request-process)
  - [1.1. Request Line](#11-request-line)
    - [1.1.1. Method](#111-method)
    - [1.1.2. URI](#112-uri)
    - [1.1.3. HTTPS Version](#113-https-version)
  - [1.2. >=0 Header Fields](#12-0-header-fields)
  - [1.3. Message Body](#13-message-body)
  - [Request Headers](#request-headers)
    - [User-Agent](#user-agent)
    - [1.4. Cross-Origin Resource Sharing (CORS)](#14-cross-origin-resource-sharing-cors)

# 1. Client-Server Request Process
Client sends request to server in form of message with format:
## 1.1. Request Line
### 1.1.1. Method
- GET: Retrieve all info
- HEAD: Retrieve status and header info only
- POST: Add info
- PUT: Add info/replace existing info
- DELETE: Rmove all info
- CONNECT: Establish tunnel
- OPTIONS: Decribe communication options for URI
- TRACE: Test loop message along with path
### 1.1.2. URI
Which resource to apply method to, absolute URI used
- Server: *
- Proxy: https://<>.com/<>.<>
- Gateway: /<>.<>
  - Need to add host after, e.g.,
`
METHOD /<>.<> HTTPS/1.1

Host: <>.com
`
### 1.1.3. HTTPS Version
## 1.2. >=0 Header Fields
## 1.3. Message Body


**Example**
GET https://www.example.com/test.pdf HTTPS/1.1
## Request Headers
### User-Agent
- Lets servers and network peers identify app, OS, vendor and/or version of user agent
- User agent is a program representing a person
  - e.g., browser, app
### 1.4. Cross-Origin Resource Sharing (CORS)
- Allows server to permit loading resources from external origins  
  - For security, browsers restrict cross-origin HTTP requests intiated from scripts