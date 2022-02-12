"""
W3C School 程式語言免費線上教學網站:
有許多熱門程式語言的入門教學，還可以在網站上直接執行測試、練習，是免費又好用的程式學習資源。
Python tutorial on W3C School:
https://www.w3schools.com/python/
"""

# 類別(class) 與 物件(object)

"""
需要類別的3個理由：

1. 減少重複：跟 迴圈(loop) 和 function(函式) 等其他程式碼的機制目的相同，都是為了減少重複的程式碼。藉由重複使用寫好的程式碼，減少重複撰寫功能相同的程式碼。
2. encapsulation(封裝) & management：封裝(encapsulate)資料及程式碼，增加程式的安全性，且便於控管。
3. 分門別類(classification)：將程式碼加以分類(classify)，以增加程式碼的清晰度與條理。
"""

from circle import Circle
from cat import Lion, FelisCatus

'''
類別成員(本質上是變數)和類別方法(method，類似function，換湯不換藥)的3種「可存取度屬性」：

public      ：公有的，任何人都可存取。
protected   ：受保護的，繼承自己的子類別方可存取。
private     ：私有的，只有自身可以存取。

除此之外，Python的方法(method)還有4種「本質屬性」：

一般方法：具體方法，類別被實例化為物件後，即可透過個別物件去執行。
抽象方法：在方法前面一行以「@abstractmethod」修飾。不可被直接執行，必須由繼承自己的子類別實作抽象方法底下區塊的內容後，變成具體方法，子類別再經實例化為物件，方可透過個別物件去執行。
靜態方法：在方法前面一行以「@staticmethod」修飾。類別不須被實例化為物件，透過「[類別名稱].[方法名稱]()」即可被如同 function 般執行，形同一般 function，只是透過類別加以包裝及分類，以增加程式碼的清晰度與條理。靜態方法雖不需要額外參數，要用到類別成員或類別中其他方法時，就必須寫出類別全名加上「.」來存取。
類別方法：在方法前面一行以「@classmethod」修飾。基本上同於靜態方法，但靜態方法不須額外參數，類別方法卻需要一個額外參數「cls」，類似一般方法的額外參數「self」，存取類別成員或其他類別方法時可用。
'''

lion1 = Lion(length=1.8, weight=215)
cat1 = FelisCatus(length=0.25, weight=4, name='喵皇')

print(lion1.roar())
print(cat1.roar())

r = 3
print(Circle.calc_area(r))
print(Circle.calc_circumference(r))

circle1 = Circle(2.5)
print(circle1.get_area())
print(circle1.get_circumference())
