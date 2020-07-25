# fmt: off
'''
Probably one of the more common use cases for decorators in Python is logging.
'''
# fmt: on


def my_logger(orig_func):
    """
    This is a decorator.
    It helps keep track of what argument the decorated function is run with.
    """
    import logging

    logging.basicConfig(
        filename="{}.log".format(orig_func.__name__), level=logging.INFO
    )

    def wrapper_function(*args, **kwargs):
        logging.info("Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper_function


def my_timer(orig_func):
    """
    This is a decorator.
    It helps time how long a decoratored function takes to run.
    """
    import time

    def wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper_function


@my_logger
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))


import time


@my_timer
def display_info_slowly(name, age):
    time.sleep(1)
    print("display_info_slowly ran with arguments: ({}, {})".format(name, age))


if __name__ == "__main__":
    display_info("John", 25)  # This creates a `display_info.log` file.
    display_info_slowly("Jane", 30)
