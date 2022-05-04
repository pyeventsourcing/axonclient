# Python Client for Axon Server

This package provides a Python client for
[Axon Server](https://developer.axoniq.io/axon-server).

## Installation

Use pip to install the stable distribution from the Python Package Index.

    $ pip install axonserver

Please note, it is recommended to install Python packages into a Python virtual environment.

## Getting started

Start an [Axon Server](https://developer.axoniq.io/axon-server).

    $ docker run -d --name my-axon-server -p 8024:8024 -p 8124:8124 axoniq/axonserver axonserver

Construct the `AxonClient` class with a `uri` that includes the host and port of your Axon Server.

```python
from axonclient.client import AxonClient

axon_client = AxonClient(uri='localhost:8024')
```
Call client methods to append and list events in Axon Server.

See the [Python eventsourcing extension project for Axon Server](https://github.com/pyeventsourcing/eventsourcing-axonserver)
for an example of use.

## Developers

After cloning the axonclient repository, set up a virtual
environment and install dependencies by running the following command in the
root folder.

    $ make install

The ``make install`` command uses the build tool Poetry to create a dedicated
Python virtual environment for this project, and installs popular development
dependencies such as Black, isort and pytest.

Add tests in `./tests`. Add code in `./axonclient`.

Run tests.

    $ make test

Check the formatting of the code.

    $ make lint

Reformat the code.

    $ make fmt

Add dependencies in `pyproject.toml` and then update installed packages.

    $ make update-packages
