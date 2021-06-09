def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(
            "concluding *wrapper_function*'s execution,"
            + f" by going on to execute the `{original_function.__name__}` function"
        )
        original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_info(name, age):
    print(f"executing *display_info* with the following inputs: ({name}, {age})")


if __name__ == "__main__":
    display_info("John", 40)

    print(display_info.__name__)  # outputs `wrapper_function` ...
    # ... - the comment at the bottom of file_6_chaining_decorator.py explains how to
    # fix that.
