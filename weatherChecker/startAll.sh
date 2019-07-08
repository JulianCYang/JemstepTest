#!/bin/bash
docker stop myRedis
docker stop mongodb
docker rm myRedis
docker rm mongodb
docker run -d --name="myRedis" redis
docker run -d --name="mongodb" mongo 
