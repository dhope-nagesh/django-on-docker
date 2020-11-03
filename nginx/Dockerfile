FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY certificates/ /etc/nginx/certs/
RUN ls -la /etc/nginx/certs/*
RUN chmod 777 -R /etc/nginx/certs/