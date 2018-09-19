# import re
#
# a="wdnwjfwj we hd 9#sdfekfmew 2011"
#
# b=re.sub("\D","",a)
# print(b)
import re
a = input('input your string:\n')
#at = re.sub('[^\d\+]', '', a)  #用正则表达式消去输入中的字母

# a = re.findall(r'\d+', s)
at=re.sub('\D',"+",a)
print(at)
try:
    print('result:{}={}'.format(at, eval(at)))   #eval是自带函数，会帮你算是多少
except:
    print('result: error')  #如果eval报错，表示加号两边都为字符