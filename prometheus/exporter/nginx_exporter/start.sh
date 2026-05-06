#!/bin/bash
# https://github.com/nginxinc/nginx-prometheus-exporter

docker run -d -p 9113:9113 nginx/nginx-prometheus-exporter:0.8.0 -nginx.scrape-uri http://10.1.34.16:6888/nginx_status
