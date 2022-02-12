"""
W3C School 程式語言免費線上教學網站:
有許多熱門程式語言的入門教學，還可以在網站上直接執行測試、練習，是免費又好用的程式學習資源。
Python tutorial on W3C School:
https://www.w3schools.com/python/
"""

# 基本的字串處理

s_Shakespeare = "To be or not to be, it's a question." # by William Shakespeare(莎士比亞)

poem_BaiLi = """
鳳凰臺上鳳凰遊，鳳去臺空江自流。
吳宮花草埋幽徑，晉代衣冠成古丘。
三山半落青天外，二水中分白鷺洲。
總爲浮雲能蔽日，長安不見使人愁。
""" # by 詩仙──青蓮居士‧李白《登金陵鳳凰臺》

s_YA = "Not いい加減，but 良い加減。\nいい加減じゃなくて良い加減。\nUnderstand?" # by Y.Akiyama

# 霹靂布袋戲虛擬角色：
poem_JinTao = '知水為命順逆同，\n浩然莫測深淺中。\n無波滄海掩洶湧，\n淵渟不動現魚龍。' # 淵渟無跡‧靜濤君
poem_FeyChanJuen = '一覺遊仙好夢，任它竹冷松寒。軒轅事，古今談，風流河山。沉醉負白首，抒懷成大觀。醒，亦在人間；夢，亦在人間。' # 玄黃三乘──人覺‧非常君
poem_ChengLingSha = "七絃撫盡，何處覓知音，但向朗月空林；翰墨殘跡，誰得千秋理，且聽松濤竹意。" # 悠弦燭遠‧夏承凜


# Python中所謂字串，其實是一個由字元(character)構成的list，使用時可以當成一般list來操作。順便一提，UTF-8編碼的一個字元大小為3個位元組(B, byte)，亦即24個位元(b, bit)。
print(poem_BaiLi) # 印出整個字串(多行字串)
print(poem_FeyChanJuen) # 印出整個字串(單行字串)
print(poem_ChengLingSha[2]) # 「撫」
print(poem_JinTao[-7]) # 「渟」
print(s_YA[13:17]) # 部分字串/子字串：13 ~ 16, 「良い加減」

print() # 換行用
# 將字串視為一個由許多字元構成的list，逐一取出字串中的字元。
for i in range(len(poem_ChengLingSha)): # for item in poem_ChengLingSha:
    print(poem_ChengLingSha[i])
print() # 換行用

# 字串切割
sentences = s_YA.split("\n") # 字串切割：以給定的字串('\n')切割字串(s_YA)，並將切割好的字串串列(a list of strings)存在一個變數中。
for sentence in sentences:
    print(sentence)
print() # 換行用

# 子字串取代
print('原字串       = ' + s_Shakespeare)
text = s_Shakespeare.replace('be', 'do') # 子字串取代：以給定的字串取代原字串中的特定子字串。
print('取代後字串   = ' + text)

print() # 換行用
# 檢查字串中是否有特定字串
print("淵渟" in poem_JinTao)
print("淵停" in poem_JinTao)
print() # 換行用
# 檢查字串中是否沒有特定字串
print(not "淵渟" in poem_JinTao)
print(not "淵停" in poem_JinTao)
