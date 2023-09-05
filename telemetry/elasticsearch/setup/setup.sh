#!/bin/bash

ELASTIC_PASSWORD=$1
KIBANA_PASSWORD=$2

echo "Start setup phase."

bash /usr/share/elasticsearch/setup/create_certs.sh "$ELASTIC_PASSWORD" "$KIBANA_PASSWORD"

echo "End setup phase."