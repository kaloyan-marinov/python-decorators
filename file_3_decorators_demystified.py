def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        original_function()

    return wrapper_function


# The following two blocks A and B are identical to each other:

# - block A
# fmt: off
'''
def display():
	print('`display` function ran')

display = decorator_function(display)

display()
'''
# fmt: on

# - block B
@decorator_function
def display():
    print("display function ran")


display()
