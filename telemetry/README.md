# General
[Send telemetry to an OpenTelemetry Collector](https://opentelemetry.io/docs/instrumentation/python/getting-started/#send-telemetry-to-an-opentelemetry-collector)

[Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker)
[Getting started with the Elastic Stack and Docker-Compose](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose)

Please remember that OpenTelemetry doesn't store any data (traces, metrics, logs). It has concept of exporters, where data are exported to user selected data (trace, metric, log) storage (3rd party). 
OpenTelemetry is "middle layer", where you can switch to another storage easily.

[Avaliable features list for used license](https://www.elastic.co/subscriptions).

## APM server
Elastic agent is installed at '/opt/Elastic/Agent' by default and should be run as a service.

[Run APM Server on Docker](https://www.elastic.co/guide/en/apm/guide/current/running-on-docker.html)

### Kibana configuration
Add token and tls certificate + key for tls which you can find in the apm-server.yml.
Example token: AAEAAWVsYXN0aWMvZmxlZXQtc2VydmVyL3Rva2VuLTE2OTMxNDgwMjE4MjY6QUE4Z3RsVVhSUFNRelp5VHdQcm91dw
After successful APM integration you should see the "no longer blocking ingestion as all precondition checks are now satisfied" log from the APM server instance.

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

## Docker helpers
Stop all containers
```bash
docker stop $(docker ps -a -q)
```

Remove all volumes
```bash
docker volume rm $(docker volume ls -q)
```

## Run Collector + Jaeger docker container + ELK
Execute the command below using Ubuntu terminal from the 'otel-collector' folder.
```bash
sudo service docker start
cd /mnt/c/MyProjects/elk/telemetry && sudo docker compose up
```

## Run FLeet Server + Fleet Agent
When ELK stack is running, run Fleet stack.
```bash
sudo docker network create fleet-external
sudo docker compose -f docker-compose-fleet-server-agent.yml up
```

### Access Kibana
http://localhost:5601/

### Access Jaeger
http://localhost:16686/

### ZPages for quick collector overview
http://localhost:55679/debug/servicez

## Beats
### Filebeat
#### syslog module

Ensure that 'syslog' service installed
```bash
sudo apt-get install --reinstall rsyslog
```

Ensure that 'syslog' service is up and running
```bash
sudo service rsyslog start
```