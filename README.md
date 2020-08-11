# Dataclasses Rock
Demonstrating the unstoppable awesomeness that is 
[Python Dataclasses](https://docs.python.org/3/library/dataclasses.html). As a 
semi-realistic example we load some objects based on JSON returned by an
server.

The problem we're solving is making a class which can be easily defined, and
serialized/deserialized to and from JSON.

```python
# decoded json
person_json = {"name": "...", "age": "..."}
# create "person" object, with proper fields

# person has corresponding fields
print(person.name)
print(person.age)

# easily serialize "person" object into JSON
'{"name": "...", "age": "..."}'
```

The heart of this is in the `client.py` file. The client-server setup instead
just loading in a file filled with JSON was for a mild amount of  realism.
Would also like to upload to the server from the client, which would exercise
serialization.

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

```python3
python3 client.py
````

## TODO
* In server
    + deal with put requests
* In client
    + make address a nested object
    + get static type checking setup and working
    + put a new person on the server
