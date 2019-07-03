import time

import redis
from flask import Flask

app = Flask(__name__) #creates the application object as an instance of Flask (the "___name__" variable is a Python predefined variable which is set to the name of the module in which it is used)
cache = redis.Redis(host='redis', port=6379)
print("Started app...")

def get_hit_count():
    retries = 5
    while True:
        try:
            redisValue = cache.incr('hits')
            print("Got cache :"+str(redisValue))
            #print(redisValue)
            return redisValue
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/morne') #Routes are the different "URLs" that the application implements (view functions)
def hello():
    count = get_hit_count()
    print ("Counting :"+ str(count))
    return 'Hello from Docker! I have been seen {} times.\n'.format(count)
    #return 'Hello World'