#!/usr/bin/env bash
redis-cli -a yuan --cluster create 192.168.123.151:6379 192.168.123.151:6380 192.168.123.151:6381 192.168.123.151:6382 192.168.123.151:6383 192.168.123.151:6384  --cluster-replicas 1
