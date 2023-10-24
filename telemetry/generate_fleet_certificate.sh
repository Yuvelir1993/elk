#!/bin/bash
rm -rf .certs
mkdir .certs

# Generate the CA key and certificate
openssl genpkey -algorithm RSA -out .certs/ca-key.pem
openssl req -x509 -new -nodes -key .certs/ca-key.pem -sha256 -days 365 -out .certs/ca-cert.pem -subj "/C=US/ST=California/L=San Francisco/O=Your Company/OU=Your Organization/CN=your-ca"

# Generate the server key and certificate
openssl genpkey -algorithm RSA -out .certs/fleet-server-key.pem
openssl req -new -key .certs/fleet-server-key.pem -out .certs/fleet-server.csr -subj "/C=US/ST=California/L=San Francisco/O=Your Company/OU=Your Organization/CN=your-server"
openssl x509 -req -in .certs/fleet-server.csr -CA .certs/ca-cert.pem -CAkey .certs/ca-key.pem -CAcreateserial -out .certs/fleet-server-cert.pem -days 365 -sha256

# Generate a passphrase for the private key
echo "MySimplePassphrase" > .certs/fleet-server-passphrase.txt

# Encrypt the private key with the passphrase
openssl rsa -in .certs/fleet-server-key.pem -out .certs/fleet-server-key-enc.pem -passout file:.certs/fleet-server-passphrase.txt

