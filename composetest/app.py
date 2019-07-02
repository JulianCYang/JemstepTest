import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
print("Started app...")

def get_hit_count():
    retries = 5
    while True:
        try:
            redisValue = cache.incr('hits')
            print("got cache:" + redisValue)
            return redisValue
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    print("Counting: "+ count)
    return 'Hello from Docker! I have been seen {} times.\n'.format(count)