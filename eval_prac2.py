import json

def eval_expression(json_data, expression):
    inventory = json.loads(json_data)
    result = eval(expression, inventory)
    return result

inventory_json = '{"item1": 50, "item2": 30, "item3": 100}'
expression = "item1 if item1 > 40 else item2"

print(eval_expression(inventory_json, expression))

