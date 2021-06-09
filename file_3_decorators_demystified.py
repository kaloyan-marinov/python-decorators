def decorator_function(original_function):
    def wrapper_function():
        print("executing *wrapper_function*")
        print(
            "concluding *wrapper_function*'s execution,"
            + f" by going on to run the `{original_function.__name__}` function"
        )
        original_function()

    return wrapper_function


# The following two code-blocks are identical to each other:

# - block A
# fmt: off
'''
def display():
	print("executing *display*")

display = decorator_function(display)


if __name__ == "__main__":
    display()
'''
# fmt: on

# - block B
@decorator_function
def display():
    print("executing *display*")


if __name__ == "__main__":
    display()
