from models.product import Product
from models.order import Order
from models.retail_client import RetailClient
from models.inventory import Inventory
from datetime import datetime

client = RetailClient("antoni", "peruzynski", "123456", "13, Gliwice", 1)
inventory = Inventory("13, akademicka", "111000222",
                      "14, Gliwice ", "empty", "inventory111@mail.com")
product1 = Product("phone", 2000, datetime(2021, 12, 9), "empty", inventory)
product2 = Product("headphones", 300, datetime(2021, 10, 12),
                   "none", inventory)
order = Order()
order.order_id = 55
order.client = client
order.date = datetime(2021, 1, 13)
order.products = [product1, product2]
order.status = "SEND"

print(order)