from src.uklon_client import UklonClient
from src.credentials import Credentials


cr = Credentials('xxx')

def get_producst():
    client = UklonClient("www.uklon.com.ua", cr)
    products = client.getProducts()
    print(products)
    return products