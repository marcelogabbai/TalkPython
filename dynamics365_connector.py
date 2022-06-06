import adal
import requests
import json


class Dynamics365Connector:
    session = None
    data = None
    page_number = 1
    token = None
    api_root_uri = ''
    client_id = ''
    resource_uri = ''
    authority_uri = ''
    client_secret = ''

    def __init__(self, _client_id, _resource_uri, _authority_uri, _client_secret, _api_root_uri):
        self.client_secret = _client_secret
        self.api_root_uri = _api_root_uri
        self.authority_uri = _authority_uri
        self.resource_uri = _resource_uri
        self.client_id = _client_id
        #self.connect()

    def connect(self):
        context = adal.AuthenticationContext(self.authority_uri, api_version=None)
        self.token = context.acquire_token_with_client_credentials(self.resource_uri, self.client_id,
                                                                   self.client_secret)
        self.session = requests.Session()
        self.session.headers.update(dict(Authorization='Bearer {}'.format(self.token.get('accessToken'))))

    def get_data(self, api_parameters):
        api_url = self.api_root_uri + api_parameters
        r = self.session.get(api_url)
        raw_json = r.content.decode('utf-8')
        results = json.loads(raw_json)
        if self.data is None:
            self.data = results['value']
        else:
            self.data += results['value']
        next_link_key = '@odata.nextLink'
        if next_link_key in results.keys():
            print("Processando pagina: " + str(self.page_number))
            self.page_number += 1
            self.get_data(results[next_link_key])

    def update_data(self, entity, record_id, **kwargs):
        update_url = self.api_root_uri + entity + f"({record_id})"
        if update_url is not None and kwargs is not None:
            params = {}
            params.update(kwargs)
            r = self.session.patch(url=update_url, json=params)
            if r.status_code == 401:
                self.connect()
                if self.token is not None:
                    self.update(entity, record_id, **kwargs)

    def create_data(self, entity_type=None, **kwargs):
        url = self.api_root_uri + entity_type
        if url is not None and kwargs is not None:
            params = {}
            params.update(kwargs)
            if self.session is None:
                self.connect()
                if self.token is not None:
                    self.create_data(entity_type, **kwargs)
                    return
            r = self.session.post(url, json=params)
            if r.status_code == 401:
                self.connect()
                if self.token is not None:
                    self.create_data(entity_type, kwargs)