def blue_method(id, task):
    big_ugly_method(id, task)


def green_method(id, task):
    big_ugly_method(id, task)


def yellow_method(id, task):
    big_ugly_method(id, task)


def red_method(id, task):
    big_ugly_method(id, task)


def use_case_323(id, task):
    # TODO The shared called method must execute logic specific for my use-case #323
    big_ugly_method323(id, task)


def big_ugly_method(store_id, task):
    donkey(store_id, task)

    sheep(store_id)


def big_ugly_method323(store_id, task):
    donkey(store_id, task)

    print("Logic just for CR#323 : ", task)
    sheep(store_id)


def donkey(store_id, task):
    print("Donkey Logic 1 ", task, " and ", store_id)
    print(task)
    print("Donkey Logic 3 ", task)


def sheep(store_id):
    print("Sheep Logic 1 ", store_id)
    print("Sheep Logic 2 ", store_id)
    print("Sheep Logic 3 ", store_id)
