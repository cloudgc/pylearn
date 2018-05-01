##练习4 循环
##
original = [
    ["腾讯", "阿里巴巴", "苹果", "google", "facebook", "amazon"],
    ["HK：000700", "BABA", "apple", "google", "FB", "AMZN"]
]

dc = {}

for i in range(6):
    dc[original[0][i]] = original[1][i]

print(dc)

for x, y in dc.items():
    print("name:{} , code:{}".format(x, y))
