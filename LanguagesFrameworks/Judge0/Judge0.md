Judge0 CE is released with two files:
# Docker Compose File: `docker-compose.yml`
- Config for docker compose
## Compose File Format: `version: '2'`
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

## Service Config: `services:`
### Instantiate nginx web server:
1. with Judge0 server image: `image: judge0/jwilder-nginx-proxy:latest-2020-10-30` 
2. with volumes 
```
volumes:
    - /var/run/docker.sock:/tmp/docker.sock:ro
    - ./srv/nginx/vhost.d:/etc/nginx/vhost.d
    - ./srv/nginx/html:/usr/share/nginx/html
    - ./srv/ssl_certs:/etc/nginx/certs:ro
```
# `judge0.conf`
   - Config for Judge0 server

