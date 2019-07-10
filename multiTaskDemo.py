import multitask 

''' This program demonstartes classical Producer\Consumer using 'multitask' module that implements coroutine'''

def Producer():
    for i in range(10):
        yield i*i

def Consumer():
    print((yield))

multitask.add(Producer())
multitask.add(Consumer())