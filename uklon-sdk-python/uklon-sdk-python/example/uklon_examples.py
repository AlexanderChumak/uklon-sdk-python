from src.uklon_client import UklonClient
from src.credentials import Credentials

credentials = Credentials('xxx',
                          'xxx',
                          'xxx',
                          'xxx')



def run_tests():

    print("### Uklon sdk test.")
    print("###")
    #client = UklonClient("localhost", 1192, False, credentials)
    client = UklonClient("www.uklon.com.ua", 80, False, credentials)

    print("###")
    print("### Get products.")
    products = client.getProducts()
    print(products)

    print("###")
    print("### Get me.")
    print(client.me())

    print("###")
    print("### Get user orders.")
    print(client.orders())
