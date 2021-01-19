from datetime import datetime, timezone
from urllib.error import HTTPError

import json


class APIResource(object):
    _api = None
    _data = ''
    _resource = None

    def __init__(self, api, **kwargs):
        self._api = api
        for key, value in kwargs.items():
            setattr(self, key, value)

    def request(self,
        data = None,
        api = None,
        sub_resource = "",
        http_method = "GET",
        ):
        if api != None:
            self._api = api
        if data != None:
            self._data = data

        if self._resource == None:
            raise Exception("Unable to send request, no _resource defined for {}".format(self))

        response = self._api.request(
            http_method = http_method,
            data = self._data,
            api_resource = "{}{}".format(self._resource, sub_resource),
        )

        if response.status_code == 400:
            raise HTTPError(
                code=response.status_code,
                url=response.url,
                fp=None,
                msg=response.content,
                hdrs=response.headers
            )

        if response.status_code == 204:
            return None

        parsed = json.loads(response.content)

        return parsed

    def get_current_time(self):
        return datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
