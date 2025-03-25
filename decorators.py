def logged(prefix):
    def inner(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} Before")
            func(*args, **kwargs)
            print(f"{prefix} After")
        return wrapper
    return inner


@logged("Log")
def function(a,b):
    print(a,b)


if __name__ == "__main__":
    function(1,2)