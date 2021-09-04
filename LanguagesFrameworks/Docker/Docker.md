# Docker
- Platform for dev, del and dep containers

## Generic Process:
1. Create container
   - `Dockerfile`: for single container
   - `docker-compose.yml`: for multicontainer
2. Build container image
   - `docker build`
   - `docker-compose build`
3. Run container image
   - `docker run`
   - `docker compose up`


# Docker Compose
- Defining and running multicontainer Docker apps


## Hosting on Firebase
1. Add `firebase-tools` to `Dockerfile`
   - e.g., for node.js, `RUN npm install -g firebase-tools`
2. Add port to `docker-compose.yml`
   - e.g.,
  ```
  services:
    web:
        ports:
            - "9005:9005"
  ```
3. Expose the port in `Dockerfile` so that the login process launches the browser
   ```
   FROM ...
   ...
   EXPOSE 9005
   ```
4. Run the container and use firebase to login, init and deploy from the container
   - `docker-compose exec web firebase login`
   - `docker-compose exec web firebase init`
   - `docker-compose exec web firebase deploy`

