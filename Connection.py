import requests
import json


class ApiConnection:
    """

    """
    endpoint = None
    token = None
    headers = None

    def __init__(self, endpoint, token, test_connection=True):

        if endpoint[-1] is not '/':
            endpoint = endpoint + '/'

        self.endpoint = endpoint
        self.token = token
        self.headers = {
            'user-agent': 'TolaApiConnection',
            'Authorization': 'Token ' + token
        }
        # test connection
        if test_connection:
            try:
                self.get("api")
            except:
                raise Exception("Connection failed")

    def get(self, route):
        url = self.endpoint + route
        return self.get_response(url, use_endpoint=False)

    def get_response(self, url, use_endpoint=True):
        if use_endpoint:
            url = self.endpoint + url
        return requests.get(url, headers=self.headers, verify=False)

    def get_json(self, url, use_endpoint=True):
        if use_endpoint:
            url = self.endpoint + url
        response = requests.get(url, headers=self.headers, verify=False)
        content = response.content.decode('utf-8')

        if response.status_code != 200:
            raise Exception("Wrong status code (%d)" % response.status_code)

        try:
            results = json.loads(content)
        except:
            # Catch the cryptic parse error and throw our own exception if something goes wrong
            raise Exception("No valid JSON Response")

        return results
