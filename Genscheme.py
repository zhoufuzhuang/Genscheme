# -*- coding: UTF-8 -*-

import json
from genson import SchemaBuilder
import os
import requests

BASEDIR = os.path.abspath(os.path.dirname(__file__))
con = requests.session()

HOST = "http://xxx.xxx.xxx"
PATH = "/path?key1=value1&key2=value2"
METHOD = "GET"
Body = {}
#生成json文件名字
NAME = "xxx.json"


def build_scheme(_response):
    builder = SchemaBuilder()
    builder.add_object(_response)
    return builder.to_schema()


def get_response(**kwargs):
    resp = con.request(method=METHOD, url=HOST + PATH, **kwargs)
    return json.loads(resp.text)


def build_json_file(filename, scheme):
    with open(BASEDIR + "/" + filename, "w") as f:
        f.write(scheme)
    f.close()


if __name__ == "__main__":
    if METHOD == "GET":
        response = get_response()
    elif METHOD == "POST":
        repsonse = get_response(data = json.dumps(Body))
    schema_text = build_scheme(response)
    scheme = json.dumps(schema_text, indent=4)
    build_json_file(NAME, scheme)
