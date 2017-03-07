import http.client

class UklonClient(object):
    
    def __init__(self, baseUrl, credentials):
        self._baseUrl = baseUrl
        self._credentials = credentials
        return super().__init__()

    def getProducts(self):
        url = '/api/v1/products'
        conn = http.client.HTTPConnection(self._baseUrl)
        conn.connect()

        headers = {"Content-type": "application/json", "Accept": "application/json", "client_id":self._credentials.clientId}

        conn.request('GET', url, None, headers)
        response = conn.getresponse()

        print(response.status, response.reason)

        resByte = response.read()
        resStr = str(resByte, 'utf-8')
        return resStr
