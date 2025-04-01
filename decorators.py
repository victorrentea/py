
from time import sleep, time

def timed(*,name):
    def inner(func):
        """
        Decorator that times the execution of a function and prints the time taken.
        """
        def wrapper(*args, **kwargs):
            t0 = time()
            print(f"Inainte: Execution of {name} started")
            result = func(*args, **kwargs) # call the decorated function

            t1 = time()
            # config = args[0]
            print(f"Dupa: Execution of {name} time: {t1-t0} seconds")
            return result
        return wrapper
    return inner

@timed(name="one")
def function1(a,b):
    print("one",a,b)
    sleep(1)

@timed(name="two")
def function2(a,b):
    print("two",a,b)
    sleep(1)


if __name__ == "__main__":
    function1(1,2)
    function2(1,2)

