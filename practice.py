'''
DECORAOTRS
def div(a, b):
    print(a/b)


def smart_div(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = smart_div(div)
div1(2, 4)
'''

'''
__name__ is a special variable only used to denote the name of module
When the file is currently run __name__ is __main__
However if it is imported in some other file and then that file is imported as module, __name__ is the module name
It can be used to check if it is the first file that is being currently executed - 
if __name__ == "__main__":
    main()
'''

'''
Classes and Objects
Classes are blueprints for Objects
Objects have Attributes(variables) and Behaviour(methods[functions])

class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is ", self.cpu, self.ram)

com1 = Computer("i5", 16)
com2 = Computer("Ryzen", 8)
# __init__ function called by default at the time of Object Creation
# com1 passed as paramter also automatically

Computer.config(com1)
Computer.config(com2)

OR

com1.config()
com2.config()
# In above line com1 gets passed as a parameter to self automatically
'''
