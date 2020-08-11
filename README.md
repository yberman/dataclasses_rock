# Dataclasses Rock
Demonstrating the unstoppable awesomeness that is 
[Python Dataclasses](https://docs.python.org/3/library/dataclasses.html). As a 
semi-realistic example we load some objects based on JSON returned by an
server.

## Instruction

### Instalation

Setup virtualenv, enable it, and download requirements

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

Later you can use the `deactivate` command to leave the virtualenv.

###  Starting and testing the Flask server

```bash
python3 server.py
# in another window...
# get a blob of json from the server
curl -vvv localhost:8080
```

### Using the client

TODO
