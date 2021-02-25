from flask import Flask
import redis

app = Flask(__name__)

@app.route("/")
def hello():
    r = redis.Redis(host='10.0.1.109', port=6379, db=0)
    return "Hello World! From the Planet - "+str(r.get('planet-3'))

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')