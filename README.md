# Python Client for Axon Server

This package provides a Python client for
[Axon Server](https://developer.axoniq.io/axon-server).

## Installation

Use pip to install the stable distribution from the Python Package Index.

    $ pip install axonserver

Please note, it is recommended to install Python packages into a Python virtual environment.

Construct the `AxonClient` class with a `uri` that includes the host and port of your Axon Server.

```python
from axonclient.client import AxonClient

axon_client = AxonClient(uri='localhost:8024')
```
Call client methods to append and list events in Axon Server.

See the [Python eventsourcing extension project for Axon Server](https://github.com/pyeventsourcing/eventsourcing-axonserver)
for an example of use.


## Developers

Clone the GitHub repo and the use the following `make` commands.

Install Poetry.

    $ make install-poetry

Install packages.

    $ make install

Start Axon Server for aggregates.

    $ make start-axon-server-aggregates

Run clients tests for aggregates.

    $ make test-axon-client-aggregates

Stop Axon Server for aggregates.

    $ make stop-axon-server-aggregates

Start Axon Server for DCB.

    $ make start-axon-server-dcb

Run clients tests for DCB.

    $ make test-axon-client-dcb

Stop Axon Server for DCB.

    $ make stop-axon-server-dcb

Check the formatting of the code.

    $ make lint

Reformat the code.

    $ make fmt

Tests belong in `./tests`. Code-under-test belongs in `./axonclient`.

Edit package dependencies in `pyproject.toml`. Update installed packages (and the
`poetry.lock` file) using the following command.

    $ make update
