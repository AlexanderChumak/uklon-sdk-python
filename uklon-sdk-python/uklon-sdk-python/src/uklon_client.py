import http.client
import urllib
import json
from src.oauth import OAuth

class UklonClient(object):

    def __init__(self, baseUrl, port, isSsl, credentials):
        self._baseUrl = baseUrl
        self._port = port
        self._isSsl = isSsl
        self._credentials = credentials
        return super().__init__()

    def getProducts(self):
        return self.makeApiRequest('GET', '/api/v1/products')

    def me(self):
        return self.makeApiRequest('GET', '/api/v1/me')

    def orders(self):
        return self.makeApiRequest('GET', '/api/v1/history/orders/1/2')

    def makeApiRequest(self, method, url):

        refreshToken = self.refreshAuth()
        if self._isSsl:
            conn = http.client.HTTPSConnection(self._baseUrl, self._port)
        else:
            conn = http.client.HTTPConnection(self._baseUrl, self._port)
        conn.connect()

        headers = {"Content-type": "application/json", "Accept": "application/json", "client_id":self._credentials.clientId, 
                   "Authorization" : "Bearer {}".format(refreshToken.accessToken)}

        conn.request(method, url, None, headers)
        response = conn.getresponse()

        print(response.status, response.reason)

        resByte = response.read()
        resStr = str(resByte, 'utf-8')
        return resStr

    def refreshAuth(self):
        if self._isSsl:
            conn = http.client.HTTPSConnection(self._baseUrl, self._port)
        else:
            conn = http.client.HTTPConnection(self._baseUrl, self._port)
        conn.connect()

        headers = {"Content-type": "application/x-www-form-urlencoded", 
                   "Accept": "application/json",
                   "client_id":self._credentials.clientId
                   }
        body =  urllib.parse.urlencode({'username': self._credentials.userName,
                                        'password': self._credentials.password,
                                        'grant_type': 'password',
                                        'client_id': self._credentials.clientId,
                                        'client_secret': self._credentials.clientSecret})

        conn.request('POST', '/api/auth', body, headers)
        response = conn.getresponse()

        print(response.status, response.reason)

        authJson = json.loads(str(response.read(), 'utf-8'))
        auth = OAuth(authJson.get('access_token'), authJson.get('refresh_token'), authJson.get('expires_in'))
        return auth