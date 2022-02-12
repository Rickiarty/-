"""
W3C School 程式語言免費線上教學網站:
有許多熱門程式語言的入門教學，還可以在網站上直接執行測試、練習，是免費又好用的程式學習資源。
Python tutorial on W3C School:
https://www.w3schools.com/python/
"""

#print_hello_N_times(3) # 在定義function前就先行呼叫，Python不認得啦

def print_hello_N_times(n):
    print_str_N_times(n, "Hello!")

def print_str_N_times(n, s1):
    if n <= 0:
        return
    for _ in range(n):
        print(s1)

def print_hello_twice():
    print_hello_N_times(2)

#print_hello_twice()
#print_str_N_times(3, "2022新年快樂！")
#print_hello_N_times(3)

def determinant(a, b, c):
    return b ** 2 - 4 * a * c

#print(determinant(1, 2, 1)) # x^2 + 2x + 1 = 0 之判別式的值

#print(determinant(1, -1, 20)) # x^2 - x + 20 = 0 之判別式的值

#print(determinant(1, -1, -20)) # x^2 - x - 20 = 0 之判別式的值

def sol_determinant(a, b, c):
    d = determinant(a, b, c)
    real_root_exist = (d >= 0)
    ans1 = (-b + d**0.5) / (2*a)
    ans2 = (-b - d**0.5) / (2*a)
    return d, ans1, ans2, real_root_exist

def show_result(d, ans1, ans2, real_root_exist):
    if real_root_exist:
        if d > 0:
            print('兩相異實根', end=':\t')
            print('D=%d, x = %d or x = %d' % (d, ans1, ans2))
        else: # elif d == 0:
            print('有一實根', end=':\t')
            print('D=%d, x = %d' % (d, ans1))
    else: # d < 0
        print('無實數解')

d, ans1, ans2, real_root_exist = sol_determinant(1, 2, 1) # x^2 + 2x + 1 = 0
show_result(d, ans1, ans2, real_root_exist)

d, ans1, ans2, real_root_exist = sol_determinant(1, -1, 20) # x^2 - x + 20 = 0
show_result(d, ans1, ans2, real_root_exist)

d, ans1, ans2, real_root_exist = sol_determinant(1, -1, -20) # x^2 - x - 20 = 0
show_result(d, ans1, ans2, real_root_exist)
