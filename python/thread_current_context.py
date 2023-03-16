import threading

a = 1
b = 2
c = 3

def d():
    pass

parent = threading.current_thread()

print(parent)
print(dir(parent))
print(parent.__dict__.get('_context',{}))
