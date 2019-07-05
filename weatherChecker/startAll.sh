#!/bin/bash
docker stop myRedis
docker rm myRedis
docker run -d --name="myRedis" redis 