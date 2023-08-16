# pip-cacher
Pip packages cacher

## Description

`pip-cacher` is basically a wrapper for [pypi-mirror](https://github.com/montag451/pypi-mirror) that
let the user create a cache for the index and whls for pip packages.

Just run the container with `docker compose up` and hit it from another machine/container to generate
the cache for all your packages.

## Usage

To run `pip-cacher`, just use `docker compose up`. Also, you could run just the docker container with

```bash
docker run --name ${container_name} --v ${packages_directory}:/pythonCacher/packages lvega23/pip-cacher:latest`
```

Then, from another machine, install the packages with:

```bash
pip install -i http://${pip-cacher-ip}:8000/simple --trusted-host http://${pip-cacher-ip} ${package}
```

Then, the packages cache will appear on the packages directory mounted into the container.