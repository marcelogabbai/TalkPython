import json

from dynamics365_connector import Dynamics365Connector

# Global configs.
CLIENT_ID = 'e13283bd-2f2b-4497-af9f-1a6ccb1de4c2'
RESOURCE_URI = 'https://origoenergiaprd.crm2.dynamics.com'
AUTHORITY_URI = 'https://login.microsoftonline.com/263c5ac6-10e8-4d2e-884b-d30a1ecf80dc'
CLIENT_SECRET = 'e~K16FkM30CtWRObj2SRSUR3683w3c.__0'
request_uri_root = 'https://origoenergiaprd.api.crm2.dynamics.com/api/data/v9.2/'
connector = Dynamics365Connector(CLIENT_ID, RESOURCE_URI, AUTHORITY_URI, CLIENT_SECRET, request_uri_root)
# Get an access token.

# Request image.
"""
request_uri_params = "contacts?$select=fullname,contactid&$filter=contains(fullname,'marcelo bassi')"
connector.get_data(request_uri_params)
results = connector.data
for index,dados in enumerate(results, start=1):
    last_name = "Bassi " + str(index)
    connector.update("contacts", dados['contactid'], firstname="Teste do ", lastname=last_name)
"""
connector.create_data("contacts",firstname="Marcelo",lastname="Gabbai",emailaddress1="marcelo@i4d.com.br",mobilephone="(11)98353-9585")