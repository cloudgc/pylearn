**python 学习笔记**

`1.	Python基本语法`
* 换行语法块
*	标识符 和关键字
*	注释 单引和双引号的区别
*	多行语句
*	模块导入

2.	数据类型
*	Number: 
int  符号顺序  
指数 (**) | 翻转,一元加减（~+-）| 乘除模，取整（* / % //） |加减 
|左右移位（>><<）| 位运算|比较| is(not) | （not） in | and (not )
Float bool complex 

*	String  list set tuple  dict 
有序集合可以 获取切片和索引,但是只有list 动态赋值


I.	数字：需要记住几个函数

||||
|--|--|--|
|abs(x)【绝对值 整】	|ceil(x)【上入整数】  |exp(x)【e的x次幂]】	|
|fabs(x) 【绝对值】	|log(x) 【e的对数】  |log10(x) 【10的对数】	|
|max(x1, x2,...)    |	min(x1, x2,...) |pow(x, y) 【x**y 】	    |
|round(x [,n]) 【x的四舍五入值】|sqrt(x)x的平方根	                |	
|choice(seq)【随机序列的元素】|randrange ([start,] stop [,step])	random()【实数(0-1) 】|shuffle(lst)【元素随机排序】|
|uniform(x, y)【实数，它在[x,y]范	4舍6入5看齐,奇进偶不进|		


II.	字符串
字符串主要是切片和索引，转义符号 只记录 特殊用法的，其他和 java 差不多

|||||
|--|--|--|--|
|(在行尾时)\【续行符】|	\a响铃|	\b退格|	\e转义|
|\000空|	\v纵向制表符	|\f换页	|\oyy [\o12代表换行]|
|\xyy |\x0a代表换行|	\other	|	

运算： +  *  []  in  not in
字符串格式化
%s 字符串	%f 浮点数	%g   %f%e
%d 整数	%e 科学计数	 %G = %f%E
b"str" 二进制 r"[0-9]" 代表正则表达式

`字符串内建函数`

|||
|--|--|
|capitalize() 首字母大写	                        |center(width, fillchar) 指定的宽度                           |
|width 居中的字符串                              |count(str,beg=0,end=len(string)) str 在 string 里面出现的次数|
|bytes.decode(encoding="utf-8", errors="strict")|encode(encoding='UTF-8',errors='strict')|
|encoding 指定的编码格式编码字符串                |	Endswith|
|expandtabs(tabsize=8                           |find(str, beg=0 end=len(string))|
|index() lower() upper()||

`list语法`

|||||
|-|-|-|-|
|len(list) 元素个数      |max(list) 列表元素最大值| min(list)列表元素最小值|list(seq)元组转换为列表  |
|list.append(obj)       |list.count(obj)        |list.index(obj)        |list.insert(index, obj) |
|list.pop(obj=list[-1]) |list.remove(obj)       | list.reverse()        |list.sort([func])       |
|list.clear() |	list.copy()|

`tuple语法`

|||
|-|-|
|len(tuple)计算元组元素个数。 |max(tuple) 返回元组中元素最大值|
|min(tuple)返回元组中元素最小值。 |	tuple(seq)将列表转换为元组。|

**`dict语法`**

_hash key_ 可以覆盖 没有异常
*len(dict)*元素个数   str(dict) 输出字典

_dict.clear()_ 删除字典内所有元素  dict.copy() 字典的浅复制

_dict.fromkeys()_创建一个新字典 dict.get(key, default=None)

_key in dict_ 键在字典dict里返回true，否则返回false 
 
_dict.items()_ 返回可遍历的(键, 值) 元组数组

dict.keys()   dict.values()  dict.setdefault(key, default=None)

*dict.update(dict2)*字典dict2的键/值对更新到dict里

_pop(key[,default])_   删除字典给定键 key 所对应的值  	_popitem()_   随机返回并删除字典中的一对键和值
 

**3.循环**

和java 中的 循环基本保持一致 注意continue和pass 区别 

_yield_ 生成迭代器 并且可以通过 next() 函数调用

**4.函数调用**

注意LEGB

嵌套列表推导式

**5.模块导入**

from 包.模块(./..隐士导入) import 内容 查找路径是 当前根据 dir(sys) 寻找

模块之间调用from . import  要在模块的高级包上调用 否则出错或者使用 绝对路径导入 from note.forimport import module1

**6.file**

|mode|r|r+|w|w+|a|a+|
|----|--|--|--|--|--|--|
|read        |+|+| |+| |+|
|wirte       | |+|+|+|+|+|
|create      | | |+|+|+|+|
|overwrite   | | |+|+| | |
|indexstart  |+|+|+|+| | |
|indexend    | | | | |+|+|

||||
|-|-|-|
|file.close()   |file.tell() |file.truncate([size])   从文件的首行首字符开始截断为 size 个字符，无 size 表示从当前位置截断；其中 Widnows 系统下的换行代表2个字符大小。|
|file.flush()   |file.readline([size])   读取整行，包括 "\n" 字符|file.readlines([sizeint]) 若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。|
|file.seek(offset[, whence])|file.write(str)|file.writelines(sequence)  向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。|
|file.next()|file.read([size])   未给定或为负则读取所有|file.isatty()   如果文件连接到一个终端设备返回 True，否则返回 False
|pickle.load(file)|pickle.dump(file)

os 系统api

如Linux系统操作文件一样 可以精准控制文件权限和属组，文件的CURD , 软硬链接的控制

os.path.isfile()|os.path.exists()

|some error|||||
|-|-|-|-|-|
|Traceback|ZeroDivisionError|NameError|TypeError|KeyboardInterrupt|

**面向对象**

较java的oop简单 多继承 方法重写  没有接口  双下划线表示私有

异常大父类是 

+-- SystemExit

+-- KeyboardInterrupt

+-- GeneratorExit

+-- Exception


**标准库**

|||
|-|-|
|日期|from datetime import date|
|数学|import math|
|http|urllib,urllib.request import urlopen, from urllib.parse import urlencode|

**多线程**

创建：_thread.start_new_thread 继承threading.Thread 实现run方法

运行：start()  join() 

锁： threading.Lock() acquire() realease() 

队列 queue.put() queue.get()


**xml,json解析**

sax与dom4j 老生常谈了 

`json解析`

|json.dumps([ref])|json.loads([ref])|对象|
|--|--|--|
|json.dump([file])|json.load([file])|文件|



**RDBMS**

* mysql  ==> pymysql
  
  * error  DatabaseError
