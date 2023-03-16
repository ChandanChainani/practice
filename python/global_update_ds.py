global_dict = {}

global_var = 0

def update_global_dict():
    print("before global_dict: ", global_dict)
    global_dict[0] = 1
    print("after global_dict: ", global_dict)

update_global_dict()

def update_global_var():
    # Will throws error without below line
    # global global_var
    print("before global_var: ", global_var)
    global_var = 1
    print("after global_var: ", global_var)

update_global_var()
