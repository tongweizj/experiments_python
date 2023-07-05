'''

这个笔记，主要是记录学习中遇到的各类代码

'''



'''
第一章
'''



#函数

def data(x,y):
	print（each_intem）


#发布一个函数
> python3 setup.py sdist  #构建发布文件
> python3 setup.py install #发布到本地


## 异常处理机制

try:

	'your code ...'   #被监控的代码

except:
	'code'   #发生错误时，运营的代码。也可以写’pass‘，就是忽视错误，直接往下运行


try:

	'your code ...'   #被监控的代码

except IOError:   #错误类型：ValueError、
	'code'   #针对特殊错误类型，执行相应的代码


#写入文本文件
the_file = open('sketch.txt','w') #写入文件th
the_file = open('sketch.txt','w+') #覆盖写入
the_file = open('sketch.txt','a') #不覆盖原文件写入文件
print('hello world!',file = the_file) #用print 写入文件
the_file.close()


#文件读写时的，异常处理

try:
	'your code...'

except IOError:      
	pass
finally：
	file.close()    #如果发生错误，会先运行 except，然后运行finally
	                #如果没有发生错误，直接运行 finally


#指定函数保护

try:
	with open('its.txt', 'w') as data:
		'your code...'

except IOError:      
	pass
                   #如果发生错误，会把data 运行完


# pickle 用法

import pickle
	...
try：
	with open('its.txt', 'wb') as data:    #wb 2进制打开写文件
		pickle.dump('123', data)

	with open('its.txt','rb') as data:     #rb  2进制读文件
		a_list = pickle.load(data)  

except IOError as err:
	print('File error:'+str(err))


## 数据处理

clean_mikey = []
for each_t in mikey:
	clean_mikey.append(sanitize(each_t))

clean_mikey = [sanitize(each_t) for each_t in mikey]  #两端代码是等价的

#sanitize(each_t)  这段代码是处理数据的



