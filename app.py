from flask import Flask
import sys
import yaml
import json
from github3 import GitHub
import base64

app = Flask(__name__)

g=GitHub()
shettyaditi=g.user('shettyaditi')

username = sys.argv[1].split("/", 4)[3]
repository = sys.argv[1].split("/", 4)[4]

@app.route("/v1/<filename>")
def hello1(filename):
    if filename.endswith('.yml'):
        r=base64.b64decode(g.repository(username,repository).contents(filename).content)
        return r

    if filename.endswith('.json'):
        i=base64.b64decode(g.repository(username,repository).contents(filename[:-5]+".yml").content)
        out=(json.dumps(yaml.load(i), sort_keys=True, indent=2))
        return out

@app.route("/")
def hello2():
   return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')