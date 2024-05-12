# decorators is @login required decorator like mosttly used in django.
def greet(fx):
    def mfx(*args, **kwargs):
        print('Hello Thanks for Adding The Shit')
        fx(*args, **kwargs)
        print('Bye Bye NIgga')
    return mfx



@greet
def add(a,b):
    print(a+b)
#the function which takes input from the programmer it requires args and kwargs to pass that arguments.





@greet
def hello():
    print('HEllo World')

hello()

add(1,3)

