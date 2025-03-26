global_var = "value of global var"

class MyClass:
    def __init__(self):
        self.value = 10

    def check_value(self):
        if self.value > 5:
            print("Value is greater than 5")
        elif self.value == 5:
            print("Value is 5")
        else:
            print("Value is less than 5")

def assert_example(value):
    assert value == True
    print("passed!")

def try_except_example():
    try:
        print("dividing 10/0")
        x = 10 / 0
    except ZeroDivisionError:
        print("indivisible")
    finally:
        print("divisible")

def loop_example():
    for i in range(3):
        print(f"looping {i}")

def while_example():
    count = 0
    while count < 3:
        print(f"Count: {count}")
        count += 1

square = lambda x: x * x
print(f"Square of 4 is: {square(4)}")

def modify_global():
    global global_var
    global_var = "global var"
    print(global_var)

def outer_function():
    outer_var = "Outer var"
    def inner_function():
        nonlocal outer_var
        outer_var = "Nonlocal var"
        print(outer_var)
    inner_function()

def pass_example():
    pass

def break_continue_example():
    for i in range(3):
        if i == 2:
            continue
        if i == 3:
            break
        print(i)

def delete_example():
    del_var = "del var"
    print(del_var)
    del del_var
    try:
        print(del_var)
    except NameError:
        print("Variable 'my_var' is deleted.")

def main():
    obj = MyClass()
    obj.check_value()

    assert_example(True)
    try_except_example()
    loop_example()
    while_example()
    modify_global()
    outer_function()
    pass_example()
    break_continue_example()
    delete_example()

if __name__ == "__main__":
    main()
