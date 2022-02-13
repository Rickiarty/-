
from abc import abstractmethod

class Felidae: # 貓科
    # 類別成員
    # 前置單底線為受保護的(protected)成員，無法被外部存取，但可被繼承自己的子類別使用。
    _length = 0 # 身長 in meter
    _weight = 0 # 體重 in kilogram
    # 前置雙底線為私有成員，無法被外部存取，亦不可被繼承自己的子類別使用。
    __name = "X"
    # 前面不加底線(underscore)者為公有的(public)成員，外部可直接存取。
    color = ""

    # 建構子(constructor)方法，將類別實例化為物件時會先被執行一次，初始化。若親類別和類別自身皆未明確定義建構子，Python會預設執行空的建構子。
    def __init__(self, length, weight):
        self._length = length
        self._weight = weight
    
    #抽象的 類別方法(method，類似function，換湯不換藥) 不可被直接執行，必須先繼承類別，並實作其下的抽象方法
    @abstractmethod
    def roar(self):
        pass
    @abstractmethod
    def show_info(self):
        pass


class Lion(Felidae): # 獅子

    #具體的 類別方法(method，類似function，換湯不換藥)，可被直接執行
    # 前面不加底線(underscore)者為公有的(public)方法，外部可直接存取。
    def roar(self):
        return 'Hoaaaaaaar~~~ 吼~~~'
    def show_info(self):
        return self._length, self._weight


class FelisCatus(Felidae): # 家貓
    # 類別成員
    __name = "" # 前置雙底線為私有(private)成員，無法被外部存取，亦不可被繼承自己的子類別使用。
    
    def __init__(self, length, weight, name):
        self._length = length
        self._weight = weight
        self.__name = name

    #具體的 類別方法(method，類似function，換湯不換藥) 可被直接執行
    # 前面不加底線(underscore)者為公有的(public)方法，外部可直接存取。
    def roar(self):
        return '%s: Meow~~~ 喵~~~' % self.__name
    def show_info(self):
        return self._length, self._weight
