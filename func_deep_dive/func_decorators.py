def simple_deco(func):
    print("Decorator is running")
    return func

@simple_deco
def print_hello():
    print("Hello World")

# print_hello()

def add_exclamation(func):
    def wrapper():
        return f" {func} !!!"
    return wrapper

@add_exclamation
def print_hii():
    return "Hi, I'm a function"

print_hii
