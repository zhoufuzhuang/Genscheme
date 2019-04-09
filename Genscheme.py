# -*- coding: UTF-8 -*-

import json
from genson import SchemaBuilder
import os
import requests
import yaml

BASEDIR = os.path.abspath(os.path.dirname(__file__))
con = requests.session()

HOST = "http://xxx.xx.xx"


def get_request_config():
    f = open(BASEDIR + '/request.yaml', 'r')
    re = f.read()
    res = yaml.load(re)
    f.close()
    return res


def build_scheme(_response):
    builder = SchemaBuilder()
    builder.add_object(_response)
    return builder.to_schema()


def get_response(method, path, **kwargs):
    resp = con.request(method=method, url=HOST + path, **kwargs)
    return resp


def build_json_file(filename, scheme):
    with open(BASEDIR + "/" + filename, "w") as f:
        f.write(scheme)
    f.close()


def run(method, path, name, **kwargs):
    response = get_response(method, path, **kwargs)
    if response.status_code == 200:
        schema_text = build_scheme(json.loads(response.text))
        scheme = json.dumps(schema_text, indent=4)
        build_json_file(name + ".json", scheme)
    else:
        print u"%s接口报错：%s\n" % (name, response.status_code)


def main():
    res = get_request_config()
    for r in res:
        path = r.get('url')
        method = r.get('method')
        name = r.get('name')
        body = r.get('body', {})
        try:
            if method == "GET":
                run(method, path, name)
            elif method == "POST":
                run(method, path, name, data=json.dumps(body))
        except Exception as e:
            print e


if __name__ == "__main__":
    main()
