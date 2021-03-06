## About
This is simple django application which exposes `/webhook/` (with token authentication) and `/public-webhook/` (without any authentication) API routes.

In production this app has mutual TLS enabled.

credits [django-on-docker](https://github.com/testdrivenio/django-on-docker)


### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production with mTLS

#### Generate Self-signed CA, server and client certificates
    
```sh
$ chmod +x generate_certs.sh
$ ./generate_certs.sh
```

#### Run containers with mTLS.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out with mTLS at [https://127.0.0.1:1337](https://127.0.0.1:1337)
    
    Test it out without mTLS at [http://127.0.0.1:8000](http://127.0.0.1:8000)
1. Use curl to test

    ```sh
    $ curl -X POST -H 'Content-type: application/json' --data '{"payload": { "a": "b"}}' https://127.0.0.1:1337/public-webhook/ --key nginx/certificates/client.key --cert nginx/certificates/client.crt --cacert nginx/certificates/server_ca.pem
    $ curl -X POST -H 'Content-type: application/json' -H 'Authorization: Token 61c0ef4aa8b8e9b6fd95612ca57e0cd727eabbe6' --data '{"payload": { "a": "b"}}' https://127.0.0.1:1337/webhook/ --key nginx/certificates/client.key --cert nginx/certificates/client.crt --cacert nginx/certificates/server_ca.pem
    ```
    
#### View Webhook data on Django admin
1. Login to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) with username = admin, password = admin
