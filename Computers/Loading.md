# Downloading
1. Web browser
   1. composes HTTPS request
   2. pushes request to system networking stack
2. Networking stack 
   1. finds server address and turns into an IP address
   2. constructs series of TCP packets directed at relevant address
3. TCP packets are sent to
   1. router
   2. networking station
   3. trunk line
   4. networking station
   5. router
   6. machine/server
4. Server
   1. decrypts packets 
   2. finds file
   3. sends back over network
5. Browser
   1. Spools file contents received into temp file