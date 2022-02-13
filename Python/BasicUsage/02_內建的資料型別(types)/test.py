a = 7
b = 3

print("設 a = %d, b = %d，則\n" % (a, b))
print('a + b = %d' % (a + b)) # +
print('a - b = %d' % (a - b)) # -
print('a × b = %d' % (a * b)) # ×
print('a ÷ b = %f' % (a / b)) # ÷(一般除法，所得結果為「浮點數」)
print('a ÷ b = %d' % (a // b)) # ÷(整數除法：求商，所得結果為「整數」)
print('a mod b = %d' % (a % b)) # ÷(整數除法：求餘數，所得結果為「整數」)
print('a ÷ b = %d ... %d' % (a // b, a % b)) # ÷(整數除法，所得結果為「整數」)
print('a^b(a的b次方) = %d' % a ** b) # a^b，a的b次方

print('I love you.\n' * 3) # 將字串重複n次
