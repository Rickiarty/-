"""
W3C School 程式語言免費線上教學網站:
有許多熱門程式語言的入門教學，還可以在網站上直接執行測試、練習，是免費又好用的程式學習資源。
Python tutorial on W3C School:
https://www.w3schools.com/python/
"""

'''
n = 0
while n < 3:
    print('Hello')
    n = n + 1
'''

n = 1
while n <= 100:
    print(n)
    n = n + 1

n = 1
total = 0
while n <= 100:
    total += n # total = total + n
    n += 1 # n = n + 1
print('結果是%d' % total)
print('結果是' + str(total))

"""
A = A [binary operator] B ---(簡寫)---> A [binary operator]= B 
e.g., A = A + B ---(簡寫)---> A += B
"""
