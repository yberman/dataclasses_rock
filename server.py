#!/usr/bin/env python3
"""
server.py

Serve a list of people.
"""

import csv

from flask import Flask
app = Flask(__name__)

people_by_id = {}
def load_data():
    with open("people.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            people_by_id[row["id"]] = row

@app.route('/')
def people():
    return people_by_id

@app.before_first_request
def main():
    load_data()

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
