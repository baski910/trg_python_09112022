#__all__ = ['addnum','divnum'] # restrict functions to be imported by from modulename import * directive
def addnum(a,b):
    return a+b

def divnum(a,b):
    return a/b

#def sayhello():
#    print("helloworld")

# __name__ - returns name of the current namespace
# __name__ will be equal to __main__ in currently executing script
#          will be equal to namespace in calling script

if __name__ == '__main__':
    print("calling from module:",__name__) 
    print("calling from module:",addnum(50,5))
    print("calling from module:",divnum(50,5))