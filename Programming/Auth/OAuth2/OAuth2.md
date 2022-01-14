- [1. Open Authorization Framework 2.0](#1-open-authorization-framework-20)
  - [1.1. Roles](#11-roles)
    - [1.1.1. Resource Owners](#111-resource-owners)
    - [1.1.2. Servers](#112-servers)
    - [1.1.3. Client](#113-client)
  - [1.2. Flow](#12-flow)
  - [1.3. Components](#13-components)
  - [1.4. Grants](#14-grants)
    - [1.4.1. Grant Types](#141-grant-types)
      - [1.4.1.1. Authorisation Code](#1411-authorisation-code)
      - [1.4.1.2. PKCE](#1412-pkce)
      - [1.4.1.3. Client Credentials](#1413-client-credentials)
      - [1.4.1.4. Device Code](#1414-device-code)
      - [1.4.1.5. Refresh Code](#1415-refresh-code)
      - [1.4.1.6. Deprecated](#1416-deprecated)
        - [1.4.1.6.1. Implicit](#14161-implicit)
      - [1.4.1.7. Resource Owner Password Credentials](#1417-resource-owner-password-credentials)

# 1. Open Authorization Framework 2.0
## 1.1. Roles

### 1.1.1. Resource Owners
- Resource Owner (RO)
  - Owns resource
  - Controls access
- End User (EU)
  - Resource owner who is a person

### 1.1.2. Servers
- Resource Server (RS)
  - Server hosting the resource
  - Accepts and responds to requests for the resource
  - Uses tokens
- Authorisation Server (AS)
  - Issues access tokens to client
### 1.1.3. Client
- Client 
  - App looking to access resources
  - Requests resource server on behalf of resource owner (and with its authorisation)
- Types
  - Public
    - Cannot protect client key and secret
    - e.g., mobile apps, js app
      - if client secret is added into a JS app for accessing the AS,
      - user of app can inspect elements and find it 
  - Confidential
    - Can protect client key and secret
    - e.g., web app running in server

## 1.2. Flow 
**Front Channel**
- Visible to end user
- All info is passed through redirect URI via GET only
1. Client requests authorisation from RO
   - Request can be made
     - directly
     - indirectly via authorisation server as intermediary (preferable)
       - e.g., redirect 
2. RO sends authorisation grant to client 

**Back Channel**
- Not visible to end user
- Direct communication (no redirect URI)
  - Other HTTP methods available
3. Client sends authorisation grant to AS
4. AS sends access token to client
5. Client sends request with access token to RS
6. RS serves request to client

- When step 1 is done through authorisation server, there are two channels:
  - Front Channel
    - Steps 1 and 2 done through redirect
    - Visible to user
  - Back Channel
    - Steps 3 to 6 done through back 
    - Not visible to user
## 1.3. Components
- Access Token (AccToken)
  - Provides client with access to protected resources 
- Authorization Grant (AuthGrant)
  - Credential held by client representing RO to obtain access token
- Client Secret
  - Secret known only to client and AS
  - i.e., application password
## 1.4. Grants
- Credential representing RO's authorisation

### 1.4.1. Grant Types
#### 1.4.1.1. Authorisation Code
- Use Case:
  - For confidential and public clients
  - 
- Authorisation server is intermediary in step 1
  - Redirect based flow
- Benefits:
  - Client can be authenticated
  - RO only authenticates with AS, credentials are not shared
  - AccToken sent directly from AS to client
    - Does not pass through RO's user agent
  - Flow:
    - User directed from client to AS
    - User returns to client via redirect URL
    - Client receives authorisation code from redirect URL
    - Client requests AccToken with Authorisation Code

#### 1.4.1.2. PKCE
- Extension to Authorisation Code to prevent CSRF and authorisation code injection attacks
- Use Case:
  - 
#### 1.4.1.3. Client Credentials
- Use Case:
  - For confidential clients only
    - e.g., B2B or client and server are part of same system
Client sends authorisation request with credentials to AS
AS sends AccToken to client

#### 1.4.1.4. Device Code
- Exchanges previously obtained device code for AccToken
- Use Case:
  - Browserless/input constrainted device
#### 1.4.1.5. Refresh Code
- Exchanges previously obtained refresh token for an AccToken 
  - Done when AccToken has expired
#### 1.4.1.6. Deprecated
##### 1.4.1.6.1. Implicit
- aka User Agent Flow
- Use Case:
  - Public clients
- Not recommended because
  - Access token returned in HTTP redirect without any confirmation it has been received by client
  - Exposed to user, may be compromised before expiry
- Substitute
  - Authorization Code + PKCE
#### 1.4.1.7. Resource Owner Password Credentials
- aka Password Grant, Password Flow, Username-Password Auth Flow
- Use Case:
  - RO/EU has trust relationship with client 
    - e.g., client and server are part of same system
- Not recommended because
  - Client stores user credentials and sends it to AS
  - No MFA
- Substitute
  - 

EU/RO provides credentials to client
Client sends credentials with AccToken request to AS
    AS authenticates client
AS sends AccToken to client
    Refresh token can be issued as well
