###练习8 简单统计
from collections import Counter
import pandas as ps
from collections import OrderedDict as odic

content = ps.read_csv("./data.csv")
print(content, "\n", type(content))

print(content.values[0])

c = Counter(content.values[0])

data = {"go": "0.1", "java": "1.9", "python": "1.6", "c++": "3.0"}

order = odic(data)

print(order)
