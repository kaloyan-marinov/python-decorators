import time

from file_5_decorators_practical_examples import (
    input_params_logging,
    execution_time_printing,
)


@execution_time_printing
@input_params_logging
def display_info_and_sleep(name, age):
    print(
        f"executing *display_info_and_sleep* with the following inputs: ({name}, {age})"
    )
    time.sleep(1)


if __name__ == "__main__":
    display_info_and_sleep("John", 60)

    # fmt: off
    '''
    The previous statement outputs
        ```
        starting `wrapper_function`'s execution
        2021-06-08 20:25:55,887 - root - INFO - going to execute with args: ('John', 60), and kwargs: {}
        executing *display_info_and_sleep* with the following inputs: (John, 60)
        ending `wrapper_function`'s execution - it took 1.0026001930236816 sec
        ```

    Q: Why does it say "wrapper_function" instead of "display_info_and_sleep"?
    A: Realize that
        chaining those 2 decorators above the definition of `display_info_and_sleep`
        is equivalent to writing
        ```
        display_info_and_sleep = execution_time_printing(
            input_params_logging(display_info_and_sleep)
        )
        ```

    Q: So, how do we fix something like this?
    A: It's always a good idea to preserve the information of our original function,
        whenever we use decorators. And we can preserve that information by using the
        `functools` module and the `wraps` decorator - namely by decorating each
        `wrapper_function` function with `@functools.wraps(orig_func)`.
    
    For more details on that,
    see https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
    '''
    # fmt: on
