from flask import Flask
from github import Github
import base64
import sys
import yaml
import json

app = Flask(__name__)

g=Github()
argument=sys.argv[1].split("/")
username = argument[len(argument)-2]
repository = argument[len(argument)-1]
repo=g.get_user(username).get_repo(repository)
@app.route("/v1/<filename>")
def hello1(filename):
    if filename.endswith('.yml'):
        r=base64.b64decode(repo.get_file_contents(filename).content)
        return r

    if filename.endswith('.json'):
        i=base64.b64decode(repo.get_file_contents(filename[:-5]+".yml").content)
        out=(json.dumps(yaml.load(i), sort_keys=True, indent=2))
        return out

@app.route("/")
def hello2():
   return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
