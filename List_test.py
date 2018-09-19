'''
a=[1,2,3,"this is a list",[4,5,6]]
print(a[-1])
print(a[1:3])
print(a[-1:-3])
b=[4,5,6,"这是第二个列表"]
print(a+b)
print(a*2)
print(a[1],a[2])
print(a[0])
a.append("haha")
a.insert(3,"xmn")
L=[['1','2','3'],['4','5']]
print(L[0][0])
# a.pop([0])
print(a)

dict={"name":"xmn","age":"18","xueli":"本科"}
print(dict)
print(dict)
'''
# 无参函数
def addStr():
    str='python'
    list=[]
    for i in str:
        list.append(i)
    print(list)
addStr()

#有参函数
def addStr2(str):
    list=[]
    for i in str:
        list.append(i)
    print(list)
addStr2('java')

#有默认参函数,没有传参数的时候，默认使用默认值
# def addStr2(str='123'):
#     lilst=[]
#     for i in str:
#         list.append(i)
#     print(list)
# addStr2('java')

def addSum(x,y):
    sum=0
    if x<=y:
        for i in range(x,y+1):
            sum+=i
            i+=1
        return(sum)

    elif x>y:
        for i in range(y,x+1):
            sum+=i
            i+=1
        return (sum)

result=addSum(1,100)
print(result)