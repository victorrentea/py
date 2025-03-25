def blue_method(id, task):
    small_and_beautiful(id, task, "RO")

def green_method(id, task):
    small_and_beautiful(id, task, "RO")

def yellow_method(id, task):
    small_and_beautiful(id, task, "RO")

def red_method(id, task):
    small_and_beautiful(id, task, "RO")

def use_case_323(id, task):
    # TODO The shared called method must execute logic specific for my use-case #323
    small_and_beautiful(id, task, 'BG')


def small_and_beautiful(store_id, task, country):
    horse(store_id, task)

    if country in ['RO', 'BG', 'HU']:
        print(f"Logic just for {country} : ", task)
    else:
        raise Exception("Country not supported, dar WOW!")
    
    sheep(store_id)

def sheep(store_id):
    print("Sheep Logic 1 ", store_id)
    print("Sheep Logic 7 asd", store_id)
    print("Sheep Logic 241as ", store_id)

def horse(store_id, task):
    print("Donkey Logic 1 ", task, " and ", store_id)
    print("Donkey Logic 1 ", task, " and ", store_id)
    print(task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logonkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logonkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logonkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logonkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)
    print("Donkey Logic 3 ", task)


use_case_323(1, 2)
red_method(1,2)