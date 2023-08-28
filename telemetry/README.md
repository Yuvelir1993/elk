# General
[Send telemetry to an OpenTelemetry Collector](https://opentelemetry.io/docs/instrumentation/python/getting-started/#send-telemetry-to-an-opentelemetry-collector)

[Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker)
[Getting started with the Elastic Stack and Docker-Compose](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose)

Please remember that OpenTelemetry doesn't store any data (traces, metrics, logs). It has concept of exporters, where data are exported to user selected data (trace, metric, log) storage (3rd party). 
OpenTelemetry is "middle layer", where you can switch to another storage easily.

## APM server
Elastic agent is installed at '/opt/Elastic/Agent' by default and should be run as a service.

[Run APM Server on Docker](https://www.elastic.co/guide/en/apm/guide/current/running-on-docker.html)

## Pre requisites
### Prepare Linux
```bash
sudo sysctl -w vm.max_map_count=262144
```

### Get ETH 0 IP
Whenever it is needed :)
```bash
ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1
```

## Run Collector + Jaeger docker container + ELK
Execute the command below using Ubuntu terminal from the 'otel-collector' folder.
```bash
sudo service docker start
cd /mnt/c/MyProjects/elk/telemetry && sudo docker compose up
```

### Access Kibana
http://localhost:5601/

### Access Jaeger
http://localhost:16686/

### ZPages for quick collector overview
http://localhost:55679/debug/servicez