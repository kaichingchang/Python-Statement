#真假值的字面常數
a = True
b = False
print(not a)       #False
print(a and b)     #False
print(a and not b) #True
print(a or b)      #True

print("----------")

#數字
a = 1
b = 0
print(not a)       #False
print(a and b)     #0
print(a and not b) #True
print(a or b)      #1

print("----------")

#串列
a = [1]
b = []
print(not a)       #False
print(a and b)     #[]
print(a and not b) #True
print(a or b)      #[1]

#《程式語言教學誌》的範例程式
# http://kaiching.org/
# 檔名：logic.py
# 功能：示範邏輯運算
# 作者：張凱慶
