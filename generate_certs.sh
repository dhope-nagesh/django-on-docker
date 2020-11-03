# Chage current directory to nginx/certificates
cd nginx/certificates

# Generate the CA for client Key and Certificate
openssl req -x509 -sha256 -newkey rsa:4096 -keyout server_ca.key -out server_ca.crt -days 356 -nodes -subj '/CN=Server Cert Authority'

# Generate CA bundle
cat server_ca.key > server_ca.pem
cat server_ca.crt >> server_ca.pem

# Generate the Server Key, and Certificate and Sign with the CA Certificate
openssl req -new -newkey rsa:4096 -keyout server.key -out server.csr -nodes -subj '/CN=127.0.0.1'
openssl x509 -req -sha256 -days 365 -in server.csr -CA server_ca.crt -CAkey server_ca.key -set_serial 01 -out server.crt



# Generate the CA for client Key and Certificate
openssl req -x509 -sha256 -newkey rsa:4096 -keyout client_ca.key -out client_ca.crt -days 356 -nodes -subj '/CN=Client Cert Authority'

# Generate CA bundle
cat client_ca.key > client_ca.pem
cat client_ca.crt >> client_ca.pem


# Generate the Client Key, and Certificate and Sign with the CA Certificate
openssl req -new -newkey rsa:4096 -keyout client.key -out client.csr -nodes -subj '/CN=Test'
openssl x509 -req -sha256 -days 365 -in client.csr -CA client_ca.crt -CAkey client_ca.key -set_serial 02 -out client.crt

# Move back to root directory
cd ../..