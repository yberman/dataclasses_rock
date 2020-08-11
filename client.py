# TODO
# * make address a nested object
# * make static type checking work

from dataclasses import dataclass
from typing import Mapping, List, Union

from marshmallow import Schema, fields, post_load, exceptions
import requests

JSON = Union[str, int, float, bool, None, Mapping[str, 'JSON'], List['JSON']]

@dataclass
class Person:
    id: int
    name: str
    age: int
    address: str

class PersonSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    age = fields.Int()
    address = fields.Str()

    @post_load
    def make_person(self, data, **kwargs):
        return Person(*data)

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
    for id in sorted(people):
        print(id, people[id])
        

if __name__ == "__main__":
    main()
