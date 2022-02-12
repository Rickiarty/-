"""
W3C School 程式語言免費線上教學網站:
有許多熱門程式語言的入門教學，還可以在網站上直接執行測試、練習，是免費又好用的程式學習資源。
Python tutorial on W3C School:
https://www.w3schools.com/python/
"""

# IF-ELIF-ELSE condition, indentation, and 2 logical operators(OR, AND) 

"""
[AND]
───────────────────────────────
    A   |   B   |   A and B
───────────────────────────────
    T   |   T   |       T
───────────────────────────────
    T   |   F   |       F
───────────────────────────────
    F   |   T   |       F
───────────────────────────────
    F   |   F   |       F
───────────────────────────────

─*─*─*─*─*─*─*─*─*─*─*─*─*─*─*─*─*─

[OR]
───────────────────────────────
    A   |   B   |   A or B
───────────────────────────────
    T   |   T   |       T
───────────────────────────────
    T   |   F   |       T
───────────────────────────────
    F   |   T   |       T
───────────────────────────────
    F   |   F   |       F
───────────────────────────────
"""

# A and B or C = A and (B or C)，由於OR邏輯運算子優先權高於AND邏輯運算子，一般來說會這樣定義優先權高低。
# 但Python定義的運算子優先權與上述相反，故 A and B or C = (A and B) or C，測試檔案如同資料夾中的 test.py。
# 如果不想出問題，最簡單的做法就是使用成對的小括號「()」強制明確地要求運算順序，便不擔心出差錯。
"""
「(A and B) or C」
(在邏輯上)不等價於
「A and (B or C)」
"""

atm_A = 1.56 #大氣壓
atm_B = 2.37 #大氣壓
temperature_A_Celsius = 27.3 #攝氏溫度
temperature_B_Celsius = 20.8 #攝氏溫度

print('atm of gas A = ' + str(atm_A))
print("atm of gas B = " + str(atm_B))

if atm_A > atm_B:
    print('A氣體氣壓大於B氣體氣壓。')
else: # 小於或等於
    print('A氣體氣壓小於或等於B氣體氣壓。')

if atm_A < atm_B:
    print('A氣體氣壓小於B氣體氣壓。')
else: # 大於或等於
    print('A氣體氣壓大於或等於B氣體氣壓。')

if atm_A >= atm_B:
    print('A氣體氣壓大於或等於B氣體氣壓。')
else: # 小於
    print('A氣體氣壓小於B氣體氣壓。')

if atm_A <= atm_B:
    print('A氣體氣壓小於或等於B氣體氣壓。')
else: # 大於
    print('A氣體氣壓大於B氣體氣壓。')

if atm_A > atm_B:
    print('A氣體氣壓大於B氣體氣壓。')
elif atm_A < atm_B: # else if
    print('A氣體氣壓小於B氣體氣壓。')
else: # 等於
    print('A氣體氣壓等於B氣體氣壓。')

if atm_A < atm_B and temperature_A_Celsius < temperature_B_Celsius:
    print('B氣體氣壓和溫度皆大於A氣體。')
else:
    print('並非B氣體氣壓和溫度皆大於A氣體。')

if atm_A < atm_B or temperature_A_Celsius < temperature_B_Celsius:
    print('B氣體氣壓或溫度大於A氣體。')
else:
    print('B氣體氣壓和溫度皆不大於A氣體。')

if atm_A == atm_B:
    print('A氣體氣壓等於B氣體氣壓。')
else: # 不相等
    print('A氣體氣壓不等於B氣體氣壓。')

if atm_A != atm_B:
    print('A氣體氣壓不等於B氣體氣壓。')
else: # 相等
    print('A氣體氣壓等於B氣體氣壓。')
