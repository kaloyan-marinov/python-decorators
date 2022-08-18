import functools


def dec(cls):
    @functools.wraps(cls, updated=())
    class D(cls):
        def d(self):
            print("`method d` says hello")

    return D


# breakpoint()
@dec
class C:
    """Docstring of class C."""

    def c(self):
        print("`method c` says hello")


if __name__ == "__main__":
    # Without applying the `functools.wraps(cls, updated=())` decorator to `D`,
    # the next statements will output the following:
    #   <class '__main__.dec.<locals>.D'>
    #   D
    #   None
    print(C)  # <class '__main__.C'>
    print(C.__name__)  # C
    print(C.__doc__)  # Decostring of class C.

    C().c()  # `method c` says hello
    C().d()  # `method d` says hello
