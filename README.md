[*please edit this file according to the needs of your project*]

# Welcome to Axon Client

[*please summarise what your project provides to users*]

## Installation

[*indicate how users can install your project*]

## Getting started

[*indicate how users can use your project*]

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