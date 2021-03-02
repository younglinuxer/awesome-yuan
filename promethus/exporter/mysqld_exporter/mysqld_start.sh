#!/bin/bash
docker run -d   -p 9104:9104  --network my-mysql-network  -e DATA_SOURCE_NAME="exporter:aA123$%^@(10.1.34.11:3306)/"   prom/mysqld-exporter
