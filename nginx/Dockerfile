FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY certificates/server.crt /etc/ssl/certs/server.crt
COPY certificates/server.key /etc/ssl/private/server.key
COPY certificates/client.crt /etc/ssl/certs/client.crt
COPY certificates/client.key /etc/ssl/private/client.key
COPY certificates/ca.crt /etc/ssl/certs/ca-certificates.crt
