# fmt: off
'''
Probably one of the more common use cases for decorators in Python is logging.
'''
# fmt: on

import logging
import time


def input_params_logging(orig_func):
    """
    This is a decorator.
    When applied to a(nother) function,
    this decorator helps keep track of what inputs the decorated function is run with.
    """

    logging.basicConfig(
        # filename=orig_func.__name__ + ".log",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    def wrapper_function(*args, **kwargs):
        logging.info(f"going to execute with args: {args}, and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper_function


def execution_time_printing(orig_func):
    """
    This is a decorator.
    When applied to a(nother) function,
    this decorator helps time how long the decoratored function takes to run.
    """

    def wrapper_function(*args, **kwargs):
        print(f"starting `{orig_func.__name__}`'s execution")

        start_time = time.time()
        result = orig_func(*args, **kwargs)
        final_time = time.time()

        delta_t = final_time - start_time
        print(f"ending `{orig_func.__name__}`'s execution - it took {delta_t} sec")
        return result

    return wrapper_function


@input_params_logging
def display_info(name, age):
    print(f"executing *display_info* with the following inputs: ({name}, {age})")


@execution_time_printing
def display_info_and_sleep(name, age):
    print(
        f"executing *display_info_and_sleep* with the following inputs: ({name}, {age})"
    )
    time.sleep(1)


if __name__ == "__main__":
    # If the call of `logging.basicConfig` above provides a value for `filename`,
    # then the next statement creates a `display_info.log` file.
    display_info("John", 50)

    display_info_and_sleep("Mary", 50)
