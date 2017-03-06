from src.uklon_client import UklonClient

def get_producst():
    client = UklonClient("www.uklon.com.ua")
    products = client.getProducts()
    print(products)
    return products