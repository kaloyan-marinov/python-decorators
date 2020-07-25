def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


if __name__ == "__main__":
    display_info("John", 25)
    print(display_info.__name__)  # outputs `wrapper_function`
