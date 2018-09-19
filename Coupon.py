import string
import random
import pymysql.cursors

# 为了报错需要做个class,不然那会出现错误未定义的报错，具体原理尚不明确，待学习。
class LengthError(ValueError):
   def __init__(self, arg):
      self.args = arg

    # 生成一个随机验证码
def code_generator(lenOfCode):
    poolOfChar = string.ascii_letters + string.digits
    randomCode = lambda x,y:''.join([random.choice(x) for i in range(y)])
    return (randomCode(poolOfChar, lenOfCode))

    # 生成主键(为保证验证码位数一致，在不足位数时，前面加0)
def key_generator(inputNum, lenOfKey):
    lenOfInput = len(str(inputNum))
    if lenOfInput > (lenOfKey):
        raise LengthError("lenOfKey is too long!")
    else:
        return '0' * (lenOfKey - lenOfInput) + str(inputNum)

"""
主要方法的参数：
number    : 验证码数量 
lenOfCode ：验证码 
lenOfKey  ：主键长度
"""
def code_factory(number=200, lenOfCode=15, lenOfKey=4):
    # 拼接验证码，标识符和主键
    tempCode, flg = '','L'
    #最后的问题出在这里，number忘记加range()，导致无法循环

    for n in range(number):
        try:
            yield (code_generator(lenOfCode)+ flg+ key_generator(n, lenOfKey))
        except LengthError:
            print ("number is larger than the lenth of Key")


def activationcode2sql():
    #打开数据库连接
    connect=pymysql.Connect( host='10.0.6.55',port=3306,user='admin',passwd='Admin_12345',db='python',charset='utf8')
    cursor = connect.cursor()
    f1 = open("text.txt", "r")
    lines = f1.readlines()  # 读取全部内容
    n=0
    for line in lines:
        n=n+1
        a = line.strip('\n').split(' ') #数组形式
        b="".join(map(str,a)) #转换为字符串形式
        #cursor.execute("INSERT INTO t1(code)  VALUES('%s')", line.strip())
        sql="INSERT INTO t1(id,code) VALUES('%s','%s')"
        data=(n, b)
        cursor.execute(sql %data)
    #cursor.fetchall()
    # print('成功插入', cursor.rowcount, '条数据')
    print('成功插入', n, '条数据')
    connect.commit()
    f1.close()
    cursor.close()


if __name__ == '__main__':
    f = open("text.txt", 'wb')
    for code in code_factory():
        print(code)
        a='\r\n'
        s=code+a
        s = s.encode()
        f.write(s)
    f.close()
    activationcode2sql()


