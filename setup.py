from setuptools import setup
from os import path

# read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="numerai-cli",
    version="1.1.3",
    description="A library for deploying Numer.ai Prediction Nodes.",
    url="https://github.com/numerai/numerai-cli",
    author="Numer.ai",
    author_email="contact@numer.ai",
    license="MIT",
    packages=["numerai"],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6.0",
    install_requires=[
        "click>=7",
        "boto3",
        "botocore",
        "numerapi>=2.4.5",
        "colorama",
        "requests",
        "azure-identity",
        "azure-mgmt-subscription",
        "azure-mgmt-containerregistry",
        "azure-containerregistry",
        "azure-data-tables",
        "azure-mgmt-storage",
        "google-cloud-storage",
        "google-cloud-run",
        "google-cloud-artifact-registry",
        "google-cloud-logging",
    ],
    entry_points={
        "console_scripts": ["numerai=numerai:main"],
    },
)



#executer ça avant le (3) dans le README
# 1. Installer le moteur Docker
#sudo apt update
#sudo apt install -y docker.io

# 2. Démarrer dockerd en arrière-plan
#sudo dockerd > /tmp/dockerd.log 2>&1 &
#sleep 2

# 3. Vérifier que le démon tourne
#docker info
#docker run hello-world