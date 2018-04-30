n = 100
while n < 1000:
    n += 1
print(n)

# while 1:
#     print("====")


for k in range(1, 10):
    print(k)

languages = ["C", "C++", "Perl", "Python"]

for i in languages:
    print(i, end=", ")

for i in range(4):
    print(i, languages[i], end=" ")

for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print('当前字母为 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当期变量值为 :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
print('当前字母 :', letter)

print("Good bye!")

sequence = [12, 34, 34, 23, 45, 76, 89]

for i, j in enumerate(sequence):
    print(i, j, end="..")

print("\n")


###冒泡排序
def paixu(li):
    max = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            if li[x] > li[x + 1]:
                max = li[x]
                li[x] = li[x + 1]
                li[x + 1] = max
            else:
                max = li[x + 1]
    print(li)


paixu([41, 23344, 9353, 5554, 44, 7557, 6434, 500, 2000])
