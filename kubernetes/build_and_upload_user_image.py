from pathlib import Path

from dotenv import load_dotenv
import docker
import os

load_dotenv(dotenv_path=Path('.') / 'versions')

print("Building image...")

local_tag = os.getenv('USERCODE_DOCKER_REPO')
remote_tage = local_tag + ':' + os.getenv('DAGSTER_VERSION')

client = docker.from_env()
image, _ = client.images.build(path='..',
                               dockerfile='./kubernetes/Dockerfile',
                               tag=local_tag,
                               buildargs={'DAGSTER_VERSION': os.getenv('DAGSTER_VERSION'),
                                          'BASE_IMAGE': os.getenv('BASE_IMAGE')})
print("Done building image")
print("Tagging Image...")
image.tag(local_tag, os.getenv('DAGSTER_VERSION'))
print("Pushing Image to Docker Hub....")
for info in client.images.push(os.getenv('USERCODE_DOCKER_REPO'),
                               tag=os.getenv('DAGSTER_VERSION'),
                               stream=True,
                               decode=True):
    print(info)
print("Done pushing image")
