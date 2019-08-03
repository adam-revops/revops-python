# A python module for integrating RevOps

[RevOps](https://www.revops.io)

## Installation

Install from PyPi using pip, a package manager for Python.

```
pip install revops
```

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, you can [download the source code
(ZIP)](https://github.com/revops-io/revops-python/zipball/master "revops-python
source code") for `revops-python`, and then run:

    python setup.py install

## Getting Started

Create a `RevOpsAPI` client.

```python
  from revops.api import RevOpsAPI
  api = RevOpsAPI()
```

### Authentication

Get your API token from your RevOps instance. Set the token to REVOPS_API_KEY in your environment variables.

    export REVOPS_API_KEY="xxxxxxxxxxxxxxxxxxxxxxx"

```python
  from revops.api import RevOpsAPI
  api = RevOpsAPI()
