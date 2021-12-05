## Workers
- Similar to Node.js
  - Server-side runtime environment 
  - Compiles with V8 engine
Key features: Isolates, compute per requests, distributed execution
### Canonical Flow
1. Event listener waits for request to Worker
2. Listener fetches event to event handler
3. Event handler initiates response by
   1. extracting event request, and 
   2. passing it to request handler 
4. Request handler returns response when ready 
```
addEventListener("fetch", event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  return new Response("Hello worker!", { status: 200 })
}
```
## Features 
### Isolates
- Sandbox for each function
- Multiple sandboxes on single runtime
  - vs containers: multiple runtimes for multiple functions
- Adv:
  - Eliminates cold start
  - Less overhead
- Dis:
  - Isolates can be spun down/evicted
    - Resource limitations
    - Suspicious activity
      - Functions within isolate which mutate global state may not finish executing
  - Isolates are short lived
### Compute per Requests
- Charged per CPU cycle, not per time 
  - e.g., with can. flow,
    - charged for no. of cycles to get response,
    - not time while waiting for response 
### Distributed Execution

## Tools
### Workers KV
- Low-latency key-value storage
- High-read low-write freq applications
- Eventual consistency 

### Cache 
- Ephemeral 
- Colo-local storage

### Streams API
- Javascript API to access treams of data (e.g., YouTube)

### Durable Objects
- Low-latency consistent storage
- Features
  - Global Uniqueness: 
    - Single instance of Durable Object class across Earth
  - Transactional storage API:
    - Strongly-consistent key-value storage 
### WebSockets
- Open connections between client and origin server 
  - Communicate with Workers in realtime
  - e.g, live chat, gaming