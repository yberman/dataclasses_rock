# Dataclasses Rock
Demonstrating the unstoppable awesomeness that is Python Dataclasses. As a 
semi-realistic example we load some objects based on JSON returned by an
server.

## Usage

```
# setup virtualenv and download requirements
python -m venv .venv
source .venv/bin/activate
# later you can use the "deactivate" command to leave the virtualenv
pip install -r requirements

# start server
python3 server.py

# in another window...
# get a blob of json from the server
curl -vvv localhost:8080
```
