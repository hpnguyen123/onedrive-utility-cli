import os
import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
from onedrivesdk.helpers.resource_discovery import ResourceDiscoveryRequest

redirect_uri = 'http://localhost:8080'
discovery_uri = 'https://api.office.com/discovery/'
auth_server_url='https://login.microsoftonline.com/common/oauth2/authorize'
auth_token_url='https://login.microsoftonline.com/common/oauth2/token'


class Client:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.http = onedrivesdk.HttpProvider()
        self.auth = onedrivesdk.AuthProvider(
                                        self.http,
                                        self.client_id,
                                        auth_server_url=auth_server_url,
                                        auth_token_url=auth_token_url)

        self.auth_url = self.auth.get_auth_url(redirect_uri)


    def authenticate(self, cache):
        assert cache

        code = GetAuthCodeServer.get_auth_code(self.auth_url, redirect_uri)
        self.auth.authenticate(code, redirect_uri, self.client_secret, resource=discovery_uri)

        # If you have access to more than one service, you'll need to decide
        # which ServiceInfo to use instead of just using the first one, as below.
        service_info = ResourceDiscoveryRequest().get_service_info(self.auth.access_token)[0]
        self.auth.redeem_refresh_token(service_info.service_resource_id)

        print(service_info.service_resource_id)

        # Save the session for later
        self.auth.save_session(path=cache)


    def load_session(self, cache):
        assert cache and os.path.isfile(cache)

        self.auth.load_session(path=cache)
        self.auth.refresh_token()


    def get_onedrive_client(self):
        return onedrivesdk.OneDriveClient('https://microsoft-my.sharepoint.com/_api/v2.0/', self.auth, self.http)
