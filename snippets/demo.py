# def greet_user(username, sex='man'): 
#     """show simple 问候语"""  
#     print(f"Hello! {username}，you are {sex}")

# greet_user('max')

# def greet_user(sex='man'): 
#     """show simple 问候语"""  
#     print(f"Hello! you are {sex}")

# # greet_user()

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\n The following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []

# print_models(unprinted_designs,completed_models)
# show_completed_models(completed_models)

# greet_user()

# def print_models():
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models():
#     print("\n The following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] 
# completed_models = []

# print_models()
# show_completed_models()

def make_pizza(*toppings):
    """print customer's toppings"""
    print(len(toppings))

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers')