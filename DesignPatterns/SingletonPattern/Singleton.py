class Singleton:
    __instance = None
    temp = 0

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):

        if Singleton.__instance != None:
            raise Exception("This is a singleton class")
        else:
            Singleton.__instance = self

s = Singleton()
s.temp = 10
print(s)

p = Singleton.getInstance()
p.temp = 20
print(p.temp)