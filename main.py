import truss
from pathlib import Path
import requests

# Load the truss
# tr = truss.load("./falcon_7b_truss")

# Run local prediction if you have a GPU
# output = tr.predict({"prompt": "Hi there how are you?"})
# print(output)

# Setup docker
# command = tr.docker_build_setup(build_dir=Path("./falcon_7b_truss"))
# print(command)

# Run inference again model microservice
# data = {"prompt": "Whats the most interesting thing about a falcon?"}
# res = requests.post("http://127.0.0.1:8080/v1/models/model:predict", json=data)
# print(res.json())