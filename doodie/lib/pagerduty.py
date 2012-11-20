import json
import requests

class Pagerduty(object):

    def __init__(self, apikey, subdomain):
        self.apikey = apikey
        self.url = "http://%s.pagerduty.com/api/v1" % subdomain
        self.headers = {
            "Content-type": "application/json",
            "Authorization": "Token token=%s" % self.apikey
        }

    def _request(self, path, params={}):
        api_url = "/".join((self.url, path))
        if params:
            r = requests.get(api_url, params=params,
                             headers=self.headers)
        else:
            r = requests.get(api_url, headers=self.headers)

        if r.status_code == requests.codes.ok:
            return(json.loads(r.content))
        else:
            return None

    def incident_count(self, **kwargs):
        path = "incidents/count"
        params = kwargs
        incidents = []

        if kwargs.get("status", None):
            for status in kwargs["status"].split(","):
                params["status"] = status
                incidents.append({
                    "id": status,
                    "value": self._request(path, params).get("total", "unknown")
                })
        else:
            incidents.append({
                "id": "all",
                "value": self._request(path, params).get("total", "unknown")
            })

        return incidents
