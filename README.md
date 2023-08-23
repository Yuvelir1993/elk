# General
Elasticsearch + Logstash + Kibana + Beats + all related stuff to play with.

# Links
[Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker)

# Pre requisites
## Prepare Linux
```bash
sudo sysctl -w vm.max_map_count=262144
```

# Start ELK
```bash
sudo service docker start
cd /mnt/c/MyProjects/elk && sudo docker compose up
```

# Access Kibana
http://localhost:5601/
