#Define a function increment_global_counter() that modifies a global variable counter using the global keyword.

#The function should increase counter by 1 each time it's called.

id=0

def increment_global_counter():
    global id
    id += 1

increment_global_counter()
increment_global_counter()
print(id)
