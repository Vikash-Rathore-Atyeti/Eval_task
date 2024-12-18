import json

def apply_discount_to_products(products_json, expression):
    products = json.loads(products_json)
    result = eval(expression, {"products": products})
    return result

products_json = '[{"name": "apple", "price": 30}, {"name": "banana", "price": 20}, {"name": "cherry", "price": 50}]'
expression = "list(map(lambda x: {'name': x['name'], 'price': round(x['price'] * 0.9, 2)}, products))"

output = apply_discount_to_products(products_json, expression)
print(json.dumps(output))
