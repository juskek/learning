Judge0 CE is released with two files:
# Docker Compose File: `docker-compose.yml`
- Config for docker compose
## Compose File Format: `version: 2`
## Extension Fields
```
x-logging:
  &default-logging
  logging:
    driver: json-file
    options:
      max-size: 100m
```
- `x-`: Extension field, for reusing config fragments
  - Config fragments are small files for kernel config, in syntax of original kernel `.config` file, for better tracking of revisions 
    - Revision control checks diff between config changes, but there are dependencies between different config options, hence changing 1 config might require changing many others
    - Fragments help to track those changes by recording only who initiated the change, why, and the specific options which were changed
    - The fragment is the processed and the final config file is generated (with all new values)
  - `x-logging`: *A logging fragment is created based off default and the config options for the driver and max size are set.*
  - `@default-logging`: Creates an anchor and specifies `logging` and its settings

## Service Config: `services:`
### Instantiate nginx web server:
1. with Judge0 server image: `image: judge0/jwilder-nginx-proxy:latest-2020-10-30` 
2. with container volumes:
```
volumes:
    - /var/run/docker.sock:/tmp/docker.sock:ro
    - ./srv/nginx/vhost.d:/etc/nginx/vhost.d
    - ./srv/nginx/html:/usr/share/nginx/html
    - ./srv/ssl_certs:/etc/nginx/certs:ro
```
3. with ports to use:
```
ports:
      - "80:80"
      - "443:443"
    <<: *default-logging
    restart: always
```
- `80`: HTTP
- `443`: HTTPS
- `<<`: YAML merge key, for merging mappings
- `*default-logging`: alias referring to original anchor
  - Therefore merging `restart: always` mapping to the mapping of `&default-logging`
### Set TLS encryption
```
letsencrypt:
    image: judge0/jrcs-letsencrypt-nginx-proxy-companion:2.0
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./srv/ssl_certs:/etc/nginx/certs:rw
    volumes_from:
      - nginx
    <<: *default-logging
    restart: always
```
### Configure server 
```
server:
    image: judge0/judge0:1.13.0
    environment:
      - VIRTUAL_HOST=judge0-62876.web.app
      - LETSENCRYPT_HOST=judge0-62876.web.app
      - LETSENCRYPT_EMAIL=justinkekjq@gmail.com
    volumes:
      - ./judge0.conf:/judge0.conf:ro
    privileged: true
    <<: *default-logging
    restart: always
```
### Set service workers
```
workers:
    image: judge0/judge0:1.13.0
    command: ["./scripts/workers"]
    volumes:
      - ./judge0.conf:/judge0.conf:ro
    privileged: true
    <<: *default-logging
    restart: always
```
### Config database
```
db:
    image: postgres:13.0
    env_file: judge0.conf
    volumes:
      - postgres-data:/var/lib/postgresql/data/
    <<: *default-logging
    restart: always
```
### Config redis cache:
```
redis:
    image: redis:6.0
    command: [
      "bash", "-c",
      'docker-entrypoint.sh --appendonly yes --requirepass "$$REDIS_PASSWORD"'
    ]
    env_file: judge0.conf
    volumes:
      - redis-data:/data
    <<: *default-logging
    restart: always
```
### Set volumes
```
volumes:
  postgres-data:
  redis-data:
```

- `privileged: true`: gives container access to all devices on host
  - allows Docker daemon in container
  - provides direct hardware access
# `judge0.conf`
   - Config for Judge0 server

