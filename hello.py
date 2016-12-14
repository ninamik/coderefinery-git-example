def say_something(something):
    if something:
        print(''.join(reversed(something)))
    else:
        print("Hello World!")
