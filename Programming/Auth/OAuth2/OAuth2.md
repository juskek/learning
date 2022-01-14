# Open Authorization Framework 2.0

## Roles

### Resource Owners
- Resource Owner
  - Owns resource
  - Controls access
- End User
  - Resource owner who is a person

### Servers
- Resource Server 
  - Server hosting the resource
  - Accepts and responds to requests for the resource
  - Uses tokens
- Authorisation Server
  - Issues access tokens to client to access resources
### Client
- Client 
  - App looking to access resources
  - Requests resource server on behalf of resource owner (and with its authorisation)


## Flow 
1. Client requests authorisation from resource owner
   - Request can be made
     - directly
     - indirectly via authorisation server as intermediary (preferable)
2. Resource owner sends authorisation grant to client 
3. Client sends authorisation grant to authorisation owner
4. Authorisation owner sends access token to client
5. Client sends request with access token to resource owner
6. Resource owner serves request

## Grants
- Credential representing resource owner's authorisation

### Grant Types
#### Authorisation Code
- Authorisation server is intermediary in step 1
- 
#### Implicit
- aka User Agent Flow
#### Resource Owner Password Credentials
- aka Password Flow
#### Client Credentials

