import time

def logged(prefix):
    def inner(func):
        def wrapper(*args, **kwargs):
            # if (not e logat) raise
            # if (dict/redis.contains(args)) return din redis;
            print(f"{prefix} Before cu param {args}")
            t0 = time.time()
            func(*args, **kwargs)
            t1 = time.time()
            print(f"{prefix} After tool {t1 - t0}")
        return wrapper
    return inner


@logged("Logc")
def function(a,b):
    print(a,b)

if __name__ == "__main__":
    function(1,2)