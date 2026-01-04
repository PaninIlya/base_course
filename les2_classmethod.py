class MyClass:
    counts = 0

    def __init__(self):
        MyClass.counts = MyClass.counts + 1
    
    @classmethod#метод самого класса, можем дергать методы класса через сам класс, а не экземпляр
    def classmethod(cls): #cls - ключевое слово (как self)
        print(cls.counts)


MyClass.classmethod()
my1 = MyClass()
my2 = MyClass()
my3 = MyClass()

MyClass.classmethod()

my3.classmethod()