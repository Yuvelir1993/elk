# General
Elasticsearch + Logstash + Kibana + Beats + all related stuff to play with.

# Links
[Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker)

# Pre requisites
## Prepare Linux
```bash
sudo sysctl -w vm.max_map_count=262144
```

## Get ETH 0 IP
Whenever it is needed
```bash
ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1
```

# Start ELK
```bash
sudo service docker start
cd /mnt/c/MyProjects/elk && sudo docker compose up
```
## Access Kibana
http://localhost:5601/

# Start Jenkins
```bash
sudo service docker start
cd /mnt/c/MyProjects/elk && sudo docker compose -f docker-compose-jenkins.yml up
```
## Access Jenkins
http://localhost:8080/
User: plozovik
Password: Password123++