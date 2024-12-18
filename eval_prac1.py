def expression_res(expression, variables):
    return eval(expression, variables)

str_input = input("enter expression: ")
variables_input = input("enter varibles in dict: ")
variables = eval(variables_input)

print(expression_res(str_input,variables))

