python 学习笔记

1.	Python基本语法
	换行语法块
	标识符 和关键字
	注释 单引和双引号的区别
	多行语句
	模块导入

2.	数据类型
	Number: 
int  符号顺序  
指数 (**) | 翻转,一元加减（~+-）| 乘除模，取整（* / % //） |加减 
|左右移位（>><<）| 位运算|比较| is(not) | （not） in | and (not )
Float bool complex 

	String  list set tuple  dict 
有序集合可以 获取切片和索引,但是只有list 动态赋值


I.	数字：需要记住几个函数
abs(x)【绝对值 整】	ceil(x)【上入整数】	exp(x)【e的x次幂]】	
fabs(x) 【绝对值】	log(x) 【e的对数】
log10(x) 【10的对数】	
max(x1, x2,...)	min(x1, x2,...)	pow(x, y) 【x**y 】	
round(x [,n]) 
【x的四舍五入值】	sqrt(x)
x的平方根		
			
			
choice(seq)
【随机序列的元素】	randrange ([start,] stop [,step])	random()【实数(0-1) 】	shuffle(lst)
【元素随机排序】
uniform(x, y)
【实数，它在[x,y]范	4舍6入5看齐,奇进偶不进		


II.	字符串
字符串主要是切片和索引，转义符号 只记录 特殊用法的，其他和 java 差不多
\(在行尾时)【续行符】	\a响铃	\b退格(	\e转义
\000空	\v纵向制表符	\f换页	\oyy [\o12代表换行]
\xyy \x0a代表换行	\other		

运算： +  *  []  in  not in
字符串格式化
%s 字符串	%f 浮点数	%g   %f%e
%d 整数	%e 科学计数	 %G = %f%E

字符串内建函数

capitalize() 首字母大写		center(width, fillchar) 指定的宽度 
width 居中的字符串	count(str,beg=0,end=len(string)) str 在 string 里面出现的次数
bytes.decode(encoding="utf-8", errors="strict")
encode(encoding='UTF-8',errors='strict')
encoding 指定的编码格式编码字符串	Endswith
expandtabs(tabsize=8
find(str, beg=0 end=len(string))
index() lower() upper()

