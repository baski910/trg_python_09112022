# singleton design patterns allows to return the same instance always
# implementation of singleton pattern

class Singleton:
    __shared_instance = 'some string'
    #num_of_instances = 0
    def __init__(self):
        if Singleton.__shared_instance != 'some string':
            raise Exception('instance already exists')
        else:
            Singleton.__shared_instance = self
        #if Singleton.num_of_instances == 5:
        #    raise Exception('exceeding limit')
        #else:
        #    Singleton.num_of_instances +=1

    @staticmethod
    def getInstance():
        if Singleton.__shared_instance == 'some string':
            Singleton()
        return Singleton.__shared_instance

if __name__ == '__main__':
    s1 = Singleton.getInstance()
    print(s1)
    try:
        s2 = Singleton()
        print(s2)
    except Exception as e:
        print(e)
