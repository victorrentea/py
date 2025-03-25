
def decorate(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper

@decorate
def function(a,b):
    print(a,b)


if __name__ == "__main__":
    function(1,2)