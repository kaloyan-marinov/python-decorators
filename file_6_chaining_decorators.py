import time

from file_5_decorators_practical_examples import my_logger, my_timer


@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print("display_info ran with arguments: ({}, {})".format(name, age))


display_info("Jane", 30)  # outputs ...
# fmt: off
'''
    ```
    display_info ran with arguments: (Jane, 30)
    wrapper_function ran in: 1.004455327987671 sec
    ```

Q: Why does it say "wrapper_function" instead of "display_info"?
A: Realize that
   the chaining of those 2 decorators above the definition of `display_info`
   is equivalent to writing
   `display_info = my_timer(my_logger(display_info))`

Q: So, how do we fix something like this?
A: It's always a good idea to preserve the information of our original function,
   whenever we use decorators. And we can preserve that information by using the
   `functools` module and the `wraps` decorator - namely by decorating each
   `wrapper_function` function with `@functools.wraps(orig_func)`.
   
For more details on that,
see https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
'''
# fmt: on
