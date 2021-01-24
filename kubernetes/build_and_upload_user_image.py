from pathlib import Path

from dotenv import load_dotenv
import docker
import os

load_dotenv(dotenv_path=Path('.') / 'versions')

print("Building image...")
client = docker.from_env()
client.images.build(path='..', dockerfile='./kubernetes/Dockerfile', tag=os.getenv('USERCODE_DOCKER_TAG'),
                    buildargs={'DAGSTER_VERSION': os.getenv('DAGSTER_VERSION'), 'BASE_IMAGE': os.getenv('BASE_IMAGE')})
print("Done building image. Pushing to Docker Hub...")
for info in client.images.push(os.getenv('USERCODE_DOCKER_TAG'), stream=True, decode=True):
    print(info)
print("Done pushing image")
