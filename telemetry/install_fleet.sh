#!/bin/bash
curl -L -O https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-8.9.1-linux-x86_64.tar.gz
tar xzvf elastic-agent-8.9.1-linux-x86_64.tar.gz
cd elastic-agent-8.9.1-linux-x86_64
sudo ./elastic-agent install \
  --fleet-server-es=http://172.29.17.18:9200 \
  --fleet-server-service-token=<your_token> \
  --fleet-server-policy=fleet-server-policy \
  --fleet-server-port=8220