FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY sample_certificates/sample_cert.crt /etc/ssl/certs/sample_cert.crt
COPY sample_certificates/sample_cert.key /etc/ssl/private/sample_cert.key
