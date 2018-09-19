

'''
def User(len,num):
    a=chr(random.randint(65,90))
    b=chr(random.randint(97,122))
    c=random.randint(100,999)
    count=0
    while count<num:
        if len>5:
            
            acc=(a+b+str(c)+'@163.com')
            print(acc)
'''
import random,string

len=int(input("Please set the account length:"))
num=int(input("Please set need account number:"))

def Users(num,len):
    result = []
    a = string.ascii_lowercase #a-z
    b = string.ascii_uppercase #A-Z
    c = string.digits #0-9
    d = string.ascii_letters #a-z&A-Z
    count = 0
    while count < num:
        if len > 2:
            #choice(seq) 从序列seq中返回随机的元素
            a1 = random.choice(a)
            b1 = random.choice(b)
            c1 = random.choice(c)
            #sample(seq, n) 从序列seq中选择n个随机且独立的元素
            d1 = random.sample(d,len-3) #list的形式
            d1.append(a1)
            d1.append(b1)
            d1.append(c1)
            #random.shuffle()如果你想将一个序列中的元素，随机打乱的话可以用这个函数方法
            random.shuffle(d1)
            print(d1)
            '''
            语法：  'sep'.join(seq)        
            参数说明
            sep：分隔符。可以为空
            seq：要连接的元素序列、字符串、元组、字典
            上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串        
            返回值：返回一个以分隔符sep连接各个元素后生成的字符串
            '''
            users = ''.join(d1) + '@163.com' +'\n'
            if users not in result:
                result.append(users)
                count +=1
        else:
            print('请输入大于2的长度')
            break
    with open('users.txt','w') as fw:
        fw.writelines(result)

Users(num,len)





