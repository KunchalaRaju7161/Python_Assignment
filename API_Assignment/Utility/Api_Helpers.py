import json
from logging import getLogger

import requests

log = getLogger()


def get(url, head):
    log.info("Getting url : " + url)
    return requests.get(url, headers=head)


def get_filtered(url, param, head):
    log.info("Getting url : " + url)
    return requests.get(url, params=param, headers=head)


def post(url, request_json):
    log.info("Post url : " + url)
    log.info("Request body : " + json.dumps(request_json))
    return requests.post(url, json=request_json)


def post_Task(url, request_json, head):
    log.info("Post url : " + url)
    log.info("Request body : " + json.dumps(request_json))
    return requests.post(url, json=request_json, headers=head)


def put(url, request_json, headers=None):
    if headers is None:
        headers = {}
    log.info("Put url:" + url)
    log.info("Request body: " + json.dumps(request_json))
    return requests.put(url, json=request_json, headers=headers)


def delete(url, headers=None):
    if headers is None:
        headers = {}
    log.info("Delete url:" + url)
    return requests.delete(url, headers=headers)
