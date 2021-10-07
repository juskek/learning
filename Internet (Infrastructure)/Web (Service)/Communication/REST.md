# Representational State Transfer (REST)
- Architectural style for the web
- Central Idea:
  - A web app should allow the user to navigate through a network of resources residing in links
  - At each link, the resource's representation is transferred from the server to the client
- Definitions:
  - Resource
    - Data, user, etc.
    - Stateful
    - e.g.,
    ```
        ID: 1
        Name: John Doe
    ```
  - Representation
    - A format of the resource
    - Stateless
    - e.g., 
    ```
    // JSON
    {
        "id": 1,
        "name": "John Doe"
    }
    // XML
    <user>
        <id>1</id>
        <name>John Doe</name>
    </user>
    ```

- Characteristics
  - Stateless
    - No session information is stored in server-client connection
  - Scalability
# RESTful API
- API which adopts 


# SOAP vs REST
- SOAP XML is a lot bigger than REST JSON
- SOAP has a schema
- REST does not have a schema