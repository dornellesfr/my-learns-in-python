from copy import deepcopy

products = [
  {"nome": "Produto 5", "preco": 10.00},
  {"nome": "Produto 1", "preco": 22.32},
  {"nome": "Produto 3", "preco": 10.11},
  {"nome": "Produto 2", "preco": 105.87},
  {"nome": "Produto 4", "preco": 69.90},
]


def increase_10_percent(arr):
    new_products = deepcopy(arr)
    for product in new_products:
        product["preco"] = round(product["preco"] * 1.10, 2)
    return new_products


def order_by_name(arr):
    array = deepcopy(arr)
    array.sort(key=lambda product: product["nome"], reverse=True)
    return array


def order_by_price(arr):
    array = deepcopy(arr)
    array.sort(key=lambda product: product["preco"])
    return array
