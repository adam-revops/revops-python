from revops.resources import APIResource
from revops.schema import AccountSchema
from revops.exceptions import RequestSchemaException

from marshmallow import Schema, fields
from datetime import datetime, timezone

class Account(APIResource):
    _resource = "v1/accounts"
    _metrics = []
    _marshaler = AccountSchema

    status = ""
    email = ""

    def update(self, id, status):
        return self.request(
            data = { 'status': status },
            http_method = "POST",
            sub_resource = f"/{id}"
        )

"""
Defines the records module
revops.usage.records.<action>
"""
class __api_module__(object):

    def __init__(self, api):
        self._api = api

    @property
    def accounts(self):
        return Account(self._api)
