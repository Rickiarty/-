"""
W3C School 程式語言免費線上教學網站:
有許多熱門程式語言的入門教學，還可以在網站上直接執行測試、練習，是免費又好用的程式學習資源。
Python tutorial on W3C School:
https://www.w3schools.com/python/
"""

# Python中FOR迴圈的三種用法 & 最常用的群集資料型別LIST

"""
[NOT]
───────────────────────
    A   |   not A
───────────────────────
    T   |       F
───────────────────────
    F   |       T
───────────────────────
"""

# 電腦中的有序collection(群集)，例如list(串列)、array(陣列)、......等，其元素(element)之索引值(index)大多預設由0開始起算，而非從1開始。

list1 = [12, 34, 5, 678, 90]
list2 = [] # list2一開始是空的

# FOR迴圈用法 1
# 將list1中大於或等於40的項目依序附加到list2的最後一個去
for i in range(len(list1)):
    if list1[i] >= 40:
        list2.append(list1[i])

# FOR迴圈用法 2
# 依序列出目前在list2中的項目(元素)
print('目前在list2中的項目:')
for item in list2:
    print(item, end=',\t')
print("\n目前在list1中卻不在list2中的項目:")
# 依序列出目前在list1中卻不在list2中的項目(元素)
for item in list1:
    if not item in list2:
        print(item, end=",\t")
print()

# FOR迴圈用法 3
# 以索引(index)配內容值(value)的方式依序列出list1中的項目
for index, value in enumerate(list1):
    print("list1[%d] = %d" % (index, value))
