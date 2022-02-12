#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime # 引用Python標準程式庫中的 datetime 模組

"""
W3C School 程式語言免費線上教學網站:
有許多熱門程式語言的入門教學，還可以在網站上直接執行測試、練習，是免費又好用的程式學習資源。
Python tutorial on W3C School:
https://www.w3schools.com/python/
"""

# 例外(exception)處理、基本檔案存取與CLI輸入

'''
The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

'''
try:
    value = input('請輸入一個數值:')
    n = int(value)
    print(n)
except Exception as ex:
    print(str(ex))
'''

# 檔案讀取方法 1，較不安全，容易造成檔案關閉不正常等嚴重後果，且步驟較複雜，但使用起來較有彈性。
f = None
try:
    f = open("demofle.txt", "r", encoding="utf-8") # "r"僅允許[讀取]檔案內容，不會真正影響電腦系統中的檔案內容，讀檔時發生失誤也影響不大。
    text = f.read()
    print(text)
except Exception as ex:
    print(str(ex))
finally:
    if f != None:
        f.close()

# 檔案讀取方法 2，較安全也較簡易，但較不彈性，使用情境複雜時不好用。
try:
    with open("demofile.txt", "r", encoding="utf-8") as f: # "r"僅允許[讀取]檔案內容，不會真正影響電腦系統中的檔案內容，讀檔時發生失誤也影響不大。
        text = f.read()
        print(text)
except Exception as ex:
    print(str(ex))

# 檔案寫入方法 1，較不安全，容易造成檔案關閉不正常等嚴重後果，且步驟較複雜，但使用起來較有彈性。
f = None
try:
    f = open("demofile.txt", "a", encoding="utf-8") # "a"為[附加]資料至檔案尾端，"w"為[覆寫]掉檔案原本內容。兩者皆會真正影響電腦系統中的檔案內容，必須小心使用。
    timestamp = datetime.datetime.now() # 取得程式執行到這一行時的時間及日期
    f.write("\n" + str(timestamp))
except Exception as ex:
    print(str(ex))
finally:
    if f != None:
        f.close()

# 檔案寫入方法 2，較安全也較簡易，但較不彈性，使用情境複雜時不好用。
try:
    with open("demofile.txt", "a", encoding="utf-8") as f: # "a"為[附加]資料至檔案尾端，"w"為[覆寫]掉檔案原本內容。兩者皆會真正影響電腦系統中的檔案內容，必須小心使用。
        timestamp = datetime.datetime.now() # 取得程式執行到這一行時的時間及日期
        f.write("\n" + str(timestamp))
except Exception as ex:
    print(str(ex))
