data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

import json

json_str = json.dumps(data)
print("original data:", repr(data))
print("json data:", json_str)

data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

# 写入 JSON 数据
with open('Content.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('Content.json', 'r') as f:
    data = json.load(f)
