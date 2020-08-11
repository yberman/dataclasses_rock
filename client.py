#!/usr/bin/env python3
"""
client.py

Get a list of people from the server and turn them into objects.
"""

from dataclasses import dataclass, field
import re
from typing import Mapping, List, Union

from marshmallow import Schema, fields, post_load, exceptions, ValidationError
import requests

JSON = Union[str, int, float, bool, None, Mapping[str, 'JSON'], List['JSON']]

@dataclass
class Address:
    street: str
    city: str
    state: str
    zip: int

class AddressField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return f"{value.street}\n{value.city}, {value.state} {value.zip}"

    def _deserialize(self, value, attr, data, **kwargs):
        addr = value.split("\n")
        if len(addr) == 2:
            m = re.match("([a-zA-Z ]+), ([a-zA-Z]+) ([0-9]+)", addr[1])
            if m:
                return Address(addr[0], m.group(1), m.group(2), int(m.group(3)))
        raise ValidationError(f"Could not parse address {value}")

@dataclass
class Person:
    id: int
    name: str
    age: int
    address: "Address"

class PersonSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    age = fields.Int()
    address = AddressField()

    @post_load
    def make_person(self, data, **kwargs):
        return Person(**data)


def download() -> JSON:
    resp = requests.get("http://localhost:8080")
    return resp.json()


def main():
    people = {}
    people_json = download()
    schema = PersonSchema()
    for key in people_json:
        try:
            people[key] = schema.load(people_json[key])
        except exceptions.ValidationError as e:
            print(f'id={key} error{e}')
        if key in people:
            print(people[key])
    for id in sorted(people):
        print(id, people[id])
        

if __name__ == "__main__":
    main()
