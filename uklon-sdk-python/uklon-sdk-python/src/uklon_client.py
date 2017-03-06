import http.client

class UklonClient(object):
    
    def __init__(self, baseUrl):
        self._baseUrl = baseUrl
        return super().__init__()

    def getProducts(self):
        url = '/api/v1/products'
        conn = http.client.HTTPConnection(self._baseUrl)
        conn.connect()
        conn.request('GET', url)
        response = conn.getresponse()

        print(response.status, response.reason)

        resByte = response.read()
        resStr = str(resByte, 'utf-8')
        return resStr
