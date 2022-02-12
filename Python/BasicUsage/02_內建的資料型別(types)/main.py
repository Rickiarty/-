"""
W3C School 程式語言免費線上教學網站:
有許多熱門程式語言的入門教學，還可以在網站上直接執行測試、練習，是免費又好用的程式學習資源。
Python tutorial on W3C School:
https://www.w3schools.com/python/
"""

#print("Python's Built-in Data Types(預設內建好的資料型別)")

'''
Python's Built-in Data Types(預設內建好的資料型別)

Text Type:	str(字串, string)
Numeric Types:	int(整數, integer), float(浮點數, floating number), complex(複數, complex number)
Sequence Types:	list(有序而可變), tuple(有序而不可變), range(範圍)
Mapping(對應) Type:	dict(兩種資料型別之間的對應關係，dictionary，勿翻譯成字典)
Set Types:	set(模擬數學與邏輯學上的「集合」(set)，無序而可變，且不重複計算元素(element)), frozenset(無序而不可變，且不重複計算元素)
Boolean Type:	bool(模擬(邏輯學上的)成立值True/False，翻譯成(邏輯上的)對/錯，而不是真/假)
Binary Types:	bytes(位元組), bytearray, memoryview
'''

# 10001010, 8 bits = 1 byte

# collection(群集)

# set(集合)
# {1, 2, 3}
# {2, 1, 3}
# {1, 1, 1, 2, 2, 3}

# list(串列)
# [1, 2, 3]
# [2, 1, 3]
# [1, 1, 1, 2, 2, 3]

# tuple(元組)
# (1, 2, 3)
# (1, 1, 1, 2, 2, 3)

# mapping / dictionary
# {1:"John", 2:"Mary", 3:'Tom', 4:'Mary'}
# key(鍵):value(值)

s1 = 'Martin'
print(s1, end='\t')
print(type(s1))

n1 = 100
print(n1, end='\t')
print(type(n1))

f1 = 3.1415926
print(f1, end='\t')
print(type(f1))

com1 = 4 + 3j # (= 4 + 3i in mathematics)
print(com1, end='\t')
print(type(com1))

b1 = True
b2 = False
print(b1, end='\t')
print(type(b1))
print(b2, end='\t')
print(type(b2))

list1 = [1, 2, 2, 3, 3, 3]
print(list1, end='\t')
print(type(list1))

tuple1 = (1, 2, 2, 3, 3, 3)
print(tuple1, end='\t')
print(type(tuple1))

set1 = {1, 2, 2, 3, 3, 3}
print(set1, end='\t')
print(type(set1))

dict1 = {1:"John", 2:"Mary", 3:'Tom', 4:'Mary'}
print(dict1, end='\t')
print(type(dict1))
