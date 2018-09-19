class Student(object): #没有明确继承的时候就是继承基类object
    def __init__(self,name,city): #创建Studen 实例的时候，就把name通过定义一个特殊方法__init__ 绑上去,
        self.name=name
        self.city=city
        print("My name is %s and come from %s"%(name,city))

    def talk(self):
        print("Hello,world!")

#实例化一个stu对象
stu1=Student("zhangsan","nanyang")
stu1.talk()