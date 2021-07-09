def make_counter():

    count = 0
    def inner():

        nonlocal count
        count += 1
        return count

    return inner


counter = make_counter() # 0

counter() # 1
counter() # 2
counter() # 3
...
